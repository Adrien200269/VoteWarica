card="inserted"
pin_number=123
selection="withdraw"
atm_balance=1000

if card=="inserted":
    if pin_number==123:
     print("Acess granted, Please select an option.")
     if selection =="withdraw":
       if atm_balance >=1200:
        print("Please take your cash.")
       else:
        print("Insufficient cash.")
     elif selection== "Deposit":
      print(("Your deposit has been accepted"))
     elif selection=="Balance Check":
      print("Your current balance is (atm_balance).")
     else:
      print("Invalid selection. Please try again")
    else:
     print("Incorrect PIN. Please try again")
else:
    print("No card detected, Please insert you card")