def is_prime(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return "True" if len(divisors) == 2 else "False"
print(is_prime(int(input("Enter any number to check : "))))
