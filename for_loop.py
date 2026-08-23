for x in[10,20,30]:         
    print(x)
print("----------------------------------------------")
#You must have a sequence to perform for loop
#the values in the list passes to variable "x" in saquence and print the 3 numbers looping for three consective times.
# We dont need to know the starting point, ending point and the pattern.But we can customize the starting,ending and 
# switch point.

#FOR RANGE
#EG:1
for x in range (5):
    print(x)
print("----------------------------------------------")

for x in range(3,8):
    print(x)
print("----------------------------------------------")

for x in range(2,11,2):
    print(x)
print("----------------------------------------------")

for x in range(5,0,-1):
    print(x)
print("----------------------------------------------")

#Eg:2
word="education"
count=0
for ch in word:
    if ch in "aeiou":
        count=count+1
print(count)
print("----------------------------------------------")

data="ICT2026"
for ch in data:
    if ch.isdigit():
        print(ch)

#isdigit is a method used to filter numbers from a string.
print("----------------------------------------------")

#Using range with a lsit
marks=[65,72,81,55,90]
for i in range(len(marks)):
    print(i,marks[i])
print("----------------------------------------------")

#For loop with Dictionaries.
student={"name":"Kamal",
         "age":18,
         "marks":85
         }

for x in student:
    print(x)
print("----------------------------------------------")
for key in student.keys():
    print(key)
print("----------------------------------------------")
for values in student.values():
    print(values)
print("----------------------------------------------")

for a,b in student.items():
    print(a,b)