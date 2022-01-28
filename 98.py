import random

number = random.randint(0,10)
chance = 0

while chance < 5 :
    print("-------You have used",chance,"of your 5 chances-------")
    guess = int(input("Your guess : "))

    if guess == number :
        print("You won !")
        break

    elif guess > number :
        print("Try lower than",guess)

    else :
        print("Try higher than",guess)

    chance += 1

if not chance < 5 :
    print("You lose! The number was :", number)
