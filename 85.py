lines = open('words.txt','r').readlines()
lst = []

for line in lines :
    if line[:3] == "sub" :
        lst.append(line[:-1])

print(lst)
