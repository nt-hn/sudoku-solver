from components.visualize_board import *
from components.find_empty_square import *
from components.grid_checker import *


#sample board 

board = [
    [0,7,0,0,2,0,9,0,0],
    [0,4,0,8,0,6,0,0,0],
    [0,1,2,0,0,0,3,0,0],
    [0,0,0,0,0,0,8,7,0],
    [0,6,0,9,7,2,0,5,0],
    [0,2,5,0,0,0,0,0,0],
    [0,0,1,0,0,0,2,9,0],
    [0,0,0,5,0,4,0,3,0],
    [0,0,7,0,6,0,0,1,0]
]

def solver(board):

    empty = empty_square(board)

    if not empty:
        return True
    else:
        row, column = empty

    for i in range(1,10):
        if checker(board, i, (row, column)):
            board[row][column] = i

            if solver(board):
                return True

            board[row][column] = 0

    return False

print('This is your original board: ')

visualize_board(board)

print(' - - - - - - - - - - - - - ')

solver(board)

print('This is your solved board: ')

visualize_board(board)
