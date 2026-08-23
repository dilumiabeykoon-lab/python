#break
password="Dilu@123"
user_password=input("Enter password:")
while True:
    user_password=input("Re-enter the password:")
    if password==user_password:
        print("Authorized")
        break;

