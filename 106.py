class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return (self.length+self.width)*2


l,w = int(input("length : ")),int(input("width : "))

newRectangle = Rectangle(l,w)
print("rectangle area :",newRectangle.area())
print("rectangle perimeter :",newRectangle.perimeter())
