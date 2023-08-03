def board_print(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j], end=" ")
        print()


def solve(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def sudoku(board, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0
    if board[row][col] > 0:
        return sudoku(board, row, col + 1)
    for num in range(1, 10, 1):

        if solve(board, row, col, num):

            board[row][col] = num
            if sudoku(board, row, col + 1):
                return True
        board[row][col] = 0
    return False


if __name__ == '__main__':
    to_solve = [[7, 0, 0, 0, 0, 0, 0, 0, 9],
                [0, 4, 0, 0, 0, 0, 0, 6, 0],
                [0, 0, 6, 7, 0, 8, 4, 0, 0],
                [0, 5, 0, 9, 4, 2, 0, 8, 0],
                [0, 0, 0, 0, 6, 0, 0, 0, 0],
                [0, 9, 0, 1, 8, 7, 0, 3, 0],
                [0, 0, 1, 3, 0, 4, 2, 0, 0],
                [0, 2, 0, 0, 0, 0, 0, 4, 0],
                [3, 0, 0, 0, 0, 0, 0, 0, 6]]

    if sudoku(to_solve, 0, 0):
        board_print(to_solve)
    else:
        print("Error")


"""
    sample_to_solve =   [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""



