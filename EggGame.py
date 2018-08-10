#imports the ability to get a random number (we will learn more about this later!)
from random import *

# --- Define your functions below! ---

userName = ""

def intro():
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
        print("5. You lose the game if you lose a match of Rock-Paper-Scissors 3 times in a row as an egg.\n")

        print("Enter 'Start Game' when you are ready to play.")
        response = input()

        while not (response.lower() == "start game"):
            print("Sorry! That is not an acceptable answer.")
            print("Enter 'Start Game' when you are ready to play.")
            response = input()
            print()

        if (response.lower() == "start game"):
            #start game

    elif (choice.lower() == "start game"):
        #start game
