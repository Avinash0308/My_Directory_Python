import random
#snake water gun
#gun beats snake
#water beats gun
#snake beats water
#use if else
def won():
    print("Hurray! You won the Game")
def lost():
    print("Nah! You lost the Game, Better luck next time")
opt = ["Snake","Water","Gun"]
while True:
    user = input("Please choose your item: ")
    rand = random.randint(0,2)
    comp = opt[rand]
    print(f"Computer Opted: {comp}")
    if comp == user:
        print("Go Again, you both opted the same!")
    elif user == "Snake":
        if comp == "Water":
            won()
        else:
            lost()
        break
    elif user == "Water":
        if comp == "Snake":
            lost()
        else:
            won()
        break
    else:
        if comp == "Snake":
            won()
        else:
            lost()
        break