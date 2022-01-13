def sign_up():
    username = input("Username : ").casefold()
    password = input("Password : ")
    open('DB-USERS.txt','a+').write(username+'\n')
    open('DB-PASSWORDS.txt','a+').write(password+'\n')
    print('User ba movafaqiat sakhte shod')


def sign_in():
    users = []
    passwords = []
    db_users = open('DB-USERS.txt')
    db_passwords = open('DB-PASSWORDS.txt')

    for user in db_users :
        # users.append(user[:-1])
        users.append(user.rstrip())

    for password in db_passwords :
        # passwords.append(password[:-1])
        passwords.append(password.rstrip())

    accounts = dict(zip(users, passwords))
    # print(accounts)
    entry = input("Username : ").casefold()

    if entry in accounts :
        password = input("Password : ")
        if password == accounts[entry] :
            print("Vorod ba movafaqiat anjam shod")
        else :
            print("Password eshtebah ast")
    else :
        print("User mojod nist")
        sign_in()


choice = int(input("1 : Sabtnam , 2 : Vorod : "))
if choice == 1 :
    sign_up()
elif choice == 2 :
    sign_in()
else :
    print("Adad entekhab shode eshtebah ast")
