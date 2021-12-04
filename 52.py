nomarat = {
    "riazi1":15,
    "farsi_omomi":20,
    "mabani_computer":19,
    "madar_electrici": 9,
    "fizik1":16,
    "difransiel":12
}

for k,v in nomarat.items():
    if v >= 10 :
        print(k,": Passed")
    else :
        print(k,": Failed")

# lst = [ i for i in nomarat.values()]
# moadel = sum(lst) / len(lst)
# print(moadel)

moadel = sum(nomarat.values()) / len(nomarat.values())
print("Moadel :",moadel)
