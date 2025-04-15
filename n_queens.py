# checa se C) valido coloar a rainha nessa posicao
def queen_is_valid(board, row, column):
    # checa se tem outra rainha na linha:
    for i in range(column):
        if board[row][i] == -1:
            return False
    # checa se tem outra rainha na coluna:
    for i in range(row):
        if board[i][column] == -1:
            return False
    # checa se tem outra rainha na diagonal principal:
    for i in range(min(row, column) + 1):
        if board[row - i][column - i] == -1:
            return False
    # checa se tem outra rainha na outra diagonal:
    for i in range(min(row, len(board) - 1 - column) + 1):
        if board[row - i][column + i] == -1:
            return False

    return True


# posicionar as rainhas, -1 = rainha
def position_queens(board, current_position):
    show_board(board)
    column = current_position % len(board)
    row = int((current_position - column) / len(board))

    print(f"row = {row}, column = {column}")

    if is_solution(board):
        return True

    if not queen_is_valid(board, row, column):
        return False

    while current_position < len(board) ** 2:
        board[row][column] = -1
        if position_queens(board, current_position):
            return True
        board[row][column] = 0
        current_position += 1

    return False


# funcao que checa se C) a solucao das n rainhas
def is_solution(board):
    queens = 0

    for row in board:
        for value in row:
            queens += value

    if queens == -len(board):
        return True

    return False


# mostra o tabuleiro
def show_board(board):
    print("------------------------")
    for row in range(len(board)):
        print(board[row])


board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

position_queens(board, 0)
show_board(board)
