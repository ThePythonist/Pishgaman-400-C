# import math
#
# def greetings(name):
#     return "Hello " + name
#
# #Aliasing
# greet = greetings
# print(greet("Sorena"))
#
# output = print
# output("Hello World")
#
# jazr = math.sqrt
# print(jazr(100))

def func(name):
    return "Hello " + name

def call_func(function):
    return function("Sorena")

print(call_func(func))

# def func(name):
#     print("Hello " + name)
#
# def call_func(taabe):
#     taabe("Sorena")
#
# call_func(func)
