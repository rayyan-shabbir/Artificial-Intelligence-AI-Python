import numpy as np
import random as rd

def printBoards():
    for k in range(4):
        print("Board ", k + 1)
        for i in range (8):
            for j in range(8):
                print(board[k][i][j], end = "\t")
            print()
        print("\n")
        
        
def printArrays():
    for k in range(4):
        print("Array ", k + 1)
        for i in range (8):
            print(array[k][i], end = "\t")
        print()
    print("\n")


def up(k,i,j):
    for n in range(i-1, -1, -1):
        if board[k][n][j] == 1:
            #count -= 1
            return True
    
    return False
            
def down(k,i,j):
    for n in range(i+1, 8):
        if board[k][n][j] == 1:
            #count -= 1
            return True
        
    return False    
            
            
def forward(k,i,j):
    for n in range(j+1, 8):
        if board[k][i][n] == 1:
            #count -= 1
            return True
        
    return False
            
            
def backward(k,i,j):
    for n in range(j-1, -1, -1):
        if board[k][i][n] == 1:
            #count -= 1
            return True
    
    return False
            
            
def up_left_dia(k,i,j):
    m,n = i,j
    for m in range(i-1, -1, -1):
        n -= 1
        if n < 0:
            return False
        if board[k][m][n] == 1:
            #count -= 1
            return True
        
    return False
    
    
def up_right_dia(k,i,j):
    m,n = i,j
    for m in range(i-1, -1, -1):
        n += 1
        if n > 7:
            return False
        if board[k][m][n] == 1:
            #count -= 1
            return True
        
    return False
            
            
def down_left_dia(k,i,j):
    m,n = i,j
    for m in range(i+1, 8):
        n -= 1
        if n < 0:
            return False
        if board[k][m][n] == 1:
            #count -= 1
            return True
        
    return False
            
            
def down_right_dia(k,i,j):
    m,n = i,j
    for m in range(i+1, 8):
        n += 1
        if n > 7:
            return False
        if board[k][m][n] == 1:
            #count -= 1
            return True
        
    return False
            
            
def fitness(k):
    count = 8
    
    for j in range(8): # j == column
        flag = False
        for i in range(8): # i == row
            
            if board[k][i][j] == 1:
                #print("i = ", i, "\tj = ", j)
                if j == 0:
                    #UP
                    if i != 0:
                        if flag == False:
                            flag = up(k,i,j)

                            
                    #FORWARD
                    if flag == False:
                        flag = forward(k,i,j)
                        #print("Forward Flag : " , flag)

                    
                    #DOWN
                    if i != 7:
                        if flag == False:
                            flag = down(k,i,j)

                    #UP-RIGHT-DIAGNOL
                    if i != 0:
                        if flag == False:
                            flag = up_right_dia(k,i,j)

                    #DOWN-RIGHT-DIAGNOL
                    if i != 7:
                        if flag == False:
                            flag = down_right_dia(k,i,j)
                        
                
                elif j == 7:
                    #UP
                    if i != 0:
                        flag = up(k,i,j)

                    #BACKWARD
                    if flag == False:
                        flag = backward(k,i,j)

                    #DOWN
                    if i != 7:
                        if flag == False:
                            flag = down(k,i,j)

                    #UP-LEFT-DIAGNOL
                    if i != 0:
                        if flag == False:
                            flag = up_left_dia(k,i,j)

                    #DOWN-LEFT-DIAGNOL
                    if i != 7:
                        if flag == False:
                            flag = down_left_dia(k,i,j)
                        
                 
                
                elif i == 0:
                   
                    #FORWARD
                    flag = forward(k,i,j)
                        
                            
                    #BACKWARD
                    if flag == False:
                        flag = backward(k,i,j)
                        

                    #DOWN
                    if flag == False:
                        flag = down(k,i,j)

                            
                    #DOWN-LEFT-DIAGNOL
                    if flag == False:
                        flag = down_left_dia(k,i,j)
                        

                    #DOWN-RIGHT-DIAGNOL
                    if flag == False:
                        flag = down_right_dia(k,i,j)

                
                
                elif i == 7:
                   
                    #FORWARD
                    flag = forward(k,i,j)                            
                            
                    #BACKWARD
                    if flag == False:
                        flag = backward(k,i,j)

                    #UP
                    if flag == False:
                        flag = up(k,i,j)

                            
                    #UP-LEFT-DIAGNOL
                    if flag == False:
                        flag = up_left_dia(k,i,j)


                    #UP-RIGHT-DIAGNOL
                    if flag == False:
                        flag = up_right_dia(k,i,j)
                
                
                else:
                    #FORWARD
                    flag = forward(k,i,j)
                    #print("Forward Flag : " , flag)
                            
                    #BACKWARD
                    if flag == False:
                        flag = backward(k,i,j)
                    
                    #UP
                    if flag == False:
                        flag = up(k,i,j)
                    
                            
                    #UP-LEFT-DIAGNOL
                    if flag == False:
                        flag = up_left_dia(k,i,j)

        
                    #UP-RIGHT-DIAGNOL
                    if flag == False:
                        flag = up_right_dia(k,i,j)

                
                    #DOWN
                    if flag == False:
                        flag = down(k,i,j)
                            
                            
                    #DOWN-LEFT-DIAGNOL
                    if flag == False:
                        flag = down_left_dia(k,i,j)


                    #DOWN-RIGHT-DIAGNOL
                    if flag == False:
                        flag = down_right_dia(k,i,j)
                
        
            #label .check
            if flag == True:
                count -= 1
                #print("Yes\t", count)
                break

                    
                    
                    
    return count


