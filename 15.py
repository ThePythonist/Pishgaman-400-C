import math

print("Ax2 + Bx + C")
#a=1 b=2 c=-3

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

delta = (b**2) - (4*a*c)

if delta < 0 :
    print("Javad nadarad")

elif delta == 0 :
    x = (-b) / (2*a)
    print(x)

else :
    x1 = (-b-(math.sqrt(delta))) / (2*a)
    x2 = (-b+(math.sqrt(delta))) / (2*a)
    print("x1 :",x1)
    print("x2 :",x2)
