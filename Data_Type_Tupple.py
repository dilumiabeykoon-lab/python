t=(10,20,30,40,50,30)
print(t[0])
print(t[3])
print(t[:3])
print(t[1:3])
print(t[-3])
print(t[-3:])

#we can not change the tupple using methods.(insert,append,copy)
#we can use some as count, index

print(t.count(30));
print(t.index(40));

#tupplewith functions.
print(len(t));
print(min(t));
print(max(t));
print(sum(t));
print(sorted(t));

tuple(reversed(t));
print(t);

tuple([1,2,3,4,5,6])
print(tuple)