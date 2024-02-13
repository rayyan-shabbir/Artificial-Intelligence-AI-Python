import numpy as np

def add(a, b):
    total = a+b
    return total

print(add(3, 4))
print("\n")

# Passing tuple as argument in the function
def add(a, *b):
    total = a
    print(b)
    print(type(b))

    for i in b:
        total += i

    return total

print(add(2, 3, 4, 5))
print("\n")


# Passing list as arguement in fcuntion
def add(a, b):
    total = a
    print(b)
    print(type(b))

    for i in b:
        total += i

    return total

l = [2, 34, 5]
print(add(3, l))

print("\n")

# Passing list as arguement in fcuntion (but it will be considered as tuple)
def add(a, *b):
    total = a
    print(b)
    print(type(b))

    for i in b:
        total += i

    return total

l = [2, 34, 5]
print(add(3, *l))

print("\n")


# Passing Dictionery as argument in a function
# A function can accept arbitrary keyword argument using the following sytanx
def add(x, **kwargs):
    total = x
    print(kwargs)
    print(type(kwargs))

    for key, val in kwargs.items():
        total += val

    return total

print(add(2, y=10, z=12, w=2)) 

# print(add(2, x=10, z=12, w=2))      # This is an error / exception bcz here x varibale is passed by postion i.e 2 as well as by name i.e x=10, So function will try to map it by name not by postion. Thus, it gives an error
print("\n")


# Passing tuple and dictionery at a time in function
def add(*a, **kvargs):
    total = 0

    print(a, kvargs)
    print(type(a))
    print(type(kvargs))

    for i in a:
        total += i

    for key, val in kvargs.items():
        total += val

    return total

print(add(2, 3, x=10, y=12, z=100))
print("\n")
