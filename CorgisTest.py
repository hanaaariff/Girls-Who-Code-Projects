import school_scores
list_of_scores = school_scores.get_all()

# print out the first element in the data set
print(list_of_scores[0])

# print out the state name and year for each row in the data set
for index in range(len(list_of_scores)):
    print(list_of_scores[index]['State']['Name'],list_of_scores[index]['Year'])

for row in list_of_scores:
    print(row['State']['Name'],row['Year'])

for row in list_of_scores:
    print(row['Total']['Test-takers'])
