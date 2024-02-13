# Syntactically, a tuple is a comma-separated list of values:
t = 'a', 'b', 'c', 'd', 'e'
print (t)

t1 = ('a', 'b', 'c', 'd', 'e')
print (t1)

t1 = 'a'
print(type(t1))

t2 = ('b')
print(type(t2))

t3 = 'a',
print(type(t3))

t4 = ('b',)
print(type(t4))

t = tuple() # it creates an empty tuple:
print (t)

# If the argument is a sequence (string, list or tuple), the result of the call to tuple
# is a tuple with the elements of the sequence:
t1 = tuple('lupins')
t2 = tuple([1, 2, 3, 4, 5])
t3 = tuple((3, 2, 1, 5, 'a'))
print (t1)
print (t2)
print (t3)


# You can’t modify the elements of a tuple, but you can replace one tuple with another:
t = ('a', 'b', 'c', 'd', 'e', 'f')
t = ('A',) + t[1:]

print(t)

print("\n")



d = {'a':10, 'd':1,'b':1, 'c':22}
t = d.items()
print(t)

# t.sort()
# print(t)

for key, val in d.items():
    print(val, key)

print("\n")

# Assignment: contents of a dictionary sorted by the value stored in each key/value pair
d = {'a':10, 'd':1,'b':1, 'c':22}
l = list()

for key, val in d.items():
    l.append((val, key))

print(l)
l.sort(reverse = True)
print(l)

print("\n")

# Swap two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1

print(tuple1)
print(tuple2)

print("\n")


# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)

lst = list()

for tup in tuple1:
    if tup == 44 or tup == 55:
        lst.append(tup)

tup = tuple(lst)

print(tuple1)
print(tup)
