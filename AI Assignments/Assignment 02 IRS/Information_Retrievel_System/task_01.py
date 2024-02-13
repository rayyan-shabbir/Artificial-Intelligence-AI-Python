import numpy as np

# TASK - 01
def word_count(dict1, fhand1):
    for line in fhand1:
        words = line.split()
        for word in words:
            cnt = dict1.get(word, 0)
            dict1[word] = cnt + 1

# FILE # 01
try:
    fhand1 = open("ray1.txt")
    fhand2 = open("ray2.txt")
    fhand3 = open("ray3.txt")
    fhand4 = open("ray4.txt")
    # print(fhand1)
    # print(fhand2)
    # print(fhand3)
    # print(fhand4)
except:
    print("File cannot be opened")
    exit(0)

# str = fhand.read()
# print(str)

word_set = dict()
word_count(word_set, fhand1)
word_count(word_set, fhand2)
word_count(word_set, fhand3)
word_count(word_set, fhand4)

print(word_set)


# TASK - 02 & 03
word_to_id = word_set
count_of_words = len(word_set)
i = 1

print(count_of_words)
# print(word_to_id)

for key in word_to_id:
    word_to_id[key] = i
    i += 1

print(word_to_id)

id_to_word = dict()

for i in range(count_of_words):
    id_to_word[i+1] = 0

j = 1

for key in word_set:
    id_to_word[j] = key
    j += 1

print(id_to_word)


# TASK - 04
file_count = 4
Term_Matrix = np.zeros((file_count, count_of_words))

# print(Term_Matrix)

for i in range(file_count):
    fn = 'ray' + str(i+1) + '.txt'
    fhand = open(fn)
    k = 0
    for word in fhand.read().split():
        k = 0
        for uw in word_set:
            if word == uw:
                Term_Matrix[i][k] = 1
            k += 1


print(Term_Matrix)



#TASK - 05
query = input("Enter your search: ")

query_vector = np.zeros((1, count_of_words))

for word in query.split():
    j = 0
    for uw in word_set:
        if word == uw:
            query_vector[0][j] = 1
        j += 1


print(query_vector)

trans_of_query_vector = query_vector.T

print(trans_of_query_vector)

rank_matrix = np.dot(Term_Matrix, trans_of_query_vector)

print("\nRank Matrix")
print(rank_matrix)

# print("Maximum value : ",np.amax(rank_matrix))
i = 1

for iterav in rank_matrix:
    if np.amax(rank_matrix) == iterav:
        fn = "ray" + str(i) + ".txt"
    i += 1

# print(fn)
fhand = open(fn)
print(fhand.read())
