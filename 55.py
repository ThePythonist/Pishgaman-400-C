info = {'max': 24, 'james': 23, 'steve': 16, 'nick': 19}

# names = []
# ages = []
#
# for k,v in info.items():
#     names.append(k)
#     ages.append(v)

names = [ i for i in info.keys() ]
ages = [ i for i in info.values() ]

print(names)
print(ages)
