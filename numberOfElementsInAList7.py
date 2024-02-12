list = ['a','b','c']
def count_list(list):
    if list == []:
        return 0
    return 1 + count_list(list[1:])

print(count_list(list))


