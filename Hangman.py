# 1. Determine a word.
# 2. Show the player how many letters the word has.
# 3. Ask the player to guess a letter.
#    a. If the letter is in the word, show the word with the letter filled in.
#    b. If the letter is not in the word, tell the player they are wrong and display how many guessCount they have left.
# 4. If the player runs out of guessCount before guessing the word, tell them they lost.
# 5. If the player guessCount the word before running out of guessCount tell them they won.
# 6. Ask the user if they want to play again.
#    a. If the user says yes, restart the game.
#    b. If the user says no, thank them for playing.

################################################################################

# hangman_wordbank = ["ghost","mission","independent","pirates","satellite","maneuver","groovy","yield","furniture"]
#
# #imports the ability to get a random number (we will learn more about this later!)
# from random import *
#
# #Generates a random integer.
# aRandomIndex = randint(0, len(hangman_wordbank)-1)
#
# word = hangman_wordbank[aRandomIndex]

################################################################################

# guessCount = 7
#
# word = input("Player 1: Enter a word.\n")
# word = word.lower()
#
# userWord = word
# for index in range(len(word)):
#     userWord[index] == "_"
#
# #ensures Player 2 can't see the word
# for num in range(50):
#     print("\n")
#
# while (guessCount > 0):
#     print("Player 2: Guess a letter!")
#     print(userWord)
#     letter = input()
#
#     for index in word:
#         if (letter == word[index]):
#             userWord[index].remove()
#             userWord[index].add(letter)
#
#     guessCount -= guessCount

################################################################################

word = input("Player 1: Type a word for someone to guess: ")
#ensures Player 2 can't see the word
for num in range(50):
    print("\n")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if (word.isalpha() == False):
	print("That's not a word!")

# Some useful variables
guessCount = 7
correct = 0

userDisplay = ["_"] * len(word)

while (guessCount > 0):

	print (userDisplay)

	if (len(word) == correct):
		print ("You guessed the word!")
		break

	letterRightWrong = 0

	guess = input("Player 2: Guess a letter: ")

	for index in range(len(word)):
		if (guess == word[index]):
			userDisplay[index] = guess
			correct += 1
			letterRightWrong += 1

	if (letterRightWrong > 0):
		print ("Correct!")
	else:
		print("Wrong!")
		guessCount -= 1

	print ("You have ",guessCount," guesses left!")

if (guessCount == 0):
	print ("You lost!")
