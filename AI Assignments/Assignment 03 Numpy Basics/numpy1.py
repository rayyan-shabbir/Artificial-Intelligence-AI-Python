import numpy as np

a = np.array([1, 2, 3, 4, 5, 0])      # It will create 1 rank array

print(a.shape)

print(a)

print(type(a))

print(a[0])
print(a[2])
# print(a[3])       # Out of bound ERROR

a[0] = 5
print(a)

aa = np.array([[1, 2, 3, 4]])         # It will create 2 rank array . 1 x 3

print(aa.shape)

print(aa)

b = np.array([[1, 2, 3], [4, 5, 6]])     # It will create 2 rank array.  2 x 3

print(b.shape)

print(b)

print(b[0, 0], b[0, 2], b[1, 1], b[1, 2])