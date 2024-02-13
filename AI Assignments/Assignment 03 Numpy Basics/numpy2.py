import numpy as np

c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])     # It will create 2 rank array. 3 x 4

print(c)

print(c.shape)
print("\n")

# Slicing in numpy array

print(c[1:])

print(c[1,:])

print(c[:,2])

print(c[1:3,:])
print("\n")

b = c[:2, 1:3]
print(b)

# A slice of an array is a view into the same data, So modifying it will modify the original array

print(c[0, 1])      # prints "2"

b[0, 0] = 87        # b[0, 0] is the same piece of data as c[0, 1]
print(c[0, 1])      # prints "87"