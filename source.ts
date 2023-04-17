export const approveSource = `#pragma version 8
txn ApplicationID
int 0
==
bnz main_l16
txn OnCompletion
int CloseOut
==
bnz main_l15
txn OnCompletion
int OptIn
==
bnz main_l14
txn OnCompletion
int DeleteApplication
==
bnz main_l13
txn OnCompletion
int UpdateApplication
==
bnz main_l12
txn OnCompletion
int 0
==
bnz main_l7
int 0
return
main_l7:
txn TypeEnum
int appl
!=
txn NumAppArgs
int 0
==
||
bnz main_l11
txna ApplicationArgs 0
byte "method"
==
bnz main_l10
int 0
return
main_l10:
int 1
return
main_l11:
int 0
return
main_l12:
txn Sender
byte "creator"
app_global_get
==
assert
int 1
return
main_l13:
txn Sender
byte "creator"
app_global_get
==
assert
int 1
return
main_l14:
int 1
return
main_l15:
int 1
return
main_l16:
byte "creator"
txn Sender
app_global_put
int 1
return`
export const clearSource = `#pragma version 8
int 1
return`