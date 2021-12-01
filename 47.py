numbers = []

for i in range(3):
    entry = input("Entry : ")
    try :
         # entry = int(entry)
         # numbers.append(entry)
        numbers.append(float(entry))
    except ValueError :
        pass

print(numbers)
