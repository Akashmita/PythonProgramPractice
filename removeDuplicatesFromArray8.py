str = input("Enter a string: ")
res=''
count=0
for i in range(len(str)):
    for j in range(len(str)):
        if str[i] == str[j]:
            count = count+1
            if count >1:
                continue

    print(str)