#sudokuSolver


def findEmpty(board): 

    for x in range(9):
        for y in range(9):
            if board[x][y] == -1:
                return x,y
    
    return None, None


def isValid(board, x, y, guess):

    #arr for column
    column = [board[i][y] for i in range(9)]

    #arr for square
    tmpX = (x // 3) * 3
    tmpY = (x // 3 ) * 3
    square = []

    for x in range (tmpX, tmpX + 3):
        for y in range (tmpY, tmpY + 3):
            square.append(board [x][y])

    #checks row, column, & box
    if guess in board[x]:
        return False
    elif guess in column:
        return False
    elif guess in square:
        return False
    else:
        return True



def solve(board):

    x,y = findEmpty(board)

    if (x is None and y is None):
        return True
    
    for guess in range(1,10):
        if (isValid(board, x, y, guess)):
            board[x][y] = guess

            if solve(board):
                return True

        board[x][y] = -1

    return False