#------------------ Basic geometry :3 ------------------#
#Geometry.py

from math import sqrt
from math import pi
import pymsgbox

print("Commands are:")
print("pyth - Pythagorean Theorem")
print("comp - Complementary Angle")
print("supp - Supplementary Angle")
print("tri - Triangle Menu")
print("trap - Trapezoid Menu")
print("rect-s - Rectangular Solid")
print("sph - Sphere Menu")
print("circ - Circle Menu")
print(" ")
op = str(input("Command: "))

#-------------MISC STUFF-------------#
if op == "pyth":
    a = int(input("A = "))
    b = int(input("B = "))
    c = ("The hypotenuse is: ", round(sqrt((a*a)+(b*b))))
    pymsgbox.alert(text=c, title="Geometry", button="Okay")

elif op == "comp":
    x = int(input("Angle 1: "))
    c = ("The supplementary angle is: "), round(90 - x)
    if x < 90:
        pymsgbox.alert(text=c, title="Geometry", button="Okay")
    else:
        print("Your angle is equal to or higher than 90, therefore not complementary.")

elif op == "supp":
    x = int(input("Angle 1: "))
    c = ("The complementary angle is: "), round(180 - x)
    if x < 180:
        pymsgbox.alert(text=c, title="Geometry", button="Okay")
    else:
        print("Your angle is equal to or higher than 180, therefore not supplementary.")
#-------------------------------------------------------------------------------------------#
        
#-------------TRIANGLE STUFF-------------#
elif op == "tri":
    print(" ")
    print("Commands are: ")
    print("per - Perimiter of a triangle")
    print("area - Area of a triangle")
    print(" ")
    op2 = str(input("Triangle Command: "))
    
    if op2 == "per":
        a = int(input("Side A: "))
        b = int(input("Side B: "))
        c = int(input("Side C: "))
        x = "The perimiter of your triangle is: ", round(a+b+c)
        pymsgbox.alert(text=x, title="Geometry", button="Okay")

    elif op2 == "area":
        b = int(input("Base: "))
        h = int(input("Height: "))
        x = "The area of your triangle is: ", round(0.5 * (b * h))
        pymsgbox.alert(text=x, title="Geometry", button="Okay")
#--------------------------------------------------------------------#

#-------------TRAPEZOID STUFF-------------#
elif op == "trap":
    print(" ")
    print("Commands are: ")
    print("per - Perimiter of a trapezoid")
    print("area - Area of a trapezoid")
    print(" ")
    op2 = str(input("Trapezoid Command: "))
    
    if op2 == "per":
        a = int(input("Side A: "))
        b = int(input("Side B: "))
        c = int(input("Side C: "))
        d = int(input("Side D: "))
        x = "The perimiter of your trapezoid is: ", round(a+b+c+d)
        pymsgbox.alert(text=x, title="Geometry", button="Okay")

    elif op2 == "area":
        a = int(input("Side A: "))
        b = int(input("Side B: "))
        h = int(input("Height: "))
        x = "The area of your trapezoid is: ", round((0.5) * (a + b) * h)
        pymsgbox.alert(text=x, title="Geometry", button="Okay")
#----------------------------------------------------------------------#

#-------------RECTANGULAR SOLID-------------#
elif op == "rect-s":
    print(" ")
    print("Commands are: ")
    print("sa - Surface Area")
    print("vol - Volume")
    print(" ")
    op2 = str(input("Rectangle Command: "))
    
    if op2 == "sa":
        L = int(input("Length: "))
        W = int(input("Width: "))
        H = int(input("Height: "))
        x = "The surface area of your 3D rectangle is: ", round(2 * (L*W) + (H*W) + (H*L))
        pymsgbox.alert(text=x, title="Geometry", button="Okay")

    elif op2 == "vol":
        L = int(input("Length: "))
        W = int(input("Width: "))
        H = int(input("Height: "))
        x = "The volume of your 3D rectangle is: ", round(L*W*H), "cubed."
        pymsgbox.alert(text=x, title="Geometry", button="Okay")
#-----------------------------------------------------------------------#

#-------------SPHERE-------------#
elif op == "sph":
    print(" ")
    print("Commands are: ")
    print("sa - Surface Area")
    print("vol - Volume")
    print(" ")
    op2 = str(input("Sphere Command: "))
    
    if op2 == "sa":
        r = int(input("Radius: "))
        x = "The surface area of your Sphere is: ", round(4 * pi * (r * r))
        pymsgbox.alert(text=x, title="Geometry", button="Okay")

    elif op2 == "vol":
        r = int(input("Radius: "))
        x = "The volume of your Sphere is: ", round((4/3) * pi * (r * r * r)), "cubed."
        pymsgbox.alert(text=x, title="Geometry", button="Okay")
#-----------------------------------------------------------------------#

#-------------CIRCLE STUFF-------------#
elif op == "circ":
    print(" ")
    print("Commands are:")
    print("circ - Circumference")
    print("rad - Radius")
    print("area - Area")
    print("semi - Semicircle")
    print(" ")
    op2 = str(input("Circle Command: "))

    if op2 == "circ":
        r = int(input("Radius: "))
        c = "The circumference of your circle is: ", round((2*pi)*r)
        pymsgbox.alert(text=c, title="Geometry", button="Okay")

    elif op2 == "rad":
        d = int(input("Diameter: "))
        c = "The radius of your circle is: ", round(d / 2)
        pymsgbox.alert(text=c, title="Geometry", button="Okay")

    elif op2 == "area":
        r = int(input("Radius: "))
        c = "The area of your circle is: ", round(pi*(r*r)), ("Squared")
        pymsgbox.alert(text=c, title="Geometry", button="Okay")

    elif op2 == "semi":
        print(" ")
        op3 = str(input("Area (area) or Circumference (circ): "))


        if op3 == "area":
            r = int(input("Radius: "))
            c = "The area of your semicircle is: ", round(pi * (r * r)/2), "Squared"
            pymsgbox.alert(text=c, title="Geometry", button="Okay")

        elif op3 == "circ":
            r = int(input("Radius: "))
            c = "The circumference of your semicircle is: ", round((pi * r) + (2 * r))
            pymsgbox.alert(text=c, title="Geometry", button="Okay")
        else:
            print("Invalid Input")
#-----------------------------------------------------------------------------------#
else:
    print("Invalid Input")

    
#------------------ FURRO404 ------------------#
