from numpy import average


lst3 = ['spam', 2.0, 5, [10, 20]]

print(lst3)

# Write a function to sum all the items in a list , given the items in the list is integer
def sumList(list):
    sum = 0
    for i in list:
        sum += i
    
    return sum


list = [5, 4, 7, 9, 1]
sum = sumList(list)
print(sum)


# Write a function that takes two lists and returns true if they have at least one common member
def commList(list1, list2):
    for l1 in list1:
        for l2 in list2:
            if l2 == l1:
                return True


list1 = [7, 'ray', 12.2, 6, 10, 3.756]
list2 = ['ahmed', 10, 98, 33, 100, 2.2, 'qs']
res = commList(list1, list2)
print(res)

print("\n")



# range returns a list of indices from 0 to n−1, where n is the length of the list.

numbers = [17, 215]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

print("\n")


# Suppose you have two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400] 

j = len(list2) - 1

for i in range(len(list1)):
    print("List1 Index:", i, list1[i], "List2 Index:", j, list2[j])
    j -= 1

print("\n")

# To create list method

c = [1] * 3
print(c)

d = [4, 2] * 3
print(d)

print("\n")

# List Slices

t = ['a', 'b', 'c', 'd', 'e', 'f']
print( t[1:3] )

print(t[:4])

print(t[3:])

print(t[:])

print("\n")

# A slice operator on the left side of an assignment can update multiple elements:
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)

t[1:4] = ['x1', 'y1']
print(t)

print("\n")

# List Methods
# append adds a new element to the end of a list:
t = ['a', 'b', 'c']
t.append('d')

print(t)

print("\n")

# extend takes a list as an argument and appends all of the elements:
t1 = ['a', 'b', 'c']
t2 = ['d', 'e', 'f']

t1.extend(t2)

print(t1)

print("\n")

# sort arranges the elements of the list from low to high:
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

print("\n")


# Delete Element in List

# There are several ways to delete elements from a list. 
# If you know the index of the element you want, you can use pop:

t = ['a', 'b', 'c', 'd']
x = t.pop(2)
print(x)
print(t)

print("\n")

y = t.pop()
print(y)
print(t)

print("\n")

# If you don’t need the removed value, you can use the del operator:
t = ['a', 'b', 'c', 'd']
del t[1]
print(t)

print("\n")

# If you know the element you want to remove (but not the index), you can use remove:
t = ['a', 'b', 'c','b']
t.remove('c') # The return value from remove is none
print(t)

print("\n")


# To remove more than one element, you can use del with a slice index:
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:4]
print(t)

print("\n")


# Write a program to remove an empty string from list of strings 
str1 = ['ray', 'amm', 'rdx', '', 'kumo']
str1.remove('')
print(str1)

print("\n")


# Write a program to print the numbers of a specified list after removing even numbers from it.
listt = [21, 65, 12, 3, 0, 7, 96]

for lst in listt:
    if lst % 2 == 0:
        # print(lst)
        listt.remove(lst)
    
print(listt)

print("\n")


# Built In Functions
# nums1 = [3, 41, 12, 9, 74, 15]
# print (len(nums1))
# print (max(nums1))
# print (min(nums1))
# print (sum(nums1))


# how we can compute average?
# ANS: We can compute the average by using sum() and len() built-in-functions of list


# print (sum(nums) / len(nums))

# OR

# avg1 = sum(nums) / len(nums)
# print(avg1)


# How can we compute the total length of the list?

# ANS: We can compute the total length of the list by using built-in-function len()

# print(len(nums))



# To convert a string to a list
# str1 = 'spam'
# t = list(str1)

# print(t)

# print("\n")

# Splitting the words of string and make it list
s = 'pining for the fjords'
t = s.split()

print(t)

print("\n")

# You can call split with an optional argument called a delimiter specifies which
# characters to use as word boundaries.
s = 'spam-spam-spam'
delimeter = '-'
print(s.split(delimeter))


# join is the inverse of split
t = ['pining', 'for', 'the', 'fjords']
delimeter = ' '
print(delimeter.join(t))

print("\n")


