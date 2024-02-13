# Write a program that reads an integer and determines and prints whether it is odd or even. (Hint: First use the
#simple division, then introduce modulus operator).

# BY USING SIMPLE DIVISION FIRST THEN MODULUS

num = int(input("Enter Number: "))

div = int(num/2) * 2

if div == num and div % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

    
# SIMPLE DIVISION
num = int(input("Enter Number: "))

div = int(num/2)

# print (div)

if (div * 2) == num:
    print("Number is Even")
else:
    print("Number is Odd")


# MODULUS OPERATOR
num = int(input("Enter number: "))

if num%2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


