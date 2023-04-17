from pyteal import *
import sys
import os
import json

class Constants:
    """
    Constant strings used in the smart contracts
    """
    # Function Names
    method = Bytes("method")
    # Global State Variables Names
    # Owner = Bytes("Owner")
   
    # Local State Variables Names
    # HasPaid = Bytes("HasPaid")
   
    # Constants
    # Fee = Int(1000)



def approval_program():
    """
    Initialise the contract
    """
    initialize = Seq(
        Approve()
    )

    """
    Starter Methods
    """
    method = Seq(
        Approve()
    )

    onDelete = Seq(
        Approve()
    )

    onUpdate = Seq(
        Approve()
    )

    """
    Handle all NoOp calls
    Arguments:
    - At least one for the handler function name
    """
    onCall = If(Or(Txn.type_enum() != TxnType.ApplicationCall, Txn.application_args.length() == Int(0)))                        \
        .Then(Reject())                                                                                                 \
        .ElseIf(Txn.application_args[0] == Constants.method).Then(method)                            \
        .Else(Reject())

    """
    Handle program approval.
    """
    return If(Txn.application_id() == Int(0)).Then(initialize)                              \
        .ElseIf(Txn.on_completion() == OnComplete.CloseOut).Then(Approve())             \
        .ElseIf(Txn.on_completion() == OnComplete.OptIn).Then(Approve())                \
        .ElseIf(Txn.on_completion() == OnComplete.DeleteApplication).Then(onDelete)     \
        .ElseIf(Txn.on_completion() == OnComplete.UpdateApplication).Then(onUpdate)     \
        .ElseIf(Txn.on_completion() == Int(0)).Then(onCall)                             \
        .Else(Reject())


def clear_program():
    program = Seq(
        Approve()
    )
    return program


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