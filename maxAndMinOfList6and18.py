n = int(input("enter number of elements: "))
list = list(map(int,input("Enter elements: ").strip().split()))[:n]
print(list)
# print(max(list))
# print(min(list))

# max = list[0]
# for i in list:
#     if i > max:
#         max = i
# print(max)

# min = list[0]
# for i in range(1,len(list)):
#     if list[i] < min:
#         min = list[i]
# print(min)

def min_ele(list,n):
    if n==1:
        return list[0]
    else:
        return min(list[n-1],min_ele(list,n-1))

print(min_ele(list,n))
