# list = ["a",1,2.5]
# print(list)
# print(list*2)
# print(list+list)

# lan = ["c","c++","java","python"]
# exp = [0.5,0,0.5,5]
#
# test = tuple(zip(lan,exp))
# print(test)


# name="test"
# change_name=int(name)
# print(change_name)

# num={1,2}
# test=frozenset(num)
# print(test)
# 
# print("test:  ",end="")
# print(10)
#-------------------------------------------------------
# for i in range(1,5):
#     for j in range(5,i,-1):
#         print(end=" ")
#     for k in range(0,i): #observe in below example
#             print("*",end="")
#     print("\r")
#-------------------------------------------------------
# num=65
# for i in range(1,5):
#     for j in range(1,i+1):
#         ch = chr(num)
#         print(ch,end="")
#         num= num+1
#     print("\r")
#-------------------------------------------------------
# count = 1
# while (count<11):
#     print("num: ",count)
#     count += 1
#-------------------------------------------------------
# class Student:
#     def __init__(self):
#         print("Welcome")
#     def __del__(self):
#         print("Destructor")
# obj= Student()
# del obj
#-------------------------------------------------------

# class Bird:
#     no_eyes = 2
#
#     def can_do(self,can_sing):
#         fly=True
#         self.sing = can_sing
#         self.num_wings =2
#         print(f"{fly} and {self.sing} and {self.num_wings}")
#
# bird1=Bird()
# bird1.can_do(False)

#-------------------------------------------------------

# class A:
#     def __init__(self):
#         self.__t2 = 345
#     def __private_method(self):
#         self.phone = 123
#         self.__add = "xyz"
#         return self.__add
#     def pub_method(self):
#         self.__t1 = 345
#         return self.__test
#
# a1=A()
# # print(a1._A__private_method()) ---O/P xyz
# # print(a1._A__add) ---Error
# # print(a1.pub_method())---345
# # print(a1._A__t1)---Error
# print(a1._A__t2)---345
#-------------------------------------------------------

#
# a= 10
# b = 10
# x,y=4,5
#
# print(id(a))
# print(id(b))
#
# print(id(x))
# print(id(y))
# -------------------------------------------------------
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
#
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
# print(fruit_list1)
#
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
#
# print (sum)

# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
# -------------------------------------------------------
#
#
#
#
#
#
