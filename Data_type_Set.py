#in SET duplicates are removed.
#We use set to remove duplicate values automatically.
numbers={5,8,10,8,5}
print(type(numbers))
print(numbers)
print(numbers)
print(numbers)

#len
print(len(numbers))

#Looping (for)
for x in numbers:
    print(x)

#in operator 
print(20 in numbers)

#add(Adds only 1 value)
numbers.add(40)
print(numbers)

#update(Add a set of values to the existing set)
numbers.update({40,50})
print(numbers)

#remove(If the value 20 is not existing it makes an error)
numbers.remove(10)
print(numbers)

#discard()
numbers.discard(40)
print(numbers)

#pop
x=numbers.pop()
print(x)

#clear
numbers.clear()
print(numbers)

#del
del numbers
