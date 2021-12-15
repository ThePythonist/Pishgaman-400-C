def calculator(n1,n2,op):
    def add():
        print(n1+n2)

    def subtract():
        print(n1-n2)

    def multiply():
        print(n1*n2)

    def divide():
        print(n1/n2)

    if op == "+" :
        add()
    elif op == "-" :
        subtract()
    elif op == "*" :
        multiply()
    elif op == "/" :
        divide()
    else :
        print("That's not a valid operator! Try again")
        calculator(
            float(input("Number 1 : ")),
            float(input("Number 2 : ")),
            input("Operator : ")
        )

calculator(
    float(input("Number 1 : ")),
    float(input("Number 2 : ")),
    input("Operator : ")
)
