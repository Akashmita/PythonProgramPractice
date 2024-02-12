import re
def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(regex.search(string) == None):
        print("String accepted")
    else:
        pint("String not accepted")

#Driver code
if __name__ == '__main__':
    string = "Geeks$For$Geeks"
    run(string)

# input string
n = "Geeks$For$Geeks"
n.split()
c = 0
s = '[@_!#$%^&*()<>?/\|}{~:]'  # special character set
for i in range(len(n)):
    # checking if any special character is present in given string or not
    if n[i] in s:
        c += 1  # if special character found then add 1 to the c

# if c value is greater than 0 then print no
# means special character is found in string
if c:
    print("string is not accepted")
else:
    print("string accepted")

# this code is contributed by gangarajula laxmi


def has_special_char(s):
    for c in s:
        if not (c.isalpha() or c.isdigit() or c == ' '):
            return True
    return False


# Test the function
s = "Hello World"
if has_special_char(s):
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")

s = "Hello@World"
if has_special_char(s):
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")
# This code is contributed by Edula Vinay Kumar Reddy


import string


def check_string(s):
    for c in s:
        if c in string.punctuation:
            print("String is not accepted")
            return
    print("String is accepted")


# Example usage
check_string("Geeks$For$Geeks")  # Output: String is not accepted
check_string("Geeks For Geeks")  # Output: String is accepted


def check_special_char_ascii(string):
    for char in string:
        if ord(char) < 48 or (57 < ord(char) < 65) or (90 < ord(char) < 97) or ord(char) > 122:
            return "String is not accepted."
    return "String is accepted."


# Example Usage
string = "Geeks$For$Geeks"
print(check_special_char_ascii(string))