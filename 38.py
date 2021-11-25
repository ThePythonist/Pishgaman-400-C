numbers = []
for i in range(3):
    x = int(input("Enter any number : "))
    numbers.append(x)

numbers.sort()
# print(numbers[::-1])
numbers.reverse()
print(numbers)