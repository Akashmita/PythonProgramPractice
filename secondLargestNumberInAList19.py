# list = list(input("Enter list elements: ").split())
list = list(map(int,input("Enter list elements: ").split()))[:4]
count=0
for i in range(len(list)):
    if count<1:
        list.remove(max(list))
        count = count+1
print("Second max in the list is: ", max(list))

# Python program to find largest number
# in a list

# List of numbers
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]

# Removing duplicates from the list
list2 = list(set(list1))

# Sorting the  list
list2.sort()

# Printing the second last element
print("Second largest element is:", list2[-2])

# Python program to find second largest number
# in a list

# List of numbers
list1 = [10, 20, 4, 45, 99]

# new_list is a set of list1
new_list = set(list1)

# Removing the largest element from temp list
new_list.remove(max(new_list))

# Elements in original list are not changed
# print(list1)
print(max(new_list))

# Python program to find second largest
# number in a list

# creating list of integer type
list1 = [10, 20, 4, 45, 99]

'''
# sort the list    
list1.sort()

# print second maximum element
print("Second largest element is:", list1[-2])

'''

# print second maximum element using sorted() method
print("Second largest element is:", sorted(list1)[-2])




