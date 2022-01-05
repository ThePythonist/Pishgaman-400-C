lines = open('words.txt','r').readlines()
lst = []

for line in lines :
    if line[-4:-1] == "ing" :
        lst.append(line[:-1])

print(lst)
