lst = [1,2,3,4]
# rev_lst=[]
#
# for i in range(len(lst)):
#     rev_list.append(lst[(len(lst)-1)])
#     del lst[(len(lst)-1)]
# print(rev_lst)
# print(lst)
# --------------------------------------------------------------------------------
#using list comprehension
rev_lst= [lst[len(lst)-i-1] for i in range(len(lst))]
print(rev_lst)
# --------------------------------------------------------------------------------
# using slicing
# def reverse(lst):
#     new_lst=lst[::-1]
#     return new_lst
# print(reverse(lst))
# --------------------------------------------------------------------------------
# lst.reverse()
# print(lst)