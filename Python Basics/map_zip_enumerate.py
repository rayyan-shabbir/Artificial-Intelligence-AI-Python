import numpy as np

# MAP map() function
names = ['Rayan', 'Ahmed', 'Shabbir', 'Ali']

def myfunc(n):
    return len(n)

s = map(myfunc, names)

print(s)
print(list(s))
print(type(s))
print("\n")


# to join to lists using maps
fnames = ['Rayan', 'Shahmeer', 'Ahmad', 'Shehryar']
lnames = ['Shabbir', 'Shabbir', 'Asif', 'Munawar']

def join(a, b):
    return a + ' ' + b

s1 = map(join, fnames, lnames)
print(list(s1))
print(type(s1))
print("\n")


# ZIP zip() function
# zip(iterator1, iterator2, iterator3, ....)

#Join two tuples together
fnames = ['Rayan', 'Shahmeer', 'Ahmad', 'Shehryar']
lnames = ['Shabbir', 'Shabbir', 'Asif', 'Munawar']

s2 = zip(fnames, lnames)
print(list(s2))
print(type(s2))
print("\n")

for i, j in zip(s2):
    print(i, j)


# ENUMERATE enumerate() 
fnames = ['Rayan', 'Shahmeer', 'Ahmad', 'Shehryar']
ID = enumerate(fnames)

# print(dict(ID))
print(type(ID))
# print(ID)

for a in ID:
    print(a)


# %timeit(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# %timeit[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
