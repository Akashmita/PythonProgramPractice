n= int(input("Enter number of elements: "))
list= list(map(int,input("Enter elements").strip().split()))[:n]
print(list)

# using for loop
# sum = 0
#
# for i in list:
#     sum = sum + i
# print(sum)

#using while loop
# sum = 0
# i=0
# while i<(len(list)):
#     sum = sum + list[i]
#     i=i+1
# print(sum)

# using recursive way
# def sum(list,size):
#     if size<=1:
#         return 0
#     else:
#         return list[size-1] + sum(list,size-1)
#
# total = sum(list1,len(list1))
# print(total)

# using sum function in list
print(sum(list))


# using list comprehension
# s = [i for i in list]
# print(sum(s))


