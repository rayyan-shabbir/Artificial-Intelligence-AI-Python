# what is type of False

print(type(False))


# if x = 10 and y = 10, which of the above statements will return True
x = 10
y = 10

print(x == y)

print(x is y)

print(x <= y)

print(x >= y)
print("\n")

# if x = 10 and y = 30, which of the above statements will return False
x = 10
y = 30

print(x == y)

print(x >= y)

print(x > y)

print(x is y)
print("\n")


a = 10
b = "10"

print(a is b)



x = 6
print (x > 0 and x < 10)

print (not (x%2 == 0))

17 and True


# what will be the output of 0 or True
0 or True

# Output: True



# what will be the output of 1 and False
1 and False

# Output: False



# will the output be true or false
print((True or False) and False)

#Output: False

# now try it out without parantheses

print(True or False and False)

# Output: True


# if statement

choice = 'b'

if choice == 'a':
    print("Bad Guess")
elif choice == 'b':
    print("Good Guess")
else: 
    print("Try Again")


x = 5
if x > 0:
    pass            # It does nothing



# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range 
# print an error. If the score is between 0.0 and 1.0, print a grade using the following 
# table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

# score = float(input("Enter score (between 0.0 and 1.0): "))


# if score < 0.0 or score > 1.0:
#     print("ERROR! Input is out of range")
# elif score >= 0.9:
#     print("Your Grade is: A")
# elif score >= 0.8:
#     print("Your Grade is: B")
# elif score >= 0.7:
#     print("Your Grade is: C")
# elif score >= 0.6:
#     print("Your Grade is: D")
# elif score < 0.6:
#     print("Your Grade is: F")



# Write a program that reads an integer and determines and prints whether it is odd or even. (Hint: First use the
#simple division, then introduce modulus operator).

num = int(input("Enter Number: "))

div = int(num/2)

# print (res)

if div * 2 is num:
    print("Number is Even")
else:
    print("Number is Odd")

# num = int(input("Enter number: "))

# if num%2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

# print("\n")

# Prompt the user for two numbers A & B, computes and displays C=A/B. If the number B is zero, displays a “division
# by Zero” message.

# A = int(input("Enter Number 1: "))
# B = int(input("Enter Number 2: "))


# if B is 0:
#     print("Division by Zero")
# else:
#     C = A/B
#     print("Value of A/B =",C)




# Input marks from a user, if marks are greater than 85 display “Excellent”, if the marks are between 80 and 84 (both inclusive)
# display “Very Good”, if the marks are between 75 and 79 (both inclusive) display “Good”, if the marks are between 70 and 74
# (both inclusive) display “Fair”, if the marks are between 65 and 69 (both inclusive) display “Satisfactory”, otherwise display
# “You may not get the degree with such marks”.

# marks = int(input("Enter your marks: "))

# if marks >= 85:
#     print("Excellent")
# elif marks >= 80 and marks <= 84:
#     print("Very Good")
# elif marks >= 75 and marks <= 79:
#     print("Good")
# elif marks >= 70 and marks <= 74:
#     print("Fair")
# elif marks >= 65 and marks <= 69:
#     print("Satisfactory")
# else:
#     print("You may not get the degree with such marks")
    



# Input a number form the user, if it is between 1 and 100, display “In Range” otherwise display “Out of Range”.
# num = float(input("\nEnter Number: "))

# if num >= 1 and num <= 100:
#     print("In Range")
# else:
#     print("Out of Range")



# TRY and EXCEPT

# inp = input('Enter Fahrenheit Temperature:')
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print (cel)
# except:
#     print ('Please enter a number')




# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
    
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input


try:
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    pay = hours * rate
    print("Your pay is:", pay)
except:
    print("Error, Please enter a numeric input.")