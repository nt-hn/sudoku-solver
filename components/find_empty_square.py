def empty_square(board):

    for i in range(len(board)): 

        for j in range(len(board[0])):

            if board[i][j]==0:
                
                return(i,j)
    return None