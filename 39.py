length = int(input("Tedad vorodi ra vared konid : " ))
numbers = []

for i in range(length):
    print("Vorodi",i+1,"ra vared konid : ")
    numbers.append(int(input()))

print("Maximum :",max(numbers))
