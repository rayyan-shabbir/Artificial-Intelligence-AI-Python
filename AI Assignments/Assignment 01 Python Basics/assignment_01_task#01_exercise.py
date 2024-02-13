# Write a program that uses raw_input to prompt a user for their name and then welcomes them.

# Enter your name: Chuck
# Hello Chuck

# raw_input = input("Enter your name: ")

# print("Hello", raw_input)



# Write a program to prompt the user for hours and rate per hour to
# compute gross pay.

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

# hours = input("Enter Hours: ")
# rate = input("Enter Rate: ")

# pay = int(hours) * float(rate)

# print("Pay:", pay)



# Assume that we execute the following assignment statements:
# width = 17
# height = 12.0

# For each of the following expressions, write the value of the expression and the
# type (of the value of the expression).

# 1. width/2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5

# Use the Python interpreter to check your answers.

width = 17
height = 12.0

print(width/2)
print(type(width/2))


print(width/2.0)
print(type(width/2.0))


print(height/3)
print(type(height/3))


print(1 + 2 * 5)
print(type(1 + 2 * 5))
print("\n")

# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit and print out the converted temperature.

celc = input("Enter Celsius Temperature: ")

# Formula:: (0°C × 9/5) + 32 = 32°F
Far = (float(celc) * 9/5) + 32

print("Fahrenheit Temperature is:", Far)
