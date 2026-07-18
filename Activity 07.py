distance=7413; #km
speed=18; #km/h
time=distance/speed;
print("Travel time is",time);

#input function
#There are two ways to convert data types.
#1st Method
distance=int(input("Enter your distance:"));
speed=12 #km/h
time=distance/speed;
print("You will travel for",time,"hours");

#2nd Method
distance=input("Enter your distance:");
distance=int(distance);
speed=12 #km/h
time=distance/speed;
print("You will travel for",time,"hours");

distance=input("Enter your distance:");
distance=int(distance);
speed=12 #km/h
time=distance/speed;
print("You will travel for",round(time,2),"hours");