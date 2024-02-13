import numpy as np
# Notice that both single quotes and double quotes give us the same string. You can pick whichever style that you like. We can also create multi-line strings, with embedded newline characters

s = "Hello/nPakistan"

print(s)

s = """Hello
Pak
is
tan"""

print(s)

# LIST COMPREHENSSION
# compute the square by convention/simple way
fields = [1, 2, 3, 4, 5]
sq = []

for field in fields:
    sq.append(field*field)

print(sq)

# compute the square by using list comprehenssion
fields = [1, 2, 3, 4, 5]

b = [f*f for f in fields]
print(b)


# calculate the sum of '1 2 3 4 5' conventionally
line = '1 2 3 4 5'
fields = line.split()
sum = 0

for field in fields:
    sum += int(field)

print(sum)
print("\n")

# calculate the sum of '1 2 3 4 5' using list comprehenssion


# Calculate the average of above list

# Calculate the Square of the lst1[10, 21, 4, 7, 12] greater than equal to 10
lst1 = [10, 21, 4, 7, 12]

sqr = [f*f for f in lst1 if f >= 10]
print(type(sqr))
print(sqr)

# DICTIONERY COMPREHENSSIONS
# build dictionery where keys are numbers and values are 10
fields = [1, 2, 3, 4, 5]

dic = {f:10 for f in fields}

print(dic)

# build dictionery where keys are numbers and values are key+10 where key is greater than 2
fields = [1, 2, 3, 4, 5]

dic1 = {f:f+10 for f in fields if f > 2}

print(dic1)