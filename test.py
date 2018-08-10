print("Hello World!")
answer = input("Who inspires you? ")
print(answer, "inspires you!")

#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

#guess = input("Guess a number between 1 and 20 (inclusive): ")
#if not guess.isnumeric(): # checks if a string is only digits 0 to 9
#	print("That's not a positive whole number, try again!")
#else:
#	guess = int(guess) # converts a string to an integer

#Challenge 1
guessCount = 3
while (guessCount > 0):
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    guess = int(guess)
    if (guess == aRandomNumber):
        print("Correct!")
        break;
    else:
        if (guess < aRandomNumber):
            print("Too low!")
        else:
            print("Too high!")
        guessCount -= 1;
if (guessCount == 0):
    print("You lost!")
    #break;

#Generates a new random number
aRandomNumber = randint(1, 20)

#Challenge 2
for i in range(3):
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    guess = int(guess)
    if (guess == aRandomNumber):
        print("Correct!")
        break;
    else:
        if (guess < aRandomNumber):
            print("Too low!")
        else:
            print("Too high!")
