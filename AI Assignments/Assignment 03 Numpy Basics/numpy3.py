# Two ways of accessing the data in the middle row of the array. Mixing integer indexing with slicing yields and array of lower rank, while using only slices yields an array of the same rank :: as the original array. 

import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

row_rank1 = a[1, :]             # Rank 1 view of the second row of a, Rank 1 array,  (4, )
row_rank2 = a[1:2, :]           # Rank 2 view of the second row of a, Rank 2 array,  1 x 4   

row_rn1 = a[:,2]                # Rank 1 view of the third row of a, Rank 1 array, (3, )
row_rn2 = a[:,2:3]              # Rank 2 view of the third row of a, Rank 2 array,  3 x 1   

print(row_rank1.shape)
print(row_rank2.shape)
print(row_rn1.shape)
print(row_rn2.shape)
print("\n")

print(row_rank1)
print(row_rank2)
print(row_rn1)
print(row_rn2)

print("\n")


# BOOLEAN ARRAY INDEXING
a = np.array([1, 2, 3, 4, 5, 6])

b = a>3

print(b)

print(a[b])

print(a[a>3])

print("\n")

# Array / Matrix math
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
# Elementwise sum; both produce the array

s1 = x + y
print(s1)
# print(c.shape)

s2 = np.add(x, y)
print(s2)
# print(d.shape)

print("\n")

# Elementwise subtract; both produce the array
d1 = x - y
print(d1)
# print(d1.shape)

d2 = np.subtract(x, y)
print(d2)
# print(d2.shape)
