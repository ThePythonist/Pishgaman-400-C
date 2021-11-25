numbers = [1,2,3,4,5]

for i in range(5):
    x = int(input("Entry : "))
    # numbers += [x]
    numbers.append(x)

print(*numbers)
