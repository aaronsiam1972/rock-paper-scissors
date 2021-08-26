from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
        else:
            print("You win!", player, "smashes", player)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose", computer, "cut", player)
        else:
            print("You Win", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "Smashes", player)
        else:
            print("You win", player, "cuts", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,2)]
