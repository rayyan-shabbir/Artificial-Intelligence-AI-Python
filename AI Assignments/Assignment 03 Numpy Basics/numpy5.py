import numpy as np

# numpy Functions
zero = np.zeros((2, 2))     # Create a 2x2 matrix conatining all zero
print(zero)

one = np.ones((2, 2))       # Create a 2x2 matrix conatining all ones
print(one)

full = np.full((3, 3), 12)  # Create a 3x3 matrix conatining all 12
print(full)

iden = np.eye(3)            # Create a 3x3 identity matrix
print(iden)

rand = np.random.random((3, 3))     # Create a 3x3 matrix conatining random values
print(rand)


print("\n")

# Create a new array from which we will select elements
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)

# Create an array of indices
b = np.array([0, 2, 0, 1])
print(b)

print(a[np.arange(4), b])

print(a[:, b])

print("\n")

# QUIZ
bb = np.array([0, 2, 0, 1])
print(a[bb, b])