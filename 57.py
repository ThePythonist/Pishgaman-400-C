string = "Python"
d = {}
# for i in range(len(string)):
#     d.setdefault(string[i],i)
# print(d)

slices = [ i for i in range(len(string)) ]
print(dict(zip(string,slices)))
