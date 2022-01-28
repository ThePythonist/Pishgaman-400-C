import random


def generate():
    pw = ""
    for i in range(6):
        pw += str(random.choice(range(0,10)))

    return pw


password = generate()

print("Password :", password)
