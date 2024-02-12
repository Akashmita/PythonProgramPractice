#multiply 1 to num

# num=int(input("Enter number: "))
#res= 1

# for i in range(1,num+1):
#     res=res*i
# print(res)

def factorial(n):
    if n>1:
        return n * factorial(n-1)
    elif n==1:
        return 1
    else:
        return "factorail is undefined"

print(factorial(6))

