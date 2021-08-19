def checker(board, value, position):

#the following checks the horizontal side
    for i in range(len(board[0])):
        if board[position[0]][i]==value and position[1] !=1:
            return False

#the following checks the vertical side
    for i in range(len(board)):
        if board[i][position[1]]==value and position[0]!=i:
            return False

#checks the 3x3 cube
    cube_x =position[1]//3
    cube_y =position[0]//3

    for i in range(cube_y*3, cube_y*3 +3):
        for j in range(cube_x*3, cube_x*3 +3):
            if board[i][j] == value and (i,j) != position:
                return False
                
    return True
