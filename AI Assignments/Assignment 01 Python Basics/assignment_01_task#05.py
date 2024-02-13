from math import atan


fruit = 'banana'

# print the last element of string using len function 
# print(fruit[len(fruit) - 1])


# Alternatively, you can use negative indices
# print(fruit[-1])        # -1 displays last character
# print(fruit[-2])        # -2 displays second last character
# print(fruit[-3])        # -3 displays third last character

print("\n")

# # Traversal through a string with a loop (while) in reverse order
# index = (len(fruit)-1)

# while index >= 0:
#     letter = fruit[index]
#     print(letter)
#     index -= 1

# print("\n")


# Traversal through a string with a loop (for) in reverse order
index = (len(fruit) - 1)

for iterav in fruit:
    letter = fruit[index]
    print(letter)
    index -= 1



# what is the output of s[:]

s = 'Hello Pakistan'

print(s[:])



# print the string excluding the last character
# string is "Code Crew"
string = "Code Crew"

print(string[:(len(string))-1])


print("\n")

# your program should accepts a string from user and display the string with first character of each word with capital

# line = input("Enter string: ")

# capt = str.title(line)

# print(capt)


# Extra Try...

# s = "python is a lang"

# result = s[0].upper() + s[1:]
# result2 = result
# count = 0

# for ine in s:
#     if ine == ' ':
#         result2 = result[0:(count+1)] + result[count+1].upper() + result[count+2:]
#         print(result2)
#     count += 1

# print("After capitalizing first letter:")
# print(result2)




# write a program which accepts a string and display first two characters of each string in a separate line
# stre = input("Enter string: ")

# print(stre[:2])
# count = 0

# for i in stre:
#     if i == ' ':
#         print(stre[count+1:count+3])
#     count += 1



# print characters on odd index using loop (for or while)
# data = "Rayan is a Boy"
# index = 0

# while index < len(data):
#     if index %2 != 0:
#         print(data[index])
#     index += 1


# print characters on odd index using Slice operator

# print(data[1::2])
# print(data[1:len(data):2])


# replace the exclaimation mark in above string with a question mark

greeting = 'Hello, world!'
new_string = greeting[:(len(greeting)-1)] + '?'

print(new_string)



# Write a program that counts the number of times the letter 'n' appears in a string "banana"
word = 'banana'
count = 0

for letter in word:
    if letter == 'n':
        count += 1
    
print(count)


# Write a program that take character or sequence of characters from user and check if that 
# input is in the word then print message "string found" else "string not found" using 
# for or while loop

# word = 'banana'
# i = 0

# s_char = input("Enter character(s): ")
# j = 0
# count = 0

# while i < len(word):
#     j = 0
#     while (j < len(s_char)) and (word[i] == s_char[j]):
#         count += 1
#         i += 1
#         j += 1
#     if count == len(s_char):
#         print("String Found")
#         break

#     i += 1
# if count != len(s_char):
#     print("String not found")


# Write a program that take character or sequence of characters from user and check if that 
# input is in the word then print message "string found" else "string not found" using 
# in operator

# word = 'banana'

# s_char = input("Enter character(s): ")

# if s_char in word:
#     print("String found")
# else:
#     print("String not found")



# define a function that accepts a string and calculate the number of upper case letters and lower case letters

# ord function is used to check ASCII value of a character
def count_upper_and_lower(data):
    count_upper = 0
    count_lower = 0

    for letter in data:
        if ord(letter) >= 65 and ord(letter) <= 90:
            count_upper += 1
        elif ord(letter) >= 97 and ord(letter) <= 122:
            count_lower += 1

    print("Upper Case count:", count_upper)

    print("Lower Case count:", count_lower)


count_upper_and_lower("RayanRDXxxxxz")


# String methods
print("\n")

# Captalize (It capitalize the first character and rest lower case)
line = "rayAn iS me"

print(str.title(line))

print(str.capitalize(line))

print(dir(line))

print(line.find('a'))

print(line.find('is'))

print(line.find('a', 2))

line2 = "  He is the   mannnn   "
print(line2.strip())

print(line.upper())

print(line.lower())

print(line.startswith("Rayan"))

print(line.startswith("rayAn"))

print(line.lower().startswith("rayan"))



print("\n")
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# write a program to extract stephen.marquard in name variable and uct.ac.za 
# in domain varibale using above parsing methods

data = "stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

atloc = data.find('@')
name = data[:atloc]

sploc = data.find(' ')
domain = data[atloc+1 : sploc]

print(name)

print(domain)