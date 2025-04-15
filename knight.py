# movimentos do cavalo
moves = [
    [-2, -1],
    [-2, 1],
    [-1, -2],
    [-1, 2],
    [1, -2],
    [1, 2],
    [2, -1],
    [2, 1]
]

# checa se é uma movimentacao valida
def position_is_valid(row, column):
    return row >= 0 and row < len(board) and column >= 0 and column < len(board) and board[row][column] == 0

def knight(board, row, column):
    show_board(board)
    
    if board[row][column] == len(board) ** 2 - len(board):
        return True
    
    for move in moves:
        row2 = row + move[0]
        column2 = column + move[1]
        if position_is_valid(row2, column2):
            board[row2][column2] = board[row][column] + 1
            if knight(board, row2, column2):
                return True
            board[row2][column2] = 0
    
    return False
    
# mostra o tabuleiro
def show_board(board):
    print("------------------------")
    for row in range(len(board)):
        print(board[row])


# resposta do algoritmo das n rainhas, -1 = raina nessa posicao
board = [
    [-1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -1],
    [0, 0, 0, 0, 0, -1, 0, 0],
    [0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -1, 0],
    [0, -1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0, 0, 0, 0]
]



for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == 0:
            board[i][j] = 1
            if knight(board, i, j):
                exit()
            board[i][j] = 0

