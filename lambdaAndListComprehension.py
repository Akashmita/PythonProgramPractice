# list from range 0 to 10
# list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_)
#
# # lambda function
# lambda_list = list(map(lambda x: x * 2, list_)) #returns value in tuple (lambda x: x * 2, list_)
# print(lambda_list)
# print(type(lambda_list))

# Map basically iterates every element
# in the list_ and returns the lambda
# function result
# print(lambda_list)
#
# # list comprehension
# list_comp = [x * 2 for x in list_]
# print(list_comp)
#
# #dictionary comprehension
# myDict = {x: x*2 for x in [1,2,3,4,5]}
# print (myDict)

#tuple comprehension
print(i for i in (1,2,3))