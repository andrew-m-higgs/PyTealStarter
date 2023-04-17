from pyteal import *
import sys
import os

"""
Organise constants, like function names, into tidy class
"""
class Constants:
    # Function Names
    method = Bytes("method")

    # Global State Variables Names
    creator = Bytes("creator")

    # Local State Variables Names
    # HasPaid = Bytes("HasPaid")

    # Constants
    # Fee = Int(1000)


"""
The Approval Program defines the rules and conditions for executing transactions within a
smart contract, allowing or rejecting them based on the specified logic.
"""


def approval_program():
    """
    Application call handlers
    """
    initialize = Seq(App.globalPut(Constants.creator, Txn.sender()), Approve())

    method = Seq(Approve())

    onDelete = Seq(Assert(Txn.sender() == App.globalGet(Constants.creator)), Approve())

    onUpdate = Seq(Assert(Txn.sender() == App.globalGet(Constants.creator)), Approve())

    """
    Handle all NoOp Application calls with the appropriate handler based on the first app argument taken as the function name.
    """
    onCall = (
        If(
            Or(
                Txn.type_enum() != TxnType.ApplicationCall,
                Txn.application_args.length() == Int(0),
            )
        )
        .Then(Reject())
        .ElseIf(Txn.application_args[0] == Constants.method)
        .Then(method)
        .Else(Reject())
    )

    """
    This return statement handles different transaction types within the approval program, executing corresponding logic: initialize for creation, approve opt-in and close-out, onDelete for deletion, onUpdate for updates, onCall for function calls, or reject invalid transactions.
    """
    return (
        If(Txn.application_id() == Int(0))
        .Then(initialize)
        .ElseIf(Txn.on_completion() == OnComplete.CloseOut)
        .Then(Approve())
        .ElseIf(Txn.on_completion() == OnComplete.OptIn)
        .Then(Approve())
        .ElseIf(Txn.on_completion() == OnComplete.DeleteApplication)
        .Then(onDelete)
        .ElseIf(Txn.on_completion() == OnComplete.UpdateApplication)
        .Then(onUpdate)
        .ElseIf(Txn.on_completion() == Int(0))
        .Then(onCall)
        .Else(Reject())
    )


"""
The Clear Program defines the logic for gracefully exiting a contract and releasing resources when
 a user opts out, while ensuring compliance with the contract's conditions.
"""


def clear_program():
    program = Seq(Approve())
    return program


"""
Compile to TEAL bytecode, and also as string variables exproted from typescript for easy access.
"""
if __name__ == "__main__":
    # Compiles the approval program
    approve = compileTeal(approval_program(), mode=Mode.Application, version=8)
    clear = compileTeal(clear_program(), mode=Mode.Application, version=8)
    with open(os.path.join(sys.path[0], "approve.teal"), "w+") as f:
        f.write(approve)

    # Compiles the clear program
    with open(os.path.join(sys.path[0], "clear.teal"), "w+") as f:
        f.write(clear)

    with open(os.path.join(sys.path[0], "source.ts"), "w+") as f:
        sourceCode = f"export const approveSource = `{approve}`\nexport const clearSource = `{clear}`"
        f.write(sourceCode)
