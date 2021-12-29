# lines = open('words.txt').readlines()
#
# output = ""
#
# for line in lines :
#     if len(line) == 6 :
#         output += line
#
# open("5-Letter.txt","w").write(output)
# print("Done")

lines = open('words.txt').readlines()

lst = []

for line in lines :
    if len(line) == 6 :
        lst.append(line)

output = "".join(lst)

open("5-Letter.txt","w").write(output)
print("Done")
