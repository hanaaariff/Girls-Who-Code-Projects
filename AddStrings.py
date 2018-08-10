#add two strings together and return to the user
# 1. Ask the user to enter a string
# 2. Save the string to a variable
# 3. Ask the user for another string
# 4. Save the string to another variable

##### - function start

# 5. Pass the two strings into a function
# 6. Within the function add the strings and save the result to a variable
# 7. Return the variable

##### - function end

# 8. Print the result from wherever the variable was returned to

# def subtract_strings(string1,string2):
#     if (len(string1) > len(string2))
#         if (string2 in string1)


def add_strings(string1,string2):
    sum = string1 + string2
    return sum

def ask_user():
    print ("Enter a word: ")
    response1 = input()
    print ("Enter another word: ")
    response2 = input()
    sum = add_strings(response1,response2)
    print (sum)

# --- Put your main program below! ---
def main():
    ask_user()


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
