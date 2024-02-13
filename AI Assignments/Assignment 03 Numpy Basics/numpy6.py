import numpy as np

# BOOLEAN ARRAY INDEXING FOR 2D ARRAY
a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

b = a > 3

print(a[b])
print(a[a>3])

print("\n")

# Array Matrix / Math
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

print(x + y)
print(np.add(x, y))

print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print("\nDot Product")

# Inner product of vectors both produce 181
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product of vectors both produce [29, 67]
# print((x.dot(v)).shape)
print(x.dot(v))
# print(np.dot(x, v))

# Matrix / matrix product of vectors both produce [[19, 22],
                                                #  [43, 50]]
# print((x.dot(y)).shape)
print(x.dot(y))
# print(np.dot(x, y))


