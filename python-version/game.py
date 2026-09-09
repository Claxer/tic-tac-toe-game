# Tic Tac Toe

board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(player):
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def board_full():
    return " " not in board


current_player = "X"

while True:
    print_board()

    move = int(input(f"Player {current_player}, choose a square (1-9): ")) - 1

    if move < 0 or move > 8:
        print("Invalid square!")
        continue

    if board[move] != " ":
        print("That square is already taken!")
        continue

    board[move] = current_player

    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    if board_full():
        print_board()
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"
