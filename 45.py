number = int(input("Enter any number : "))
divisors = [ i for i in range(1,number+1) if number % i == 0 ]

print(divisors)

prime_status = False
if len(divisors) == 2 :
    prime_status = True

print("Prime :",prime_status)
