str_check = "I love automation testing"
str_sub = "love"

#using if-else and in
# if "SDET" in str_check:
#     print("Yes")
# else:
#     print("No")

#using find
# print(str_check.find(str_sub))
# if (str_check.find(str_sub) == -1): #if element not founf find() return -1 otherwise index
#     print("No")
# else:
#     print("Yes")

#using index()
# print(str_check.index(str_sub)) #first occurance index or ValueError: substring not found

# using count method
# if str_check.count(str_sub)>0:
#     print("Yes")
# else:
#     print("No")

#list comprehension
# print("yes" if str_sub in str_check else "No")

#using lambda function
# x=list(filter(lambda x: (str_sub in str_check),str_check.split()))
# print("yes" if x else "no")---yes
# print(["yes" if x else "no"]) #['yes']

#Python program to check if a substring is present in a given string
import re

MyString1 = "A geek in need is a geek indeed"

if re.search("need", MyString1):
    print("Yes! it is present in the string")
else:
    print("No! it is not present")
