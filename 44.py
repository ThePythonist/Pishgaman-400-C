number = int(input("Enter any number : "))
# divisors = []
# for i in range(1,number+1):
#     if number % i == 0 :
#         divisors.append(i)
divisors = [ i for i in range(1,number+1) if number % i == 0 ]
print(divisors)
