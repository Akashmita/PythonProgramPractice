import re


def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))


def Find(string):
    x = string.split()
    res = []
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
            res.append(i)
    return res


# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))


def Find(string):
    x = string.split()
    res = []
    for i in x:
        if i.find("https:") == 0 or i.find("http:") == 0:
            res.append(i)
    return res


# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))