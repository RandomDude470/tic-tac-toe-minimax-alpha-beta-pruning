import copy
def eval(gameArr):
    c= 0
    d=0
    for i in range(3):
        temp = 0 
        for j in range(3):
            temp+= gameArr[i][j]
        if temp == 2:
            c+=temp
        elif temp == -2:
            d+= temp
    for i in range(3):
        temp = 0 
        for j in range(3):
            temp+= gameArr[j][i]
        if temp == 2:
            c+=temp
        elif temp == -2:
            d+= temp
    temp = 0
    for i in range(3):
        temp += gameArr[i][i]
    if temp == 2:
        c+=temp
    elif temp == -2:
        d+= temp
    temp = 0
    for i in range(3):
        temp += gameArr[i][2-i]
    if temp == 2:
        c+=temp
    elif temp == -2:
        d+= temp
    if c+d > 0:
        return 0.5
    elif c+d <0:
        return -0.5
    else:
        return 0
    
    



def is_game_over(gameArray) :
    """
    Checks if game is over. Returns a tuple in which the first member is either 3 for x -3 for o or 0 for draw, the second indicates on which line column or diagonal should a line be drawn
    """
    for i in range(3) :
        line_sum =0 
        for j in range(3) :
            line_sum += gameArray[i][j]
        if line_sum == -3 :
            return (-3,i)
        elif line_sum == 3:
            return (3,i)
    for i in range(3) :
        line_sum =0 
        for j in range(3) :
            line_sum += gameArray[j][i]
        if line_sum == -3 :
            return (-3,i+3)
        elif line_sum == 3:
            return (3,i+3)
    line_sum = 0
    #diagonal 1
    for i in range(3):
        line_sum += gameArray[i][i]
    if line_sum == 3 : 
        return (3,6)
    elif line_sum == -3:
        return (-3,6)
    
    line_sum = 0
    #daigonal 2
    for i in range(3):    
        line_sum += gameArray[i][2-i]
    if line_sum == 3 : 
        return (3 ,7) 
    elif line_sum == -3:
        return (-3,7)
    for i in range(3):
        for j in range(3):
            if gameArray[i][j] == 0:
                return (1,-1)
    return (0,-1 )    
def print_matrix(matrix):
    """
    Prints a matrix in a table 2D form rather than a list of lists
    """
    for row in matrix:
        for element in row:
            if element == -1:
                print(element, end='  ')
            else :
                print(element, end='   ')
        print()
def possible_moves(gameArray, Is_X):
    """
    Returns an array of all possible states that the game could be in in the next move
    """
    result = []
    moves_played = []

    if Is_X:
        for i in range(len(gameArray)):
            for j in range(len(gameArray[0])):
                if gameArray[i][j] == 0 and (i, j) not in moves_played:
                    moves_played.append((i, j))
                    newArr = copy.deepcopy(gameArray)
                    newArr[i][j] = 1
                    result.append(newArr)
    else : 
        for i in range(len(gameArray)):
            for j in range(len(gameArray[0])):
                if gameArray[i][j] == 0 and (i, j) not in moves_played:
                    moves_played.append((i, j))
                    newArr = copy.deepcopy(gameArray)
                    newArr[i][j] = -1
                    result.append(newArr)
                    
                  
    return result


# Testing
# g = [[1,1,-1],[0,1,1],[-1,0,-1]]
# a = possible_moves(g,True)
# n=[]
# for i in a: 
#     n.append((i,1))


# for i in n :
#     print_matrix(i[0])
#     print("--------")
#     print(i[1])
#     print("+++++++++++++++")
