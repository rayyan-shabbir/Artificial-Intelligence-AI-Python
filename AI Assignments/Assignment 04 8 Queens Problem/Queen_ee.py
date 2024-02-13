import numpy as np
import random as rand

class chest_Board:
    def __init__(self):
        self.board = np.zeros((8,8))
        for i in range(0,8):
            self.board[rand.randint(0,7)][i] = 1
        self.attacks = np.zeros((1,8))

    def check_attacks(self):
        for i in range(0,8):
            for j in range(0,8):
                if self.board[i][j] == 1:
                    var_i = i
                    var_j = j
                    while(var_j < 8):
                        if self.board[var_i][var_j] == 1 and var_j != j:
                            self.attacks[0][j] += 1
                            break
                        var_j = var_j+1
                    var_i = i
                    var_j = j  
                    while(var_j >= 0):
                        if self.board[var_i][var_j] == 1 and var_j != j:
                            self.attacks[0][j] += 1
                            break
                        var_j = var_j-1
                    var_i = i
                    var_j = j  
                    while(var_j < 8 and var_i < 8):
                        if self.board[var_i][var_j] == 1 and var_j != j and var_i != i:
                            self.attacks[0][j] += 1
                            break
                        var_j = var_j+1
                        var_i = var_i+1
                    var_i = i
                    var_j = j  
                    while(var_j >= 0 and var_i >= 0):
                        if self.board[var_i][var_j] == 1 and var_j != j and var_i != i:
                            self.attacks[0][j] += 1
                            break
                        var_j = var_j-1
                        var_i = var_i-1
                    
                    var_i = i
                    var_j = j  
                    while(var_j < 8 and var_i >= 0):
                        if self.board[var_i][var_j] == 1 and var_j != j and var_i != i:
                            self.attacks[0][j] += 1
                            break
                        var_j = var_j+1
                        var_i = var_i-1
                    
                    var_i = i
                    var_j = j  
                    while(var_j >= 0 and var_i < 8):
                        if self.board[var_i][var_j] == 1 and var_j != j and var_i != i:
                            self.attacks[0][j] += 1
                            break
                        var_j = var_j-1
                        var_i = var_i+1
        self.best = 0
        for i in range(0,8):
            if self.attacks[0][i] == 0:
                self.best += 1    


b1 = chest_Board()
b2 = chest_Board()
b3 = chest_Board()
b4 = chest_Board()

best_1 = -1
best_2 = -1
best_1_name = None
best_1_name = None



score_dic = dict()

iteration = 0

while(1):
    b1.check_attacks()
    b2.check_attacks()
    b3.check_attacks()
    b4.check_attacks()

    if b1.best == b3.best and iteration > 2000 and iteration < 4000:
        b1 = b4

    if b1.best >= 8:
        print(b1.board)
        print('\n')
        print("Attack : ",b1.attacks)
        break

    if b2.best >= 8:
        print(b2.board)
        print('\n')
        print("Attack : ",b2.attacks)
        break
    
    if b3.best >= 8:
        print(b3.board)
        print('\n')
        print("Attack : ",b3.attacks)
        break

    if b4.best >= 8:
        print(b4.board)
        print('\n')
        print("Attack : ",b4.attacks)
        break

    
    print("value board 1 : ",b1.best)
    print("value board 2 : ",b2.best)
    print("value board 3 : ",b3.best)
    print("value board 4 : ",b4.best)


    score_dic[b1] = b1.best
    score_dic[b2] = b2.best
    score_dic[b3] = b3.best
    score_dic[b4] = b4.best
    
    print('\n')


    value = 0
    for i in score_dic:
        if score_dic[i] >= max(score_dic.values()):
            best_1 = i
            value = i
    score_dic.pop(value)
    for i in score_dic:
        if score_dic[i] >= max(score_dic.values()):
            best_2 = i

    b1 = best_1
    b2 = best_2

    b3 = chest_Board()
    b4 = chest_Board()
    for i in range(0,8):
        for j in range(0,8):
            if j < 4:
                b3.board[i][j] = b1.board[i][j]
            else:
                b3.board[i][j] = b2.board[i][j]
    for i in range(0,8):
        for j in range(0,8):
            if j < 4:
                b4.board[i][j] = b2.board[i][j]
            else:
                b4.board[i][j] = b1.board[i][j]
    
    column1 = rand.randint(0,7)
    row1 = rand.randint(0,7)
    for i in range(0,8):
        if b3.board[i][column1] == 1:
            b3.board[i][column1] = 0
    b3.board[row1][column1] = 1

    column2 = rand.randint(0,7)
    row2 = rand.randint(0,7)
    for i in range(0,8):
        if b4.board[i][column2] == 1:
            b4.board[i][column2] == 0
    b4.board[row2][column2] = 1

    iteration = iteration + 1

        


