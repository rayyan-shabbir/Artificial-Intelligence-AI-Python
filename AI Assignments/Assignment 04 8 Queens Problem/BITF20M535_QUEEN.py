# Including libraries
import numpy as np
import random as rand

# Class of Chess Board Objects
class ChessBoard:

    # Constructor
    def __init__(self):
        self.cBoard = np.zeros((8,8))

        for i in range(8):
            row = rand.randint(0,7)
            self.cBoard[row][i] = 1
        self.queen_attacks = np.zeros((1, 8))

    # Fitness Function
    def fitnessFunction(self):
        for i in range(8):
            for j in range(8):
                if self.cBoard[i][j] == 1:
                    rowI = i
                    colJ = j

                    # move forward
                    while(colJ < 8):
                        if self.cBoard[rowI][colJ] == 1 and colJ != j:
                            self.queen_attacks[0][j] += 1
                            break
                        colJ = colJ+1

                    rowI = i
                    colJ = j  

                    # move backward
                    while(colJ >= 0):
                        if self.cBoard[rowI][colJ] == 1 and colJ != j:
                            self.queen_attacks[0][j] += 1
                            break
                        colJ = colJ-1

                    rowI = i
                    colJ = j  

                    # moving forward-downward diagonal
                    while(colJ < 8 and rowI < 8):
                        if self.cBoard[rowI][colJ] == 1 and colJ != j and rowI != i:
                            self.queen_attacks[0][j] += 1
                            break
                        colJ = colJ+1
                        rowI = rowI+1

                    rowI = i
                    colJ = j  

                    # move backward-upward diagonal
                    while(colJ >= 0 and rowI >= 0):
                        if self.cBoard[rowI][colJ] == 1 and colJ != j and rowI != i:
                            self.queen_attacks[0][j] += 1
                            break
                        colJ = colJ-1
                        rowI = rowI-1
                    
                    rowI = i
                    colJ = j  

                    # move forward-upward diagonal
                    while(colJ < 8 and rowI >= 0):
                        if self.cBoard[rowI][colJ] == 1 and colJ != j and rowI != i:
                            self.queen_attacks[0][j] += 1
                            break
                        colJ = colJ+1
                        rowI = rowI-1
                    
                    rowI = i
                    colJ = j  

                    # move backward-downward diagonal 
                    while(colJ >= 0 and rowI < 8):
                        if self.cBoard[rowI][colJ] == 1 and colJ != j and rowI != i:
                            self.queen_attacks[0][j] += 1
                            break
                        colJ = colJ-1
                        rowI = rowI+1

        self.prime_level = 0

        # checking no. of queens which are correctly placed
        for i in range(8):
            if self.queen_attacks[0][i] == 0:
                self.prime_level += 1    


# Creating 4 (8x8) Chess Board objects
board1 = ChessBoard()
board2 = ChessBoard()
board3 = ChessBoard()
board4 = ChessBoard()

iterav = 0

# For picking best chess boards
bestChessBoardName_1 = None
bestChessBoardName_1 = None

bestChessBoard1 = -1
bestChessBoard2 = -1

# Creating dictionery for checking best level of each chess board
chessBoard_prime_dict = dict()


while(True):

    board1.fitnessFunction(), board2.fitnessFunction(), board3.fitnessFunction(), board4.fitnessFunction()

    if board1.prime_level == board3.prime_level and iterav > 2000 and iterav < 4000:
        board1 = board4

    # checking Goal founding in 1st chess board, and stop
    if board1.prime_level >= 8:

        print("\n#SOLUTION FOUND#\n")
        print("\n***Goal Chess Board***\n")
        print(board1.cBoard)
        print("\nQueens Attacking:: ", board1.queen_attacks)
        print("\n")
        break

    # checking Goal founding in 2nd chess board, and stop
    if board2.prime_level >= 8:

        print("\n#SOLUTION FOUND#\n")
        print("\n***Goal Chess Board***\n")
        print(board2.cBoard)
        print("\nQueens Attacking:: ", board2.queen_attacks)
        print("\n")
        break
    
    # checking Goal founding in 3rd chess board, and stop
    if board3.prime_level >= 8:

        print("\n#SOLUTION FOUND#\n")
        print("\n***Goal Chess Board***\n")
        print(board3.cBoard)
        print("\nQueens Attacking::  ", board3.queen_attacks)
        print("\n")
        break

    # checking Goal founding in 4th chess board, and stop
    if board4.prime_level >= 8:

        print("\n#SOLUTION FOUND#\n")
        print("\n***Goal Chess Board***\n")
        print(board4.cBoard)
        print("\nQueens Attacking::  ", board4.queen_attacks)
        print("\n")
        break




    # putting prime_value for each Chess Board
    chessBoard_prime_dict[board1] = board1.prime_level
    chessBoard_prime_dict[board2] = board2.prime_level
    chessBoard_prime_dict[board3] = board3.prime_level
    chessBoard_prime_dict[board4] = board4.prime_level


    # Getting 1st best from population
    value = 0
    for i in chessBoard_prime_dict:
        if chessBoard_prime_dict[i] >= max(chessBoard_prime_dict.values()):
            bestChessBoard1 = i
            value = i

    # Removing 1st best population value
    chessBoard_prime_dict.pop(value)

    # Getting 2nd best from population
    for i in chessBoard_prime_dict:
        if chessBoard_prime_dict[i] >= max(chessBoard_prime_dict.values()):
            bestChessBoard2 = i


    board1 = bestChessBoard1
    board2 = bestChessBoard2

    board3 = ChessBoard()
    board4 = ChessBoard()

    # Generating offspring # 03 by using Cross-Over
    for i in range(8):
        for j in range(8):
            if j < 4:
                board3.cBoard[i][j] = board1.cBoard[i][j]
            else:
                board3.cBoard[i][j] = board2.cBoard[i][j]

    # Generating offspring # 04 by using Cross-Over
    for i in range(8):
        for j in range(8):
            if j < 4:
                board4.cBoard[i][j] = board2.cBoard[i][j]
            else:
                board4.cBoard[i][j] = board1.cBoard[i][j]
    
    # Toogle Queen by using Mutation in board # 03
    row_1 = rand.randint(0,7)
    column_1 = rand.randint(0,7)


    for i in range(8):
        if board3.cBoard[i][column_1] == 1:
            board3.cBoard[i][column_1] = 0
    board3.cBoard[row_1][column_1] = 1

    # Toogle Queen by using Mutation in board # 04
    row_2 = rand.randint(0,7)
    column_2 = rand.randint(0,7)
    

    for i in range(8):
        if board4.cBoard[i][column_2] == 1:
            board4.cBoard[i][column_2] == 0
    board4.cBoard[row_2][column_2] = 1

    iterav = iterav + 1

        

print("\nTotal Iterartions:: ", iterav)

