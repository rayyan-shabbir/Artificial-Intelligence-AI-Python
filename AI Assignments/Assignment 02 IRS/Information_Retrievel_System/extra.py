# # # def word_count(dict1, fhand1):
# # #     for line in fhand1:
# # #         words = line.split()
# # #         for word in words:
# # #             cnt = dict1.get(word, 0)
# # #             dict1[word] = cnt + 1

# # # # FILE # 01
# # # try:
# # #     fhand1 = open("ray1.txt")
# # #     fhand2 = open("ray2.txt")
# # #     fhand3 = open("ray3.txt")
# # #     fhand4 = open("ray4.txt")
# # #     # print(fhand1)
# # #     # print(fhand2)
# # #     # print(fhand3)
# # #     # print(fhand4)
# # # except:
# # #     print("File cannot be opened")
# # #     exit(0)

# # # # str = fhand.read()
# # # # print(str)

# # # dict1 = dict()
# # # word_count(dict1, fhand1)
# # # word_count(dict1, fhand2)
# # # word_count(dict1, fhand3)
# # # word_count(dict1, fhand4)

# # # # for line in fhand1:
# # # #     words = line.split()
# # # #     for word in words:
# # # #         cnt = dict1.get(word, 0)
# # # #         dict1[word] = cnt + 1

# # # print(dict1)

# # # # for line in fhand2:
# # # #     words = line.split()
# # # #     for word in words:
# # # #         cnt = dict1.get(word, 0)
# # # #         dict1[word] = cnt + 1

# # # # # print(dict1)

# # # # for line in fhand3:
# # # #     words = line.split()
# # # #     for word in words:
# # # #         cnt = dict1.get(word, 0)
# # # #         dict1[word] = cnt + 1

# # # # # print(dict1)


# # for line in fhand4:
# #     words = line.split()
# #     for word in words:
# #         if dic[word] 

# # # # print(dict1)


# # fhand = open("ray1.txt")

# # print(fhand.readlines())

# file_count = 4


# unique_word_dict = dict()

# for i in range(file_count):
#     fname = "f"+str((i+1))+".txt"
#     fh = open(fname)
#     data = fh.read().upper()
#     for word in data.split():
#         if word not in dictionery:
#             dictionery[word] = 1
#         else:
#             dictionery[word] += 1

# unquWord = len(unique_word_set)
# TermMatrix = np.zeros((file_count, unquWord))

# print("TERM DOC MATRIX initially\n", Term_Document_Matrix)

# print("\nDictionery of unique words\n", unique_word_dict)

# print("\nDictionery of files\n", files_dict)

# query_vector = np.zeros((1, len(unique_word_set)))

# query_vector = query_vector.T

# print(query_vector)

# query = input("\nWrite something for searching:: ")
# # Check every word of query if it exists in the set of unique words or not
# # If exixts then increment the count of that word in word dictionary

colVector = np.zeros((1, len(unique_word_set)))

colVector = colVector.T

print(colVector)

query = input("\nWrite something for searching:: ")
# Check every word of query if it exists in the set of unique words or not
# If exixts then increment the count of that word in word dictionary

r = 0
i = 0
query_str = query.upper().split()
for queuer in query_str:
    r = 0
    for word in unique_word_set:
        if queuer in word:
            query_vector[r][i] = 1
        r = r + 1

# r = 0
# i = 0
# query_str = query.upper().split()
# for queuer in query_str:
#     r = 0
#     for word in unique_word_set:
#         if queuer in word:
#             query_vector[r][i] = 1
#         r = r + 1


# resultantVector = np.dot(TermMatrix,colVector)

# print(resultantVector)
# max=np.amax(resultant_matrix)
# print(max)
# maxInd = np.argmax(resultant_matrix)
# print(maxInd)
r = 1
for i in resultantVector:
    if max== i:
        file = "f"+str(i)+".txt"
        r += 1
    else:
        r += 1
print(file)
fh = open(file)
for line in fh:
    print(line)