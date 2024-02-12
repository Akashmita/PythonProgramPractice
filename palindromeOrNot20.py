str= input("Enter string: ")
# str_rev = str_input[::-1]

# if str == str_rev:
#     print("Palindrome")
# else:
#     print("Not")

# using for loop
# for i in range(0,int(len(str)/2)):
#     if str[i] != str[len(str)-i-1]:
#         print("False")
#         break
# else:
#     print("True")

#using join
# rev = "".join(reversed(str))
# if str == rev:
#     print("Yes")
# else:
#     print("No")

#using one extra variable
# x = "malayalam"
#
# w = ""
# for i in x:
#     w = i + w
#
# if (x == w):
#     print("Yes")
# else:
#     print("No")

#using a flag
# st = 'malayalam'
# j = -1
# flag = 0
# for i in st:
#     if i != st[j]:
#         flag = 1
#         break
#     j = j - 1
# if flag == 1:
#     print("NO")
# else:
#     print("Yes")

#using recursion
def isPalindrome(s):
    # to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)

    # if length is less than 2
    if l < 2:
        return True

    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:

        # Call is palindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])

    else:
        return False


# Driver Code
s = "MalaYaLam"
ans = isPalindrome(s)

if ans:
    print("Yes")

else:
    print("No")

