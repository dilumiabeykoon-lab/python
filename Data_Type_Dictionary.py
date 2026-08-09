student={
    "name":"Nimal",
    "age":18,
    "city":"Kandy"
}
print(student)

#methods
#Add new data
student["grade"]="A"
print(student);

#Update existing data
student["age"]=16
print(student);

'''#Delete values using pop
student.pop("city")
print(student);

#Delete values using popitem
student.popitem()
print(student);

#Delete all values using clear
student.clear()
print(student);'''

#functions
print(len(student));

print(type(student));

#the original dictionary is not changing.Only a copy is created with the sorted values.
print(sorted(student))

print(min(student))

print(max(student))

#create copy of student dictionary
nw_std=dict(student)
print(nw_std)

#methods which are more secured.

#get()
print(student.get("name"))

#item()
print(student.items())

#keys()
print(student.keys())

#values()
print(student.values())

#fromkeys()
nw_infolist=dict.fromkeys(["A","B","C"],0)
print(nw_infolist)

nw_infolist=dict.fromkeys(["A","B","C"])
print(nw_infolist)

