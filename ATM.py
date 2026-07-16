balance = int(input("Enter Balance:"))

Withdraw =int( input("Enter Withdraw amount:"))
if Withdraw < 0:
    print("Invalid Amount")
if Withdraw <= balance:
    print("Transaction Successful")
    print(f"Remaining Balance:{balance - Withdraw}")
else:
    print("Insufficient Funds")
    