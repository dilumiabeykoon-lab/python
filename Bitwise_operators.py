#Left bit [n<<x]=[n*2^x]
a=5
print(a<<1)
print(a<<2)

#Right bit [n>>x]=[n/2^x]
b=20
print(b>>1)

#BitWise &
c=5            #  0101
d=3            # &0011
print(c&d)     #  0001 <-----Convert to decimal(The decimal value is the output)

print(c|d)     #   0101
               #  |0011
               #   0111<-----Convert to decimal(The decimal value is the output)

print(c^d)     #   0101
               #  ^0011
               #   0110<-----Convert to decimal(The decimal value is the output)