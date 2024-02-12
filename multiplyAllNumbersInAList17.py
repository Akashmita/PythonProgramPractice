n = int(input("Number of ele in a list: "))
list = list(map(int,input("Enter ele of the list: ").strip().split()))[:n]
res = 1
#
# for i in list:
#     res = res * i
# print(res)

def mul(n):
    if n<1:
        return none
    elif n==1:
        return list[0]
    else:
        return list[n-1] * mul(n-1)
print(mul(n))

