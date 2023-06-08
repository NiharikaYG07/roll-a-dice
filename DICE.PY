import random;
number=random.randint(1,6)

def rollDice(response):
    if response=="y":
        number=random.randint(1,6)
        if number==1:
            print("[---]")
            print("[-0-]")
            print("[---]")
        elif number==2:
            print("[---]")
            print("[0-0]")
            print("[---]")
        elif number==3:
            print("[---]")
            print("[000]")
            print("[---]")
        elif number==4:
            print("[0-0]")
            print("[---]")
            print("[0-0]")
        elif number==5:
            print("[0-0]")
            print("[-0-]")
            print("[0-0]")
        elif number==6:
            print("[0-0]")
            print("[0-0]")
            print("[0-0]")
        option=input("Enter y to roll a dice and n to exit: ")
        rollDice(option)
    if response=="n":
        print("Thanks for playing")

option=input("Enter y to roll a dice and n to exit: ")
rollDice(option)