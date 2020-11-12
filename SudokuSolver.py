#sudokuSolver


def findEmpty(board): 

    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return x,y
    
    return None, None


def isValid(board, guess, x, y):

    row_vals = board[x]
    if guess in row_vals:
        return False

    col_vals = [board[i][y] for i in range(9)]
    if guess in col_vals:
        return False

    rows = (x // 3) * 3
    columns = (y // 3) * 3

    for r in range(rows, rows + 3):
        for c in range(columns, columns + 3):
            if board[r][c] == guess:
                return False

    return True



def solve(board):

    x,y = findEmpty(board)

    if (x is None and y is None):
        return True
    
    for guess in range(1,10):
        if (isValid(board, guess, x, y)):
            board[x][y] = guess

            if solve(board):
                return True

        board[x][y] = 0

    return False



# if __name__ == '__main__':
#     example_board = [
#         [7,8,0,4,0,0,1,2,0],
#         [6,0,0,0,7,5,0,0,9],
#         [0,0,0,6,0,1,0,7,8],
#         [0,0,7,0,4,0,2,6,0],
#         [0,0,1,0,5,0,9,3,0],
#         [9,0,4,0,6,0,0,0,5],
#         [0,7,0,3,0,0,0,1,2],
#         [1,2,0,0,0,7,4,0,0],
#         [0,4,9,2,0,6,0,0,7]
#     ]
#     print(solve(example_board))
#     print(example_board)