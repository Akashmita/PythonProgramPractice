# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))

# String-sorted based on ASCII translations
x = "python"
print(sorted(x))

# Dictionary
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
print(sorted(x))

# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))

################################
L = ['aaaa', 'bbb', 'cc', 'd']

# sorted without key parameter
print(sorted(L))
print()

# sorted with key parameter
print(sorted(L, key=len))

# sorted()	sort()
# 1.	The sorted() function returns a sorted list of the specific iterable object.	The sort() method sorts the list.
# 2.	We can specify ascending or descending order while using the sorted() function	It sorts the list in ascending order by default.
# 3.	
# Its syntax is :
# 
# sorted(iterable, key=key, reverse=reverse)
# 
# Its syntax is -:
# 
# list.sort(reverse=True|False, key=myFunc)
# 
# 4.	Its return type is a sorted list.	We can also use it for sorting a list in descending order.
# 5.	It can only sort a list that contains only one type of value.	It sorts the list in-place.