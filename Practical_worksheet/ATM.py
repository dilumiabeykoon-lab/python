accounts={
    "A001":{"Name":"Dilumi","Balance":20000},
    "A002":{"Name":"Sara","Balance":15000}
}
while True:
    print("===ATM MENU===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3.Withdrawal")
    print("4.View Transaction")
    print("5.Exit")

    choice=int(input("Enter Choice:"))

    if choice==5:
        print("Thank you!")
        break

    account_id=input("Enter Account ID:")

    if account_id not in accounts:
        print("Invalid Account No.")
        continue
    account=accounts[account_id]

    if choice==1:
        print("Your account balance is:",account['Balance'])

    if choice==2:
        print("Deposit successfull")

    if choice==3:
        print("Withdrawal successfull")

    if choice==4:
        print("Your Transactions:")


    