# Before you can update a variable, you have to initialize it, usually with 
# a simple assignment

x = 0
x += 1
x = x + 1

x += 3

print(x)

print("\n")


# Print first 10 natural numbers using while loop.
n = 1

while n <= 10:
    print(n)
    n += 1

# Count total number of digits in a number.

# --> If we take INTEGER number as input
# num = int(input("Enter Number: "))

# count = 0

# while num >= 1:
#     num = num / 10
#     count += 1

# print("The number has", count, "digits.")

# # --> If we take STRING numberas input
# num = input("Enter Number: ")

# print(len(num))


# While and break statement

# while True:
#     line = input("Enter > ")
#     if line == "done":
#         break
#     print(line)
# print("Done!")


# While Continue and Break statement

# while True:
#     line = input("Enter > ")
#     if line[0] == '#':
#         continue
#     if line == "done":
#         break
#     print(line)

# print("Done!")





# find largest values from [3, 41, 12, 9, 74, 15]
# list1 = [3, 41, 12, 9, 74, 15]

# largest = None

# for iterav in list1:
#     if largest is None or iterav > largest:
#         largest = iterav
#     print("Largest:", largest, "Iterav:", iterav)

# print("Largest:", largest)



# find smallest values from [3, 41, 12, 9, 74, 15]
# list1 = [3, 41, 12, 9, 74, 15]

# smallest = None

# for iterav in list1:
#     if smallest is None or iterav < smallest:
#         smallest = iterav
#     print("Smallest:", smallest, "Iterav:", iterav)

# print("Smallest:", smallest)

print("\n")

# find Second largest values from [3, 41, 12, 9, 74, 15]

# list1 = [3, 41, 12, 9, 74, 15]

# for iterav in range(1, len(list1)):
#     key = list1[iterav]
#     j = iterav - 1

#     while j >= 0 and key < list1[j]:
#         list1[j+1] = list1[j]
#         j = j-1
    
#     list1[j+1] = key

# print(list1)
# print(len(list1))

# print("Second Largest Element =", list1[len(list1)-2])

# for ine in range(1, len(list1)):
#     print(ine)



# Calculate factorial of 5.

# num = int(input("Enter number you want factorial of: "))
# n = 1

# for i in range(1, num+1):
#     n = n * i

# print("Factorial:",n)




# Write a program to display only those numbers from a list that satisfy the following conditions

# 1) The number must be divisible by five
# 2)If the number is greater than 150, then skip it and move to the next number
# 3)If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0:
        if num > 500:
            break
        if num > 150:
            continue
        print("Number:", num)