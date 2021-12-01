numbers = []

for i in range(3):
    entry = input("Entry : ")
    try :
        entry = float(entry)
        entry_str = str(entry)
        if entry_str[-2:] == ".0" :
            numbers.append(int(entry))
        else :
            numbers.append(float(entry))
    except ValueError :
        pass

print(numbers)
