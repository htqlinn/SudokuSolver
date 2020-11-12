#sudokuSolver


def findEmpty(board): 

    for x in range(9):
        for y in range(9):
            if board[x][y] == -1:
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

        board[x][y] = -1

    return False



if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve(example_board))
    print(example_board)