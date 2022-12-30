import math
a=int(input("1 for lateral surface area/2 for complete surface area"))
b=int(input("enter the length of cylinder"))
c=int(input("enter the radius of cylinder"))
v=2*math.pi*b*c
    
if a==1 :
     print("lateral surface area of the given cylinder is",v)
elif a==2:
    print("total surface are of the given cylinder is",v+2*math.pi*c**2)
else :
    print("wrong input")