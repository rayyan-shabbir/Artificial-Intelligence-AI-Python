import numpy as np

# SUM
x = np.array([[1, 2], [3, 4]])

# Compute sum of all the elements
sum = np.sum(x)
print(sum)

# Compute sum of each column
sum_column = np.sum(x, axis = 0)
print(sum_column)

# Compute sum of each row
sum_row = np.sum(x, axis = 1)
print(sum_row)

print("\n")

# TRANSPOSE OF NUMPY ARRAY

# Taking transpose of rank 2 matrix
a = np.array([[1, 2], [3, 4]])

c = a.T
print(c)

print(a.T)

# Note that taking transpose of rank 1 matrix does nothing
b = np.array([1, 2, 3])

print(b.T)

print("\n")

# BROADCASTING
# Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations.

# There are 3 ways of performing broadcasting

# 1) Using for loop :: (NOT RECOMMENDED)
# We will add the vector v to each row of the matrix x, storing the result in matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
y = np.empty_like(x)        # Create an empty matrix with same shape as x

v = np.array([1, 0, 1])

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i,:] = x[i,:] + v

print(y)
print("\n")

# 2) Using tile function
# We will add the vector v to each row of the matrix x, storing the result in matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])

vv = np.tile(v, (4, 1))     # Stack 4 copies of v on top of each other

print(vv)

y = x + vv                  # Add x and vv elementwise
print(y)
print("\n")


# 3) Using Broadcast concept that exists in python
# We will add the vector v to each row of the matrix x, storing the result in matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])

print(x + v)

y = x + v       # Add v to each row of x using broadcasting
print(y)