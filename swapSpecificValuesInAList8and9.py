first_ele = int(input("Enter 1st ele position: "))
second_ele = int(input("Enter 2nd ele position: "))
#
list = list(input("Enter elements: ").strip().split())
# temp = list[first_ele]
# list[first_ele] = list[second_ele]
# list[second_ele] = temp
#
# print(list[first_ele])
# print(list[second_ele])

list[first_ele], list[second_ele] =  list[second_ele],list[first_ele]

print(list)
