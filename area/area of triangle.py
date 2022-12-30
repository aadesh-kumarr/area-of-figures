x=input("dear user, please enter your name")
print("welcome",x)
print("this programme will help you to calculate")
print("area of triangle whose sides are kown to us")

#--------------area of triangle--------


def intro():
    print("1: to continue")
    print("2: to exit\n")
    inpp()
    
def inpp():
    x=int(input("enter your choice"))
    if(x==1):
        area()
    elif(x==2):
        exit
    else:
        print("invalid option")
        intro()
        print("\n\n")

def area():
    a = float(input('Enter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))
    print("\n\nthe units for area are not been")
    print("calculated by this programme")



    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # calculate the area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print('The area of the triangle is ',area)


#------------main-------------
intro()
