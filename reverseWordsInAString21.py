# str= (input("Enter string: ")).split()
# print(str)
# s = str[::-1]
# print(s)


str = "a bc d"
# s = str.split()[::-1]
# print(s)
# l = []
# for i in s:
#     l.append(i)
# # print(l)
# print(" ".join(l))

# print(str.split())
# x = str.split()
# print(type(x))
# # rev = x.reverse() #not working
# # print("test",rev)
# rev = " ".join(reversed(str.split()))
# print(rev)


# initializing string
string = "geeks quiz practice code"

# creating an empty stack
stack = []

# pushing words onto the stack
for word in string.split():
    stack.append(word)

# creating an empty list to store the reversed words
reversed_words = []

# popping words off the stack and appending them to the list
while stack:
    reversed_words.append(stack.pop())

# joining the reversed words with a space
reversed_string = " ".join(reversed_words)

# printing the reversed string
print(reversed_string)

# This code is contributed by Edula Vinay Kumar Reddy

