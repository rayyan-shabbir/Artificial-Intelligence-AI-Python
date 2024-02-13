# File Handling
fhand = open("test.txt")
print(fhand)

# print(fhand.read())

inp = fhand.read()
print(inp)

print(inp[:20])

print("\n")

# counting no of line in a file
fhand = open("test.txt")
count =  0

for line in fhand:
    print(line)
    count += 1

print("Number of lines in file are:", count)

print("\n")


# write aprogram that looks for the string "leave" in each line of the file "test.txt" and prints found if string is found in that line or not found if string is not found in that line 

word = "leave"
fhand = open("test.txt")

for line in fhand:
    if word in line:
        print("String is found")
    else:
        print("String is not found")



# write a program that allows you to read a file upto 10 characters
fhand = open("test.txt")
read_char = fhand.read()

print(read_char[:10])


print("\n")

# write a program to read a file and print the contents of the file in upper case
fhand = open("test.txt")
read_char = fhand.read()

print(read_char.upper())

print("\n***\n")



# write a program that opens and prints the first two lines of the file "test.txt"
fhand = open("test.txt")
count = 0

for line in fhand:
    if count >= 2:
        break
    else:
        print(line)
    count += 1


print("\n***\n")


# Using try, except and open
# fname = input("Enter File name: ")

# try:
#     fhand = open(fname)
# except:
#     print("File does not exists!")
#     exit()

# count = 0
# for line in fhand:
#     count += 1
# print("Number of lines in your file are:", count)

# print("\n***\n")


# Writing to a file
# modes::
# r -> read mode (default mode)
# w -> write mode (it creates file if not exists) (if file exists it deletes its content and write to it.)
# a -> write at end of a file (append mode)
# r+ -> read and write mode (write at start of file)
# w+ -> write and read mode

# Writing to a file
fout = open("ray.txt", "w")

line = "This is Me"
fout.write(line)
fout.close()


# ***Note***
# if we have
s = '1 2\t 3\n 4'

print(s)            # It will use \n for new line and \t for tab space
print(repr(s))      # It simply print the string as to is without assuming what \n or \t do   


# Write a program that open and read the file after appending text to a file
# fout = open("test.txt", "a")
# line1 = "\n\nSo My name is Joker"

# fout.write(line1)
# fout.close()

# fhand = open("test.txt", "r")


# inp = fhand.read()

# print(inp)

