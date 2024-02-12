import copy
li1 = [1, 2, [3, 5], 4]
li2 = copy.copy(li1)
li2[2][0] = 7
print("li2 ID: ", id(li2), "Value: ", li2)
print("li2 ID: ", id(li1), "Value: ", li1) #original changed
li3 = copy.deepcopy(li1)
li3[2][0] = 8
print("li3 ID: ", id(li3), "Value: ", li3)
print("li2 ID: ", id(li1), "Value: ", li1)#original not changed

# A shallow copy constructs a new compound object
# and then (to the extent possible) inserts references into it to the objects found in the original.
# A deep copy constructs a new compound object
# and then, recursively, inserts copies into it of the objects found in the original.