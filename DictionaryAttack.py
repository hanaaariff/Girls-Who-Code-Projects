#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
user_password = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:

# convert f to a list
dictionary = []
for word in f:
    dictionary.append(word)

# variable to check if a word has been found in the dictionary
word_match = False

# itera
for item in dictionary:
    if(user_password == item.strip()):
        word_match = True
    # checks if 2018 is in the end of user_password
    if(user_password[len(user_password)-4:len(user_password)] == "2018"):
        word_match = True

if(word_match == True):
    print("Your password is very weak.")
else:
    print("Your password is strong.")
