import numpy as np

print(range(5, 10))

print(list(range(5, 10)))

# LAMBDA
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments; but can have only one expression.

# lambda arguments : expression

# A Lambda function that adds any number with 10
add = lambda x : x+10
print(add(5))

# multiplication
mul = lambda x,y:x*y
print(mul(3, 4))


# The power of lambda is better shown when you use them as anonymous function inside another function

# A function definition that takes 1 argument, and that argument will be multiplies with unknown number
def mul(x):
    return lambda a: x*a

lmul = mul(5)
print(lmul(3))