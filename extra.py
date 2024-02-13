# name = "So My name is Joker"

# print(name[0:-1:1])

# print(name[0::2])

# print(name[0:-1:3])

# print(name[2:-3:4])

# print(name[3:-2:3])

# print(name[3:-2:5])


# write a program which accepts a string and display first two characters of each string in a separate line
# stre = input("Enter string: ")

# print(stre[:2])
# count = 0

# for i in stre:
#     if i == ' ':
#         print(stre[count+1:count+3])
#     count += 1


# Write a Python program to iterate over dictionaries using for loops.
# d = {'Red': 1, 'Green': 2, 'Blue': 3}
# SAMPLE OUTPUT:
# Red corresponds to  1
# Green corresponds to  2
# Blue corresponds to  3

# d = {'Red': 1, 'Green': 2, 'Blue': 3}

# l1 = list(d)
# for key in l1:
#     print(key)



# S = "Hello CS F20"
# print(S[::-3])


# str1 = "Hello"
# str2 = "Pakistan"

# print(str1+""+str2)


# X  = "kamran.malik@pucit.edu.pk"

# print(X[-12:-6:1])


# x = 5
# x + 1

# print(x)


# age = input("Enter your age: ")
# # print(age + age + age)
# print(age * 3)

# print(0 or False)

# num = input("Enter Number: ")

# count = 0 

# while count < len(num):
#     count += 1
# print("The number has", count, "digits.")

# i = 1
# fact = 1

# while i <= 5:
#     fact = fact * i
#     i += 1

# print(fact)

# for i in range(1, 5+1):
#     print(i)


# int('Hello')


# S = "Hello IT F20"
# #0  l
# print(S[::-3])



# def myfunction(n):
#     return lambda a : a * n

# myval = myfunction(3)

# print(myval(4))

# fhand = open("ray.txt", 'w')

# fhand.write("This is Rayan. So OK. ")
# fhand.close()



# def commList(list1, list2):
#     for l1 in list1:
#         for l2 in list2:
#             if l2 == l1:
#                 return True
#     return False


# list1 = [7, 'ray', 12.2, 6, 10, 3.756]
# list2 = ['ahmed', 100, 98, 33, 100, 2.2, 'qs']
# res = commList(list1, list2)
# print(res)

# s = 'pining for the fjords'
# t = list(s)
# print (t)

# fname = input('Enter file name: ')
# try:
#     fhand = open(fname)
#     d = dict()

# except:
#     print("File cannot be opened")
#     exit(0)

# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in d:
#             d[word] = 1
#         else:
#             d[word] = d[word] + 1


# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key, val in counts:
#     print (key, counts[key])

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# lst = list(counts)
# print (lst)

# a = 5
# b = 10

# print(a, b)

# a, b = b, a

# print(a, b)

# dic = {('Rayan','Shabbir'):1, ('Ahmed','Ali'):2, ('Ali','Arslan'):3}

# for key, val in dic:
#     print(key, val, dic[key, val])


# t1 = (1, 2, 3, 4)

# for i in t1:
#     print(i)

# lst = [1, 2, 3, 4, 5]
# print(sum(lst))

# import numpy as np
# print(list(np.arange(4)))

import numpy as np

# tran_set = np.array([1, 2, 3])
# test_set = np.array([[0, 1, 2], [1, 2, 3]])

# resulting_set = np.vstack([tran_set, test_set])
# # resulting_set = np.concatenate([tran_set, test_set])
# # resulting_set = tran_set.append(test_set)
# print(resulting_set)

# a = np.arange(10).reshape(2, -1)
# b = np.repeat(1, 10).reshape(2, -1)
# # print(a)
# # print(b)

# print(np.c_[a, b])

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([9, 7, 3, 8, 5, 2])

# print(np.where(a == b))

a = np.arange(15)

# print(a[(a>=5) & (a<=10)])
# np.where((a>=5)&(a<=10))
# np.where(np.logical_and(a>=5, a<10))

# def maxx(x, y):
#     if x >= y:
#         return x
#     else:
#         return y

# pair_max = np.vectorize(maxx, otypes=[float])

# a = np.array([5, 7, 9, 8, 6, 4, 5])
# b = np.array([6, 3, 4, 8, 9, 7, 1])

# print(pair_max(a, b))

# a = np.array([1, 2, 3])
# # print(np.repeat(a, 10).reshape(2, -1))
# # print(np.tile(a, (3, 1)))

# np.r_[np.repeat(a, 3), np.tile(a, 3)]

# print(a.argmin(), a.argmax())


# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# z = np.empty_like(x)
# # print(z)

# vv = np.tile(z, (2, 1))     # Stack 4 copies of v on top of each other

# print(vv)

# # y = x + vv                  # Add x and vv elementwise
# # print(y)
# # print("\n")

a = np.arange(9).reshape(3, 3)
# print(a[:, ::-1])
print(np.size(a))