# required imports
import numpy as np
import fnmatch
import os

# # STEP-01 :: CREATE FILE WITH DUMMY DATA
try: 
    fhand = open("ray1.txt", "w")
    fhand.write("I love Pakistan I love love")

    fhand = open("ray2.txt", "w")
    fhand.write("I love Cricket")

    fhand = open("ray3.txt", "w")
    fhand.write("Pakistan Cricket Team")

    fhand = open("ray4.txt", "w")
    fhand.write("I LOVE PUCIT I love pucit")

except:
    print("Dummy Files are not created, SORRY...")
    exit(0)

# # We can also create multiple files at once
# # for i in range(10):
# #     fileName = "rayy" + str((i+1)) + ".txt"
# #     fhand = open(fileName, "w")



# # STEP-02 :: TRAVERSE DIRECTORIES
# # Here we have intialized some variables, you can add more if required.

file_count = 0             # file_count to count number of files
files_dict = {}            # files_dic to store count of every file    
unique_word_set = set()    # unique_word_set to store all the unique words in a set

count = 0

for i in range(4):
    fname = "ray"+str((i+1))+".txt"
    files_dict[fname] = count
    count += 1

file_count = len(files_dict)
print("\nTotal Number  of files::", file_count)

print("\nDictionary containing  files\n", files_dict)


# # STEP-03 :: EXTRACT UNIQUE VOCABULARY
# # write code to print all the unique words in every file and store them in a set
for i in range(file_count):
    fhand = open("ray"+str((i+1))+".txt")
    unique_word_set.update(fhand.read().upper().split(" "))

print("Unique words in files:",unique_word_set)

print("\nCount of files:", file_count)
print("\n")
# for word in unique_word_set:
#     print(word)


# # STEP-04 :: CREATE TERM DOCUMENT MATRIX
# # Create Term doc matrix such that colmns will be unique words and all the files will be rows
# # Write code to count all the unique words appearances in all the files and store it in a dictionary for words 

def unique_word(fname, dic):
    fhand = open(fname)
    for line in fhand:
        words = line.upper().split()
        for word in words:
            cnt = dic.get(word, 0)
            dic[word] = cnt + 1


unique_word_dict = dict()

for i in range(file_count):
    fname = "ray"+str((i+1))+".txt"
    unique_word(fname, unique_word_dict)


Term_Document_Matrix = np.zeros((file_count, len(unique_word_dict)))

print("TERM DOC MATRIX initially\n", Term_Document_Matrix)

print("\nDictionery of unique words\n", unique_word_dict)

print("\nDictionery of files\n", files_dict)


# # STEP - 05 :: FILL TERM-DOCUMENT-MATRIX
# # Fill the term doc matrix by checking if the unique word exists in a file or not
# # If it exists then substitute a 1 in term_doc_matrix (eg : TERM_DOC_MATRIX[file][word] = 1 ) 
# # Do the same for all the files present in the directory

k = 0

for i in range(file_count):
    fname = "ray"+str((i+1))+".txt"
    fhand = open(fname)
    k = 0
    for word in fhand.read().upper().split():
        k = 0
        for uw in unique_word_dict:
            if uw == word:
                Term_Document_Matrix[i][k] = 1
            k += 1


print("\nTerm Document Matrix after filling\n", Term_Document_Matrix)
print("\n")

# # STEP - 06 :: ASK FOR A USER QUERY
# # For user query make a column vector of length of all the unique words present in a set
query_vector = np.zeros((len(unique_word_dict), 1))

print("\nQuery Vector Initially\n", query_vector)

# print(len(query_vector))
# print(len(unique_word_dict))

query = input("\nWrite something for searching:: ")
# # Check every word of query if it exists in the set of unique words or not
# # If exixts then increment the count of that word in word dictionary

j = 0
for q in query.upper().split():
    j = 0
    for uw in unique_word_dict:
        if q == uw:
            query_vector[j][0] += 1
            # unique_word_dict[uw] += 1
        j += 1

print("\nQuery Vector after filling\n", query_vector)


# # STEP - 07 :: DISPLAY THE RESULTANT VECTOR
# # Display

# # 1.Resultant vector.
# # 2.Max value in resultant vector.
# # 3.Index of max value in resultant vector.

resultant_matrix = np.dot(Term_Document_Matrix, query_vector)

print("\nResultant/Rank Matrix\n", resultant_matrix)

# # print(np.amax(query_vector))
print("\nMaximum in resultant is ", np.amax(resultant_matrix))

# # print(np.argmax(query_vector))
print("\nIndex of Maximum in resultant is ", np.argmax(resultant_matrix))


# # STEP - 08 :: DISPLAY THE CONTENTS OF FILE
# #Write the code to identify the file_name having maximum value in the resultant vector and display its contents.

print("\nContents of File\n")
flag = True

index = np.where(resultant_matrix == np.amax(resultant_matrix))

if np.amax(resultant_matrix) == 0:
    flag = False
    
if flag == False:
    print("No file with such query Found ")
else:
    i = 1
    for iterav in resultant_matrix:
        if np.amax(resultant_matrix) == iterav:
            fn = "ray" + str(i) + ".txt"
        i += 1

    filename = "ray" + str(index[0][0]+1) + ".txt"

    print("File Name with Query founded::", filename)   
    fhand = open(filename)
    print("Content::",fhand.read())
