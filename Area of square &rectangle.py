side1=int(input("Enter side value:"))
side2=int(input("Enter second value:"))
if side1==side2:
    print("Shape is Square")
    print("Area of Square is:", side1*side2)
else:
    print("Shape is Rectangle")
    side=side1+side2
    area=2*side
    print("Area of Rectangle is:", area)


