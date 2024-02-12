# nterms = int(input("how many terms? "))
# n1,n2 = 0,1
# count =0
#
# if nterms<=0:
#     print("Please enter a positive number: ")
# elif nterms==1:
#     print(f"Fibonacci number upto {nterms} is: ")
#     print(n1)
# else:
#     print("Fibonacci sequence: ")
#     while count <nterms:
#         print(n1)
#         nth = n1+n2
#         n1=n2
#         n2=nth
#         count = count+1

# using for loop
# nterms = int(input("how many terms? "))
# n1,n2 = 0,1
# count =0
#
# if nterms<=0:
#     print("Please enter a positive number: ")
# elif nterms==1:
#     print(f"Fibonacci number upto {nterms} is: ")
#     print(n1)
# else:
#     for i in range(0,nterms):
#         print(n1)
#         new_n2=n1+n2
#         n1=n2
#         n2=new_n2

# using function
# def fibonacci(nterms):
#     # n1, n2 = 0, 1
#     fibo_sequence=[]
#     # count = 0
#
#     if nterms <= 0:
#         print("Please enter a positive number: ")
#     elif nterms == 1:
#         print(f"Fibonacci number upto {nterms} is: ")
#         print(fibo_sequence[0])
#     else:
#         fibo_sequence = [0,1]
#         for i in range(1, nterms):
#             # new_n2 = fibo[i] + fibo[i+1]
#             # fibo[i] = fibo[i+1]
#             # fibo[i+1] = new_n2
#             fibo_sequence.append(fibo_sequence[i-1]+fibo_sequence[i])
#         return fibo_sequence
#
# nterms = int(input("how many terms? "))
# print(fibonacci(nterms))

# using recursive function
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2)

def fibonaccisequence(n):
    sequence=[]
    for i in range(0,n):
        sequence.append(fibonacci(i))
    return sequence

print(fibonaccisequence(4))