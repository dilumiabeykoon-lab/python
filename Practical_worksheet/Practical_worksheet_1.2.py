name=input("Enter student's name:")

sub1=int(input("Enter Mathematics Mark:"))
sub2=int(input("Enter Science Mark:"))
sub3=int(input("Enter ICT Mark:"))
marks=[sub1,sub2,sub3]
'''#validation
if sub1<0 or sub1>100:
    print("Invalid mark entered")
if sub2<0 or sub2>100:
    print("Invalid mark entered")
if sub3<0 or sub3>100:
    print("Invalid mark entered")'''


if sub1>0 and sub1<100 and sub2>0 and sub2<100 and sub3>0 and sub3<100:

    total=sub1+sub2+sub3
    avg=total/3

    if avg>=85:
        grade="Distinction"
    elif avg>74 and avg<85:
        grade="Merit"
    elif avg>64 and avg<75:
        grade="Credit"
    elif avg>49 and avg<65:
        grade="Pass"
    else:
        avg<50
        grade="Fail"

    if avg>=90:
        academic_excellence="Yes"
    else:
        academic_excellence="No"

    if sub1>80 and sub2>80 and sub3>80:
        best_all_rounder="Yes"
    else:
        best_all_rounder="No"

    if sub1<35 or sub2<35 or sub3<35:
        improvement="Yes"
    else:
        improvement="No"

    print("----------Student Performance Report-----------")
    print("Student Name:",name)
    print("Total marks:",total)
    print("Average marks:",avg)
    print("Performance Grade:",grade)
    print()
    print("Academic Excellence:",academic_excellence)
    print("Best All-Round Award:",best_all_rounder)
    print("Improvement Notice:",improvement)
else:
    print()
    print("Invalid Marks Entered.")
    print("Please enter marks between 0 and 100")


        



