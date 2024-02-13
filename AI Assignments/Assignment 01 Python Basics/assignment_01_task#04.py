# Type conversion functions
int('32')
# int('Hello')
#int(3.99999)
#float(32)
#str(32)
#str(3.14159)



# find the purpose of math.copysign(x,y) function and run it with sample data
import math

print(math.copysign(4, -1))
print(math.copysign(-8, 97.21))
print(math.copysign(-43, -76))

print("\n")

# find the purpose of math.trunc(x) function and run it with sample data
print(math.trunc(7.34))
print(math.trunc(-187.90))
print(math.trunc(96.90))

print("\n")

# find the purpose of math.fabs(x) function and run it with sample data
print(math.fabs(-12.11))
print(math.fabs(-7))
print(math.fabs(-848))
print(math.fabs(44))


def rayan(rayan):
    print("My name is", rayan)

rayan("Rayannnnn")

print(rayan)
print(type(rayan))

print("\n")


# define a function, to which when your name is passed as an argument, returns the no of characters in your name

def name_length(name):
    no_chars = len(name)
    return no_chars


print(name_length("RDXXXX"))
print("\n")



# define a function to find the maximum of three numbers

def max_of_three(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c

    return max

print(max_of_three(27, 133, 1000))



# define a function that accepts an argument which is a string and you have to reverse that string

def rev_string(line):
    length = len(line)
    # print(length)

    line2 = ""

    for i in line:
        # print(i)
        line2 += line[length-1]
        length -= 1

    # print(line2)
    return line2


print(rev_string("Shahmeer"))