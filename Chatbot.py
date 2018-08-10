#imports the ability to get a random number (we will learn more about this later!)
from random import *

# --- Define your functions below! ---

# intro function
def intro():
    print ("\nI am Chatbot!")

# greeting
def greeting():
    print ("What is your name?")
    name = input()
    print ("Hello ",name)

# default
def default():
    print ("great.")

# process input
def process_input(response):
    if (response == "hi" or response == "Hi" or response == "HI"):
        greeting()
    else:
        default()

# give user list of options to choose the Chatbot to do
def option_list():
    print()
    print("Here is a list of things I can do.")
    print("Enter the number of what you want me to do.")
    print("1. Tell a poem")
    print("2. Play Rock-Paper-Scissors")
    print("3. Magic 8 Ball")
    print("4. Tell a joke")
    print("5. Chat with you")
    response = input()
    return response

# tell a poem
def tell_poem():
    return ("Warm, cold sharks calmly desire a cold, misty wind.\nNever desire a sun.\nAll sails pull rainy, rainy pirates.\nClear, old shores calmly lead a warm, small shark.")

# play Rock-Paper-Scissors
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
    # else:
    #     rock_paper_scissors()

# Magic 8 Ball simulator
def magic_8_ball():
    magic_8_responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes, definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
    #Asks user for a question.
    print ("What is it you wish to ask?")
    input()
    #Generates a random integer.
    aRandomIndex = randint(0, len(magic_8_responses)-1)
    #Gives user an answer.
    return (magic_8_responses[aRandomIndex])

# say a joke
def tell_joke():
    joke_list = ["Why do we tell actors to break a leg?\nBecause every play has a cast.","Yesterday I saw a guy spill all his Scrabble letters on the road.\nI asked him, 'What's the word on the street?","Did you hear about the new restaurant called Karma?\nThere's no menu: you get what you deserve."]
    #Generates a random integer.
    aRandomIndex = randint(0, len(joke_list)-1)
    return joke_list[aRandomIndex]

# chat with Chatbot
def chat():
    response_list = ["great.","cool story, bro.","tell me more about that.","yes","no"]
    #Generates a random integer.
    for index in range(2):
        print("What will you say?")
        input()
        aRandomIndex = randint(0, len(response_list)-1)
        print (response_list[aRandomIndex])
    print ("k i'm done talking. bye.")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        user_choice = option_list()
        if (user_choice == "1"):
            print (tell_poem())
        elif (user_choice == "2"):
            print (rock_paper_scissors())
        elif (user_choice == "3"):
            print (magic_8_ball())
        elif (user_choice == "4"):
            print (tell_joke())
        elif (user_choice == "5"):
            chat()
        else:
            print ("\nError: Answer not acceptable.")
            print ("Try again.")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
