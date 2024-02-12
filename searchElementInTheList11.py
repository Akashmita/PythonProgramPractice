def search_item(list,item):
    for i in list:
        if i == item:
            return True
    return False

list=[1,2,3]
item=4

# print(search_item(list,item))

if search_item(list,item):
    print("Product is available....")
else:
    print("Product is not available...")


