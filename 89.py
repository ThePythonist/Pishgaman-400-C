# lines = open('words.txt').readlines()
# lst = []
#
# for line in lines :
#     lst.append(line[:-1])
#
# output = "".join(lst)
# print(output)

lines = open('words.txt').read().replace("\n", "")
lst = []

for line in lines :
    lst.append(line)

output = "".join(lst)
print(output)
