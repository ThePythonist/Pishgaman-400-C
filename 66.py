def myfunc(x,y):
    numbers = range(x,y)
    print(*numbers)

myfunc(int(input("X : ")),int(input("Y : ")))
