print('enter your choice')
a= int(input('enter your choice 1 for diagonal length/2 for length of side'))
if a==1:
    b=float(input("enter the length of the diaonal"))
    print("the are of the square is",1/2*b*b)
elif a==2:
    b=float(input("enter the length of side"))
    print("area of circle",b*b)
else:
    print("invalid choice")
    
