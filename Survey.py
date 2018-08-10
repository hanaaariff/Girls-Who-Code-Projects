import json

user_list = []
question_list = [
    'What is your name?',
    'What is your age?',
    'What is your favorite movie?'
]

startover = "again"

while(startover == 'again'):
    print()
    print('Welcome to my survey!')
    survey = {}
    print()
    for int in range(len(question_list)):
        print(question_list[int])
        answer = input()
        print()
        survey[question_list[int]] = answer
    user_list.append(survey)
    print('Do you want to exit or take the survey again?')
    print('Type "exit" or "again".')
    startover = input()
    while not(startover == "exit" or startover == "again"):
        print("Sorry! Not a valid answer.")
        print('Do you want to exit or take the survey again?')
        print('Type "exit" or "again".')
        startover = input()

file = open("Survey.json","r")
olddata = json.load(file)
user_list.extend(olddata)
file.close()

file = open("Survey.json","w")
json.dump(user_list,file)
file.close()

# openusers = open("Survey.json","w")
# openusers.write(json.dumps(user_list))
# openusers.close()
#
# #file opening
# openlist = open("Survey.json","r")
# jsonusers = json.load(openlist)
# print(jsonusers)
# ageSum = 0

# for index in range(len(user_list)):
#     print(user_list[index])
