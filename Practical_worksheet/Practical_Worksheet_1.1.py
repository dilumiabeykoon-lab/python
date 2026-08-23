name=input("Enter customer name:")
age=int(input("Enter Age:"))
currency="RS."
print("-----------Ticket Details----------")
if age<0 or age>120:
    print("Invalid age.")
else:
    if age<12:
        Discount=0
        category="Child"
        Ticket_Price=int(400)
        print("Customer name:",name)
        print("Category:",category)
        print("Ticket price:",currency,Ticket_Price)
        print("Discount:",currency,Discount)
        print("Amount Payable:",currency,Ticket_Price)
    else:
        category="Adult"
        Ticket_Price=int(800)
        if age>60:
                Discount=Ticket_Price*10/100
                Amount_Payable=Ticket_Price-Discount
                print("Customer name:",name)
                print("Category:",category)
                print("Ticket price:",currency,Ticket_Price)
                print("Discount:",currency,Discount)
                print("Amount Payable:",currency,Amount_Payable)
        else:
            Discount=0
            Amount_Payable=Ticket_Price
            print("Customer name:",name)
            print("Category:",category)
            print("Ticket price:",currency,Ticket_Price)
            print("Discount:",currency,Discount)
            print("Amount Payable:",currency,Amount_Payable)








    

