import numpy as np

#Q 6
# numpy Functions
# zero = np.zeros((1, 2))     # Create a 2x2 matrix conatining all zero
# print(zero)

# one = np.ones((1, 3))       # Create a 2x2 matrix conatining all ones
# print(one)

# full = np.full((1, 4), 5) # Create a 3x3 matrix conatining all 12
# print(full)

# Q 7
x = [10, 20, 30]
# x = np.append(x, [40, 50, 60])
s = set(x)

s.update({40, 50, 60})

b = np.array(s)

print(x)
print(s)
print(b)
print(x)

#Q 5

# lst = [1, 2, 3, 4, 5, 6]

# odd = [f for f in lst if f%2 != 0 and f <= 3]

# print(odd)

# OR


# def oddNum(n, l):
#     odd = [f for f in l if f%2 != 0 and f <= n]

#     return odd

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(oddNum(5, lst))

# num = [i**2 for i in range(10)]
# print(num)

# print( np.vstack((zero, one)))
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.vstack((a,b)))

# print(a)

# array1 = np.vstack((array, full))

# print(array)


# iden = np.eye(3)            # Create a 3x3 identity matrix
# print(iden)

# rand = np.random.random((3, 3))     # Create a 3x3 matrix conatining random values
# print(rand)


print("\n")



# for k in range(0, 30, 4):
#     print(k)