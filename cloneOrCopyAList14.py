list1=list(input("Enter elements of first list: ").strip().split())[:2]
list2=list(input("Enter elements of second list: ").strip().split())[:3]
list3 = []
# list3.append(list2)
# # list3.extend(list2)
# print(list3)

# Python program to copy or clone a list
# Using the Slice Operator
# list3 = list2[:]
# print(list3)

# using list copy
# list3=list2
# print(list3)

# using list comprehension
# list3 = [i for i in list2]
# print(list3)

# using copy
import copy
# list3 = copy.copy(list2)
list3 = copy.deepcopy(list2)
print(list3)