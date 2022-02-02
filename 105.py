class Calculator :
    def __init__(self, n1, op, n2):
        self.num1 = n1
        self.num2 = n2
        self.operator = op

    def add(self):
        return self.num1 + self.num2

    def substract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


calc = Calculator(
    float(input("Number 1 : ")),
    input("Operator : "),
    float(input("Number 1 : ")),
)

if calc.operator == "+":
    print(calc.add())
elif calc.operator == "-":
    print(calc.substract())
elif calc.operator == "*":
    print(calc.multiply())
elif calc.operator == "/":
    print(calc.divide())
else :
    print("Invalid Input")
