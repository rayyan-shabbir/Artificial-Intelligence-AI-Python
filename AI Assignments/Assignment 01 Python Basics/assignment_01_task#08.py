# Creating empty disctionary with a built-in-function dict()
eng2spn = dict()
print(eng2spn)

print("\n")

# The squiggly-brackets, {}, represent an empty dictionary. 
# To add items to the dictionary, you can use square brackets:

eng2spn['one'] = 'uno'
print(eng2spn)

print("\n")


# Creating Dictionary by ourselves
eng2spn1 = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng2spn1)

print("\n")


# you use the keys to look up the corresponding values:
print(eng2spn1['two'])

print("\n")

# If the key isn’t in the dictionary, you get an exception:
# print (eng2spn1['four'])

# The len function works on dictionaries; it returns the number of key-value pairs:
print(len(eng2spn1))

print("\n")


# The in operator works on dictionaries; it tells you whether something appears as
# a key in the dictionary (appearing as a value is not good enough).
res = 'one' in eng2spn1
print(res)

res1 = 'uno' in eng2spn1
print(res1)


# To see whether something appears as a value in a dictionary, you can use the
# method values, which returns the values as a list, and then use the in operator:

vals = eng2spn1.values()
res2 = 'uno' in vals
print(res2)

print("\n")


# Dictionary as a set of counters
word = 'rayanshabbir'
d = dict()

for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
    
print(d)

print("\n")


# Dictionaries have a method called get that takes a key and a default value. If the
# key appears in the dictionary, get returns the corresponding value; otherwise it
# returns the default value. For example:
d = {'chunk' : 1, 'annie' : 42, 'jan' : 100}

print(d.get('jan', 0))
print(d.get('tim', 0))

print("\n")


# implement above code using get() method (no need to use if and else statement)
word = 'rayanshabbir'
d = dict()

for c in word:
    res = d.get(c, 0)
    d[c] = res + 1

print(d)

print("\n")


# count no of words in a file
# fname = input("Enter the file name: ")

# try:
#     fhand = open(fname)
# except:
#     print("File cannot be opened: ", fname)
#     exit()

# counts = dict()

# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
    
# print(counts)

print("\n")

# If you use a dictionary as the sequence in a for statement, it traverses the keys of
# the dictionary. This loop prints each key and the corresponding value:
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

for key in counts:
    print(key, counts[key])

print("\n")

# Printing sorting keys and their values of dictionery
counts1 = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}

lst = list(counts1.keys())
print(lst)

lst.sort()

for l in lst:
    print(l, counts1[l])

print("\n")

# Write a Python program to check if value 200 exists in the following dictionary.
sample_dict = {'a': 100, 'b': 200, 'c': 300}
flag = False

for key in sample_dict:
    if sample_dict[key] == 200:
        flag = True
        print("Value 200 exists in dictionery at a key: ", key)

if not flag:
    print("Value 200 does not exists in dictionery")

print("\n")

# Write a Python program to iterate over dictionaries using for loops.
# d = {'Red': 1, 'Green': 2, 'Blue': 3}
# SAMPLE OUTPUT:
# Red corresponds to  1
# Green corresponds to  2
# Blue corresponds to  3

d = {'Red': 1, 'Green': 2, 'Blue': 3}

for iterv in d:
    print(iterv, "corresponds to", d[iterv])

