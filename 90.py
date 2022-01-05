lines = open('words.txt').readlines()
rev = []

for line in lines :
    rev.append(line[::-1])

print(rev)
# print(lines[::-1])
