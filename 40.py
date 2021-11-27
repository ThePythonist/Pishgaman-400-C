lst1 = [16,11,13,15,2,4,10]
lst2 = [11,2,7,8,4]
lst3 = list()

for i in lst1 :
    if i in lst2 :
        lst3.append(i)

print(lst3)
