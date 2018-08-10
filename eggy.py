from random import *

# play Rock-Paper-Scissors
egg = '''
   ____
  /    \
 /      \
|        |
|        |
|        |
 \______/
'''

chicken = '''
       /\ /\
      / |/ |/|
     |_______|
    /         \
   |  o        |
  _|           |
 /__\          |
     \          \
'''
dinosaur = '''
   ________________
 _|                |_
|    []              |
|                    |
|                    |
|           _________|
|          |________
|          _________|
|         |
'''
win_game = '''
                        ________________
                      _|                |_
                     |    []              |
                     |                    |
                     |                    |
                     |           _________|
                     |          |________
                     |          _________|
  _                _|         |
 | |             _|           |____                 ___
 | |_         __|               _  |        \   /  |   |  |   |   |
 |   |_     _|                 | |_|         \ /   |   |  |   |   |
 |      |__|                   |              |    |   |  |   |   |
 |_                            |              |    |___|  |___|   |
   |_                          |                    _____ _       |
     |__                      _|         |    |   |   |   |\  |   |
        |                   _|           |    |   |   |   | \ |
        |_                _|              \__/\__/  __|__ |  \|   O
          |      ____    |
          |    _|    |_  |
          |  _|        | |
          | |__        | |__
          |____|       |____|
'''
lose_game = '''

   ____             ___
  /   |\     \   / |   | |   |
 /   /| \     \ /  |   | |   |           ___   ____   ____
|   /\_  |     |   |   | |   |    |     |   | |      |
| _/   | |     |   |___| |___|    |     |   | |____  |____
|        |                        |     |   |      | |
 \______/                         |____ |___|  ____| |____   o o o
'''


userName = ""

def intro():
    print()
    userName = input("Enter username: ")
    print("Hello ", userName, "! Welcome to Egg-Chicken-Dinosaur!")
    print()
    choice = input("Enter 'Read Rules' or 'Start Game'.\n")
    print()

    while not (choice.lower() == "read rules" or choice.lower() == "start game"):
        print("Sorry! That is not an acceptable answer.")
        choice = input("Enter 'Read Rules' or 'Start Game'.\n")
        print()

    if (choice.lower() == "read rules"):
        print("Rules:")
        print()
        print("1. Throughout the game, you can be an egg, chicken, or dinosaur.")
        print("   A chicken is a higher position than an egg. A dinosaur is a higher position than an egg.\n")
        print("2. You will start the game as an egg.\n")
        print("3. To level up, you must win a match of Rock-Paper-Scissors against your opponent.\n")
        print("4. To win the game, you have to reach the dinosaur status.\n")

        print("Enter 'Start Game' when you are ready to play.")
        response = input()

        while not (response.lower() == "start game"):
            print("Sorry! That is not an acceptable answer.")
            print("Enter 'Start Game' when you are ready to play.")
            response = input()
            print()

        if (response.lower() == "start game"):
            egg()

    elif (choice.lower() == "start game"):
            egg()

def rock_paper_scissors():
    rps_options = ["rock","paper","scissors"]

    #Generates a random integer.
    aRandomIndex = randint(0, len(rps_options)-1)
    cp_play = rps_options[aRandomIndex]
    print ("Enter 'rock', 'paper', or 'scissors'.")
    user_play = input()
    while not (user_play == "rock" or user_play == "paper" or user_play == "scissors"):
        print ("Enter 'rock', 'paper', or 'scissors'.")
        user_play = input()

    print (cp_play)
    if (cp_play == user_play):
        return ("It's a tie!")
    elif (cp_play == "rock" and user_play == "scissors"):
        return ("You lose!")
    elif (cp_play == "rock" and user_play == "paper"):
        return ("You win!")
    elif (cp_play == "paper" and user_play == "rock"):
        return ("You lose!")
    elif (cp_play == "paper" and user_play == "scissors"):
        return ("You win!")
    elif (cp_play == "scissors" and user_play == "rock"):
        return ("You win!")
    elif (cp_play == "scissors" and user_play == "paper"):
        return ("You lose!")

def egg():
    output = rock_paper_scissors()
    if (output=="You lose!"):
        print("Try again egg!")
        rank="Egg"
        egg()
    elif (output=="You win!"):
        print("Awesome you are now a chicken!")
        rank="Chicken"
        chicken()
    else:
        rank="Egg"
        egg()

def chicken():
    output = rock_paper_scissors()
    if (output=="You lose!"):
        print("You have dishonored your name, you are an egg now!")
        rank="Egg"
        egg()
    elif (output=="You win!"):
        print("Siiiiick you are now a Dino!")
        rank="Dino"
        dino()

    else:
        chicken()
        rank="Chicken"

def dino():
    output = rock_paper_scissors()
    if (output =="You lose!"):
        print("So close you are now chicken, try again!")
        rank="Chicken"
        chicken()
    elif (output =="You win!"):
        print("Congrats you win")
        rank="Dino Master Extreme"
        intro()
    else:
        dino()
        rank="Dino"


def main():
    intro()

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
