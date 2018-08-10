az = ["donkey","apple","Air","zebra","Heir","heir"]

nums = [5, 42, 73, 1000000, 163478, 3.4,]

az_nums = ["donkey",5,"apple",42,"Air",73,"zebra",1000000,"Heir",163478,"heir",3.4]

print()

#az

#1
print (sorted(az)) #prints in alphabetical order, capital letters are higher priority
print()

#2
print (sorted(az, reverse=True)) #prints the reverse of #1
print()

#3
print (sorted(az, key=len)) #sorts from smallest word to biggest word, in terms of length
print()

#4
#We thought this would sort the list by giving priority to words starting with
#lowercase letters, but it doesn't work.
print (sorted(az, key=str.lower))
print()

#5
#nums
print (sorted(nums)) #sorts from smallest value to biggest value
print()

#6
#az_nums
#only works with python, not python3
az_nums.sort() #sorts numbers first, then strings
print (az_nums)
print()
