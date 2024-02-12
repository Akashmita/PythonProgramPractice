# 10---Remove 3rd occurance of a from the list
# list = ['a','b','a','c','a','d']
position = 3
search_char = 'a'
count = 0

# for i in list:
#     if i == search_char:
#         count = count + 1
#         if count == position:
            # list.remove(search_char) ---removes first char

# here range is 0 to 5(6-1)
# for i in range(len(list)):
#     if list[i] == search_char:
#         count = count+1
#         # print(count)
#         if count == position:
#             # ---Important
#             del list[i]
#             break
# print(list)

# Get a list as input from user in Python---using loop
# list=[]
# n=int(input("Enter number of elements in a list: "))
# for i in range(0,n):
#     ele = int(input("Enter element: "))
#     # important
#     list.append(ele)
# print(list)

# Get a list as input from user in Python---using exception handling
# try:
#     list=[]
#     while True:
#         list.append(int(input("Enter Elements: ")))
# except:
#     # print list is any element entered other than int if entered 10 20 s then print [10,20]
#     print(list)

# Get a list as input from user in Python---using map function
# n = int(input("Enter number of elements: "))
# list = list(map(int,input("Enter elements: ").strip().split()))[:n]
# print(list)

# List of lists as input important
# n = int(input("Enter number of elements: "))
# list=[]
# for i in range(0,n):
#     list.append([input("Enter str: "),int(input("Enter int: "))])
# print(list)

# Get a list as input from user in Python Using List Comprehension and Typecasting
try:
    list=[]
    list=[int(item) for item in (input("Enter elements: ").split())]
    print(list)
except:
    list = [item for item in (input("Enter str elements: ").split())]
    print(list)

