import LogicFn
def minimax(gameArr,maxPlayer,depth):
    eval =  LogicFn.is_game_over(gameArr)[0]
    if eval ==3:
        return (gameArr, 1)
    elif eval == -3:
        return  (gameArr,-1)
    elif eval == 0 :
        return (gameArr, 0)
    elif depth == 0:
        return (gameArr,LogicFn.eval(gameArr))
    else:
        if maxPlayer :
            possible_moves_with_rating=[]
            possible_moves = LogicFn.possible_moves(gameArr,maxPlayer)
            for array in possible_moves: 
                possible_moves_with_rating.append((array,minimax(array,not maxPlayer,depth-1)[1]))
            sorted_arrs = sorted(possible_moves_with_rating,key=lambda x:x[1],reverse=True)
            return sorted_arrs[0]
        else:
            possible_moves_with_rating=[]
            possible_moves = LogicFn.possible_moves(gameArr,maxPlayer)
            for array in possible_moves: 
                possible_moves_with_rating.append((array,minimax(array,not maxPlayer,depth-1)[1]))
            sorted_arrs = sorted(possible_moves_with_rating,key=lambda x:x[1])
            return sorted_arrs[0]


def minimax_alphaBeta(gameArr,maxPlayer,alpha,beta):
    eval =  LogicFn.is_game_over(gameArr)[0]
    if eval ==3:
        return (gameArr, 1)
    elif eval == -3:
        return  (gameArr,-1)
    elif eval == 0 :
        return (gameArr, 0)
    else:
        if maxPlayer :

            possible_moves_with_rating=[]
            possible_moves = LogicFn.possible_moves(gameArr,maxPlayer)

            for array in possible_moves: 
                rating = minimax_alphaBeta(array,not maxPlayer,alpha,beta)
                if rating[1] > alpha: 
                    alpha = rating[1]
                if rating[1] > beta :
                    return rating
                possible_moves_with_rating.append((array,rating[1]))
            sorted_arrs = sorted(possible_moves_with_rating,key=lambda x:x[1],reverse=True)
            return sorted_arrs[0]
        else:
            possible_moves_with_rating=[]
            possible_moves = LogicFn.possible_moves(gameArr,maxPlayer)
            for array in possible_moves:
                rating = minimax_alphaBeta(array,not maxPlayer,alpha,beta)
                if rating[1] < beta: 
                    beta = rating[1]
                if rating[1] < alpha :
                    return rating 
                possible_moves_with_rating.append((array,rating[1]))
            sorted_arrs = sorted(possible_moves_with_rating,key=lambda x:x[1])
            return sorted_arrs[0]

g = [[-1,1,-1],[0,1,-0],[-0,-1,-1]]
LogicFn.print_matrix(minimax(g,True,5)[0]) 
# print(minimax(g,True,5)[1])

# print(LogicFn.is_game_over(g))        