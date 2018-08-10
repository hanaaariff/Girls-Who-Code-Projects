import json
from pprint import pprint

file = open("Survey.json","r")
data = json.load(file)
print(type(data))
print(data)
file.close()

ages = []
for a in range(len(data)):
    if data[a]["What is your age?"] is not '':
        ages.append(int(data[a]["What is your age?"]))
print(ages)
total = sum(ages)
average = total/len(ages)
print(average)