#INITIALIZING BOARDS AND ARRAYS 

board = np.zeros((4,8,8), dtype=int)
array = np.zeros((4,8), dtype=int)

#li = [6,2,4,1,0,0,6,2] #FOR TESTING FITNESS RETURNS

final_index = 0
count = 0

for k in range(4):
    for j in range (8):
        i = rd.randint(0,7)
        #i = li[j]
        board[k][i][j] = 1
        array[k][j] = i

        
#print("INITIAL BOARDS ARE ")
#printBoards()
#print("\nINITIAL ARRAYS ARE ")
#printArrays()


print("Working on Solution !...\n")

while(True): 
    
    #print("ITERATION NUMBER : ", count)

    fit = [fitness(0), fitness(1), fitness(2), fitness(3)]

    #BASE CASE
    if max(fit) == 8:
        final_index = fit.index(max(fit))
        break

        
#     print("Fitness Returns : ",fit)


    best_two_indx = np.argpartition(fit, -2)[-2:]

#    print(best_two_indx)
#     for i in best_two_indx:
#         print(fit[i])


    #DISCRADING WORST TWO BOARDS
    for i in range(4):
        if i not in best_two_indx:
            fit[i] = 0
            board[i] = np.zeros((8,8))
            array[i] = np.zeros(8)


    #EXTRACTING BEST TWO BOARDS/ARRAY
    best_two_array = np.zeros((2,8), dtype=int)
    k = 0
    for i in best_two_indx:
        best_two_array[k] = array[i]
        k+=1

        
    
#     print("\nBEST TWO INDEX ARE : ",best_two_indx) 
#     print("\nBEST TWO ARRAYS / BOARDS ARE \n",best_two_array)  


    #GENERATING OFFSPRINGS AND MUTATION
    k = 0
    m = 1
    for i in range(4):
        if i not in best_two_indx:
            array[i] = np.concatenate((best_two_array[k][0:4],best_two_array[m][4:8]), axis = 0)
            y,b = rd.randint(0,7), rd.randint(0,7)
            array[i][y] = b
            k = 1
            m = 0

    
    #GENERATING BOARDS FROM OFFSPRINGS
    for k in range(4):
        if k not in best_two_indx:
            for j in range (8):
                i = array[k][j]
                board[k][i][j] = 1



#     print("\nUPDATED OFFSPRINGS ARE ")
#     printArrays()

#     print("\nUPDATED BOARDS ARE ")
#     printBoards()


    count += 1
    
    
print("\nSOLUTION FOUND ")
print("\nTOTAL ITERATIONS ", count)

print("\nFinal Board ")
for i in range (8):
    for j in range(8):
        print(board[final_index][i][j], end = "\t")
    print()

print("\nFINAL ARRAY \n", array[final_index])



            #  ---------------------------------------------------------------------------------------- #
    
#FOR TESTING PURPOSE

# li  = [0,0,6,7,0,2,3,6] # Returns 0 
# li2 = [0,0,3,6,7,5,4,3] # Returns 0
# li3 = [2,6,0,2,2,3,1,7] # Returns 1
# li4 = [3,4,5,4,3,6,4,0] # Returns 0
# li5 = [3,7,3,6,6,2,5,3] # Returns 3
# li6 = [1,0,0,0,5,3,6,7] # Returns 0
# li7 = [0,4,3,5,1,4,3,4] # Returns 2
# li8 = [0,1,3,1,0,2,2,0] # Returns 1

# Solutions obtained

# sol1 = [5,2,6,1,7,4,0,3] # Returns 8
# sol2 = [1,6,4,7,0,3,5,2] # Returns 8
# sol3 = [2,4,1,7,5,3,6,0] # Returns 8
# sol4 = [3,5,0,4,1,7,2,6] # Returns 8
# sol5 = [1,5,0,6,3,7,2,4] # Returns 8
# sol6 = [5,0,4,1,7,2,6,3] # Returns 8
# sol7 = [5,2,6,1,7,4,0,3] # Returns 8
# sol8 = [4,1,7,0,3,6,2,5] # Returns 8
# sol9 = [4,1,5,0,6,3,7,2] # Returns 8
# sol10= [7,1,3,0,6,4,2,5] # Returns 8
# sol11= [2,5,7,1,3,0,6,4] # Returns 8
# sol12= [2,4,6,0,3,1,7,5] # Returns 8