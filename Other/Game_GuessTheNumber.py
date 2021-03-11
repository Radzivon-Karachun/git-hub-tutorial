import random


def play_more():
    print("Do you want more? Enter Y or N: ")
    req = input().upper()
    if req == "Y":
        get_guess()
    else:
        print("Bye, bye!")


def get_guess():
    num = random.randint(0, 5)
    gus = int(input("Please enter your number between 0 and 5: "))
    if num == gus:
        print("You win!")
        play_more()
    else:
        print("You loose..")
        play_more()


get_guess()
