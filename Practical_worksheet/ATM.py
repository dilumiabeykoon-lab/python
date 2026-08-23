accounts={
    "A001":{"Name":"Dilumi","Balance":20000},
    "A002":{"Name":"Sara","Balance":5000}
}
transactions=[]
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
        #print("Your account balance is:",account['Balance']) 
        print(f"Balance:{account["Balance"]}")

    if choice==2:
        amount=float(input("Enter Amount:"))
        account["Balance"]+=amount
        transactions.append({
            "Account":account_id,
            "Type":"Deposit",
            "Balance":amount})
        
        print("Deposit successfull")

    if choice==3:
        amount=float(input("Enter Amount:"))
        if amount<= account["Balance"]:
            account["Balance"]-=amount
            transactions.append({
                "Account":account_id,
                "Type":"Withdrawal",
                "Balance":amount})
            print("Withdrawal successfull")
        else:
            print("Insufficient amount entered.")

        

    if choice==4:
        print("\nTransaction History")
        print("Your Transactions:")

        for transaction in transactions:
            if transaction["Account"]==account_id:
                print(f"{transaction["Type"]}-{transaction["Balance"]}")
            else:
                print("Invalid Transactions")
        