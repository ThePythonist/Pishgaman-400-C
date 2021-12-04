info = {
    "fname":"james",
    "lname":"bond",
    "job":"mi6 agent",
    "code":"007"
}

key = input("Enter any key to search : ")

if key in info.keys():
    print(key,"Found :",info[key])
else :
    print(key,"Not Found")
