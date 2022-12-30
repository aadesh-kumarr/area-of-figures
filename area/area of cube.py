from traceback import print_tb


print("____________________ area of cube_________________")
def takeinp():
    s=int(input("enter the side of cube"))
    a=int(input("1 for total surface area \n 2 for lateral surface area"))
    if a==1:
        print("the total surfae area of the given cube is",6*s*s)
    elif a==2:
        print("the lateral surface area of the cube is",4*s*s)
    else:
        print("invalid input")
        takeinp()
takeinp()

    
