lines = open('words.txt','r').readlines()
lst = []

for line in lines :
    lst.append(line[:-1])

print(len(lst[:100]))
