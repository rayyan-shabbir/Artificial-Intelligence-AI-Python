import numpy as np
import random as rn

chess1 = np.zeros((8,8))
chess2 = np.zeros((8,8))
chess3 = np.zeros((8,8))
chess4 = np.zeros((8,8))


for i in range(8):
    num1 = rn.randint(0, 7)
    num2 = rn.randint(0, 7)
    num3 = rn.randint(0, 7)
    num4 = rn.randint(0, 7)
    chess1[num1][i] = 1
    chess2[num2][i] = 1
    chess3[num3][i] = 1
    chess4[num4][i] = 1

print(chess1)
# print(chess2)
# print(chess3)
# print(chess4)

chess_list1 = []
chess_list2 = []
chess_list3 = []
chess_list4 = []


for i in range(8):
    for j in range(8):
        if chess1[j][i] == 1:
            chess_list1.append(j)

        if chess2[j][i] == 1:
            chess_list2.append(j)
        
        if chess3[j][i] == 1:
            chess_list3.append(j)

        if chess4[j][i] == 1:
            chess_list4.append(j)

print(chess_list1)
print(chess_list2)
print(chess_list3)
print(chess_list4)
