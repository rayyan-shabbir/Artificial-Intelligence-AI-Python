import numpy as np

# To create empty set
s = set()

print(s)
print(type(s))

# Use braces to create set
s1 = {1, 'hi', 4, 6}

print(s1)

# We cannot create set by this (this is dictionery)
s2 = {}
print(s2)
print(type(s2))


# set don't allow duplication
s3 = {6, 2, 3, 4, 4, 5, 1}

print(s3)

# converting a list into set (This is used mostly to remove duplication from list)
lst = [2, 4, 5, 6, 4, 3, 2]
print(set(lst))

print("\n")

# SET OPERATIONS
st1 = {1, 2, 3, 4, 5, 6}
st2 = {2, 3, 4, 5, 7}

# union (Elements / things which are in st1 or in st2)
st3 = st1.union(st2)
print(st3)

# union can also be computed like this
st3 = st1 | st2
print(st3)

# intersection (Elements / things which are common in st1 and st2)
st4 = st1.intersection(st2)
print(st4)


# intersection can also be computed like this 
st3 = st1 & st2
print(st3)

print("\n")
# difference (Elements / things which are in st1but not in st2)
st5 = st1 - st2
print(st5)

# difference can also be computed like this
st5 = st1.difference(st2)
print(st5)

# symmetric difference (Elements / things which are in st1 or in st2 but not in both)
st6 = st1.symmetric_difference(st2)
print(st6)

# symmetric_difference can also be computed like this
st6 = st1 ^ st2
print(st6)

print("\n")

# Set Containment
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3}

# subset, both of them give the same answer
print(b.issubset(a))
# or
print(b <= a)

# superset
print(a.issuperset(b))

# disjoint
print(a.isdisjoint(b))

print("\n")

# SET METHODS
st = {1, 2, 3, 4, 5}

# Adiing elements
st.add(7)
print(st)

# To add collection of elements
st.update({8, 9, 10})
print(st)

# To remove elements from set
st.remove(7)
print(st)

st.remove(5)
print(st)

# if we try to remove the element that was not in the set, we got an error (exception)
# st.remove(7)
# print(st)

# if we try to remove an element without get worrying about error / exception
st.discard(7)
print(st)

st.discard(4)
print(st)

st.discard(4)
print(st)

# pop is used to remove the first elements from set
st.pop()
print(st)


print("\n")

# Frozenset (This is a special kind of set that is immutable (we cannot change anything in it))
fs = frozenset({1, 2, 3, 4, 4, 5, 5})

print(fs)

# fs.add(5)     # ERROR
# print(fs)