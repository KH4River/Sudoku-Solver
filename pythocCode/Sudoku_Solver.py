# import random

def valid_numbers_check(sudoku_board,rows,column,number, bol):
    """
    Function declares the valid numbers checks the column row and quadrant of the position that gets passed and eliminates
    the numbers it finds from valid_numbers
    :param number: the number its checking at the moment
    :param sudoku_board: the array that represents the sudoku board
    :param column: the column its checking
    :param rows: the row its checking
    :param bol: if bol is True it skips the position of the number it needs to check so it doesn't give a false negative
    :return: true or false, depending on if the number is valid
    """

    for r in range(len(sudoku_board)): #checks if a number can be put in the column
        if bol and r==rows: continue
        if number==sudoku_board[r][column]:
            return False

    for c in range(len(sudoku_board)): #checks if a number can be put in the row
        if bol and c==column: continue
        if number == sudoku_board[rows][c]:
           return False

    #gets the current quadrant position by dividing the row and column by 3 and then multiplying it by 3 again
    quadrant_row=rows//3
    quadrant_column=column//3
    quadrant_column=quadrant_column*3
    quadrant_row=quadrant_row*3
    for x in range(quadrant_row,quadrant_row+3): #checks for all numbers in the quadrant
        for y in range(quadrant_column,quadrant_column+3):
            if bol and x==rows and y==column: continue
            if number==sudoku_board[x][y]:
                return False

    return True

def solve_sudoku_board(sudoku_board,i,j):
    """
    Function uses recursive backtracking to declare if the sudoku board is solved
    :param sudoku_board: the sudoku
    :param i: the rows in the sudoku board (starting from 0)
    :param j: the columns in the sudoku board (starting from 0)
    :return: true when the sudoku board is solved
    """
    if i==8 and j==9: #checks if the sudoku board is completed
        return True

    elif j == 9: #resets te column of the sudoku board to 0 whenever it goes out of range, adds 1 to the row
        j=0
        i+=1

    if sudoku_board[i][j]!=0: #checks if a number is already in the current position, calls the function again if it is
        # skipping the position in the process
        return solve_sudoku_board(sudoku_board,i,j+1)

    for x in range(1,10):#goes through numbers 1 to 9 checking if it can be put there if it can it goes deeper into
        # the recursion if it is not it goes to return false and declares the path as invalid
        if valid_numbers_check(sudoku_board,i,j,x,False):
            sudoku_board[i][j]=x
            if solve_sudoku_board(sudoku_board, i, j+1):
                return True
            sudoku_board[i][j] = 0

    return False

def check_rules(sudoku_board,i,j):
    if i == 8 and j == 9:
        return True

    elif j == 9:
        j = 0
        i += 1

    x = sudoku_board[i][j]
    if valid_numbers_check(sudoku_board, i, j, x, True):
        return check_rules(sudoku_board,i,j+1)
    return False


def show_sudoku_board(sudoku_board):
    """
    Function prints the sudoku board without a grid format
    :param sudoku_board: the board
    :return: nothing
    """
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[i])):
            if j != len(sudoku_board[i])-1:
                print(sudoku_board[i][j],end=" ")
            else:
                print(sudoku_board[i][j])


sudoku= ([5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9])

if solve_sudoku_board(sudoku,0,0):
    if check_rules(sudoku,0,0):
        show_sudoku_board(sudoku)
    else:print("el sudoku introduit no es valid")
else:
    print("No hi ha solució")
