def visualize_board(board):

    for i in range(len(board)):

        if i%3==0 and i !=0:
            print(' - - - - - - - - - - - - - ') 

        for j in range(len(board[0])):

            if j%3==0 and j!=0:
                print(' │ ', end="") # end makes sure they aer on the same line

            if j==8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end ="")

