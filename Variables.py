#Global and Local variables

x = 10 #Global

def f(x):
    x = 20 #Local
    print(x) #Output will be local x

f(x) #Using Global x
