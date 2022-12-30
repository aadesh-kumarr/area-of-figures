import math
a=int(input("1 for curved surface area\n2 for total surface area "))
b=int(input("enter the length of cone"))
c=int(input("enter the radius of cone"))
l=math.sqrt(b**2+c**2)
if a==1:
    print("curved surface area of the given cone is",math.pi*c*l)
elif a==2:
    print("total curve dsurface area of the given cone is",math.pi*(l+c)*c)