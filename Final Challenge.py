name=input("Enter your name:");
id=input("Admission no:" );
age=int(input("Enter your age:"));
height=float(input("Enter your height:"));
school=input("Enter your school:");
Sub1=int(input("Enter your mark for Subject 1:"));
Sub2=int(input("Enter your mark for Subject 2:"));
Sub3=int(input("Enter your mark for Subject 3:"));

#Calculating the avg
total=Sub1+Sub2+Sub3;
avg=total/3;

#The result generated
print("Student Name:",name)
print("Student Admission no:",id)
print("Age:",age)
print("Height",height)
print("School",school)
print("Marks for subject 1",Sub1)
print("Marks for subject 2",Sub2)
print("Marks for subject 3",Sub3)
print("The average is",avg)