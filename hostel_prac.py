import numpy as np

a = np.array([1, 2, 3])     
print(a.shape)

print(a)

print(type(a))

print(a[0])
print(a[2])
# print(a[3])       # Out of bound ERROR

a[0] = 5
print(a[0])

aa = np.array([[1, 2, 3]])

print(aa.shape)
print(aa)

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b.shape)
print(b)

print(b[0, 0], b[0, 1], b[1, 0], b[1, 2])