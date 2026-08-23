name=input("Enter Employee Name:")
salary=float(input("Enter Basic Salary:"))
allowance=float(input("Enter Allowance:"))
bonus=float(input("Enter Bonus:"))

print("---------Employee Salary Report---------")
if salary<0 or allowance<0 or bonus<0:
    print("Invalid input.")
    print("Salary, allowance and bonus can't be negative.")

else:
    g_salary=salary+allowance+bonus

    if g_salary<75000:
        tax=0
    elif g_salary>=75000 and g_salary<=99999:
        tax=g_salary*5/100
    elif g_salary>=100000 and g_salary<=149999:
        tax=g_salary*10/100
    else:
        tax=g_salary*15/100

net_salary=g_salary-tax

if g_salary>=150000:
    exc_performance_bonus="Yes"
else:
    exc_performance_bonus="No"

if net_salary>120000:
    Annual_incentive="Yes"
else:
    Annual_incentive="No"

if bonus>25000:
    high_performer="Yes"
else:
    high_performer="No"

print("Employee Name:",name)
print("Gross Salary:Rs.",g_salary)
print("Income Tax:Rs.",tax)
print("Net Salary:",net_salary)
print()
print("Executive Performance:",exc_performance_bonus)
print("Annual Incentive:",Annual_incentive)
print("High performer:",high_performer)




