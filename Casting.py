#Casting STRING
string="Jhon"
print(string)

A=bool(string)
print(A)
print(type(A))

B=list(string)
print(B)
print(type(B))

C=tuple(string)
print(C)
print(type(C))

D=set(string)
print(D)
print(type(D))

string_2="2000"

print(type(int(string_2)))
print(type(float(string_2)))

#Casting LIST
List=[110,"Blue","Kandy"]
print(List)
print(type(List))

E=str(List)
print(type(E))

F=tuple(List)
print(type(F))

G=set(List)
print(type(G))

#Casting TUPLE
Tuple=(1,2,5,"Anne")
print(type(tuple))

H=list(Tuple)
print(type(H))

I=set(Tuple)
print(type(I))

J=str(Tuple)
print(type(J))

#Casting SET
Set={2,4,6,8}
print(Set)

K=list(Set)
print(type(K))

L=tuple(Set)
print(type(L))

M=str(Set)
print(type(M))

