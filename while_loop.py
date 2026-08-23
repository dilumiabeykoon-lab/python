count=1
while count<=5:
    print(count)
    count=count+1

count=40
while count>19:
    print(count)
    count=count-1

count=0
while count<21:
    if count%2==1:
        print(count)
    count=count+1

#Repeat the while loop until the password is correct.
#Method 1
password="Dilu@123"
user_password=input("Enter the password:")
while password!=user_password:
    user_password=input("Re-enter password:")
print("You are authorized.")



