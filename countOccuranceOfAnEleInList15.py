# 15--count occurance of an element in a list
# using count function
# list = list(input("Enter elements: ").split())
# print(list.count(10))

# using looping
# list = list(map(int,input("Enter elements: ").split()))
# ele=10
# count=0
# print(len(list))
# for i in range(len(list)):
#     if list[i] == ele:
#         count = count+1
# print("Occurances is :",count)

# using counter
# from collections import Counter
# list = list(map(int,input("Enter elements: ").split()))
# print(Counter(list))

# using count of
# import operator as op
# list = list(map(int,input("Enter elements: ").split()))
# print(list)
# search_ele = 10
# print(op.countOf(list,search_ele))

# using dictionary comprehension
# list=[10,20,30,45,20]
# ele=20
# count_ele= {i: list.count(i) for i in list}
# print(count_ele)
# print(count_ele.get(ele))

# using pandas
# import pandas as pd
# list=[10,20,30,10]
# count = pd.Series(list).value_counts()
# print(count)

# 
