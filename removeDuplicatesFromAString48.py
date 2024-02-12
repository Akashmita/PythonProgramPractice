# using set and concatenation
#input a string
#take a blank list/set to append/add unique charecters from the input string
#take a blank output string which will show result with unique characters
#
# def unique_value(str):
#     # unique_char = set()
#     unique_char = []
#     output = ""
#     for char in str:
#         if char not in unique_char:
#             # unique_char.add(char) #In set same as append in list
#             unique_char.append(char)
#             output = output + char
#     return output
#
# input_str = input("Enter a string: ")
# print(unique_value(input_str))

# using a list and join
def remove_duplicates(str):
    unique_chars = []
    for char in str:
        if char not in unique_chars:
            unique_chars.append(char)
    return "".join(unique_chars)

input_str = input("Enter a string: ")
print(remove_duplicates(input_str))






