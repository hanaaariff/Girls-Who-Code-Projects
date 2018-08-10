# 1. How is the length of a list and the index of the last item related?
#    - The index of the last item is one less than the listself.
# 2. What else do you think yu can put in lists?
#    - You can put lists inside other lists.
# 3. Do you think all items must be the same data type?
#    - no
# 4. Can you put a list in the list?
#    - yes

grocery = ["bananas", "milk", 23.84, "tomato"]

# print the length of the list
print(len(grocery))

#print the elements/items in the list
for item in grocery:
    print(item)

#add a list within a list and try printing it out
pens = ["ballpoint", "gel", "fountain"]
pencils = ["wooden", "mechanical"]
stationery = [pens, pencils]

#prints out each list in stationery
for item in stationery
    print(item)

#prints out each item line by line
#no distinction between sublists
for item in stationery:
    for index in item:
        print(index)
