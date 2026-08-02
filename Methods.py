#Methods

#Append
numbers=[10,20,30,20]
#         0  1  2  3
numbers.append(100);
print(numbers)

#Insert
numbers.insert(1,15)
print(numbers)

#inserting a string
numbers.insert(1,"home")
print(numbers)

print(numbers.index(20));
print(numbers.count(20));
print(numbers.pop());
print(numbers.pop());   #When we add a pop whatever the last figure is completely dragged out from the list.
print(numbers)

#remove                 #any character from the list can be removed.
numbers.remove("home")
print(numbers)

#del
colors=["white","green","blue"];
print(colors)
#print(colors)

values=[10,20,30,40]
values.reverse();
numbers.reverse();
print(values);
print(numbers);

#sort
numbers.sort();
print(numbers);
colors.sort(key=len)
print(colors);
