# Inheritance
# class A :
#     def say_hello(self):
#         print("Hello")
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# b = B()
# b.say_goodbye()
# b.say_hello()

#-------------------------------------------------
# Super()
# class Pedar :
#     def __init__(self, lname):
#         self.lastname = lname
#
#     def say_hello(self):
#         print("Hello")
#
#
# class Farzand(Pedar):
#     def __init__(self, lname):
#         super().__init__(lname)
#
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# pesar = Farzand("Ahmadi")
# print(pesar.lastname)

#-------------------------------------------------
# Without Inheritance
class Aval :
    def __init__(self, lname="Ahmadi"):
        self.lastname = lname

    def say_hello(self):
        print("Hello")


class Dovom :
    def __init__(self):
        self.pedar = Aval()
        self.age = 15

    def say_goodbye(self):
        print("Goodbye")


dovom = Dovom()
print(dovom.pedar.lastname)
print(dovom.age)
