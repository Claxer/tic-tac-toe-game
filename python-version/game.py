# ==========================================
# TIC TAC TOE
# Expanded Beginner Python Project
# ==========================================

import random
import time


# ==========================================
# Display Game Title
# ==========================================

def display_title():
    print()
    print("=" * 55)
    print("                 TIC TAC TOE")
    print("              Python Edition")
    print("=" * 55)
    print()


# ==========================================
# Create a New Board
# ==========================================

def create_board():
    return [" " for _ in range(9)]


# ==========================================
# Display the Board
# ==========================================

def display_board(board):
    print()
    print("                 BOARD")
    print()

    print(f"             {board[0]}   |   {board[1]}   |   {board[2]}")
    print("           -------+-------+-------")
    print(f"             {board[3]}   |   {board[4]}   |   {board[5]}")
    print("           -------+-------+-------")
    print(f"             {board[6]}   |   {board[7]}   |   {board[8]}")
    print()


# ==========================================
# Display Position Guide
# ==========================================

def display_position_guide():
    print()
    print("             POSITION GUIDE")
    print()

    print("               1   |   2   |   3")
    print("             -------+-------+-------")
    print("               4   |   5   |   6")
    print("             -------+-------+-------")
    print("               7   |   8   |   9")
    print()


# ==========================================
# Get Player Names
# ==========================================

def get_player_names():
    print()
    print("Enter Player Information")
    print("-" * 35)

    player_x = input("Player X name: ").strip()
    player_o = input("Player O name: ").strip()

    if player_x == "":
        player_x = "Player X"

    if player_o == "":
        player_o = "Player O"

    return player_x, player_o


# ==========================================
# Display Scores
# ==========================================

def display_scores(player_x, player_o, scores):
    total_games = scores["X"] + scores["O"] + scores["Draws"]

    print()
    print("=" * 55)
    print("                    SCOREBOARD")
    print("=" * 55)

    print(f"{player_x} (X): {scores['X']} wins")
    print(f"{player_o} (O): {scores['O']} wins")
    print(f"Draws:         {scores['Draws']}")
    print(f"Games Played:  {total_games}")

    if total_games > 0:
        x_percentage = (scores["X"] / total_games) * 100
        o_percentage = (scores["O"] / total_games) * 100
        draw_percentage = (scores["Draws"] / total_games) * 100

        print()
        print("Win Statistics")
        print("-" * 35)
        print(f"{player_x}: {x_percentage:.1f}%")
        print(f"{player_o}: {o_percentage:.1f}%")
        print(f"Draws:    {draw_percentage:.1f}%")

    print("=" * 55)
    print()


# ==========================================
# Display Detailed Statistics
# ==========================================

def display_statistics(player_x, player_o, scores, total_moves):

    total_games = scores["X"] + scores["O"] + scores["Draws"]

    print()
    print("=" * 55)
    print("                GAME STATISTICS")
    print("=" * 55)

    print(f"Total Games:       {total_games}")
    print(f"{player_x} Wins:      {scores['X']}")
    print(f"{player_o} Wins:      {scores['O']}")
    print(f"Draws:             {scores['Draws']}")
    print(f"Total Moves:       {total_moves}")

    if total_games > 0:
        average_moves = total_moves / total_games
        print(f"Average Moves:     {average_moves:.2f}")

    print("=" * 55)
    print()


# ==========================================
# Check Valid Move
# ==========================================

def is_valid_move(board, move):

    if move < 1 or move > 9:
        return False

    index = move - 1

    if board[index] != " ":
        return False

    return True


# ==========================================
# Get Available Moves
# ==========================================

def get_available_moves(board):

    available_moves = []

    for i in range(9):

        if board[i] == " ":
            available_moves.append(i + 1)

    return available_moves


# ==========================================
# Get Player Move
# ==========================================

def get_player_move(player_name, player_symbol, board):

    while True:

        print(f"{player_name} ({player_symbol})")
        print("Choose a position from 1-9")
        print("Enter Q to quit the current game.")

        choice = input("> ").strip().upper()

        if choice == "Q":
            return None

        if not choice.isdigit():

            print()
            print("Invalid input.")
            print("Please enter a number from 1 to 9.")
            print()
            continue

        move = int(choice)

        if not is_valid_move(board, move):

            if move < 1 or move > 9:

                print()
                print("Invalid position.")
                print("Choose a number from 1 to 9.")
                print()

            else:

                print()
                print("That position is already taken.")
                print("Choose another position.")
                print()

            continue

        return move


# ==========================================
# Make a Move
# ==========================================

def make_move(board, move, player_symbol):
    board[move - 1] = player_symbol


# ==========================================
# Winning Combinations
# ==========================================

def get_winning_combinations():

    return [

        # Rows
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        # Columns
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        # Diagonals
        (0, 4, 8),
        (2, 4, 6)
    ]


# ==========================================
# Check Winner
# ==========================================

def check_winner(board, player_symbol):

    winning_combinations = get_winning_combinations()

    for first, second, third in winning_combinations:

        if (
            board[first] == player_symbol
            and board[second] == player_symbol
            and board[third] == player_symbol
        ):
            return True

    return False


# ==========================================
# Find Winning Move
# ==========================================

def find_winning_move(board, symbol):

    available_moves = get_available_moves(board)

    for move in available_moves:

        test_board = board.copy()

        make_move(test_board, move, symbol)

        if check_winner(test_board, symbol):
            return move

    return None


# ==========================================
# Easy Computer Move
# ==========================================

def easy_computer_move(board):

    available_moves = get_available_moves(board)

    if available_moves:
        return random.choice(available_moves)

    return None


# ==========================================
# Medium Computer Move
# ==========================================

def medium_computer_move(board, computer_symbol, player_symbol):

    # First, try to win
    winning_move = find_winning_move(
        board,
        computer_symbol
    )

    if winning_move is not None:
        return winning_move

    # Then block the player
    blocking_move = find_winning_move(
        board,
        player_symbol
    )

    if blocking_move is not None:
        return blocking_move

    # Prefer center
    if board[4] == " ":
        return 5

    # Choose a corner
    corners = [1, 3, 7, 9]

    available_corners = [
        move for move in corners
        if move in get_available_moves(board)
    ]

    if available_corners:
        return random.choice(available_corners)

    # Otherwise random
    return easy_computer_move(board)


# ==========================================
# ADDED FEATURE
# TRUE HARD COMPUTER MOVE
# MINIMAX ALGORITHM
# ==========================================

def minimax(
    board,
    depth,
    is_maximizing,
    computer_symbol,
    player_symbol
):

    # Computer wins
    if check_winner(board, computer_symbol):
        return 10 - depth

    # Player wins
    if check_winner(board, player_symbol):
        return depth - 10

    # Draw
    if is_board_full(board):
        return 0

    # Computer's turn
    if is_maximizing:

        best_score = -1000

        for move in get_available_moves(board):

            make_move(
                board,
                move,
                computer_symbol
            )

            score = minimax(
                board,
                depth + 1,
                False,
                computer_symbol,
                player_symbol
            )

            board[move - 1] = " "

            best_score = max(
                best_score,
                score
            )

        return best_score

    # Player's turn
    else:

        best_score = 1000

        for move in get_available_moves(board):

            make_move(
                board,
                move,
                player_symbol
            )

            score = minimax(
                board,
                depth + 1,
                True,
                computer_symbol,
                player_symbol
            )

            board[move - 1] = " "

            best_score = min(
                best_score,
                score
            )

        return best_score


def hard_computer_move(
    board,
    computer_symbol,
    player_symbol
):

    best_score = -1000
    best_move = None

    for move in get_available_moves(board):

        make_move(
            board,
            move,
            computer_symbol
        )

        score = minimax(
            board,
            0,
            False,
            computer_symbol,
            player_symbol
        )

        board[move - 1] = " "

        if score > best_score:

            best_score = score
            best_move = move

    return best_move


# ==========================================
# Get Computer Move
# ==========================================

def get_computer_move(
    board,
    difficulty,
    computer_symbol,
    player_symbol
):

    if difficulty == "Easy":

        return easy_computer_move(board)

    elif difficulty == "Medium":

        return medium_computer_move(
            board,
            computer_symbol,
            player_symbol
        )

    elif difficulty == "Hard":

        return hard_computer_move(
            board,
            computer_symbol,
            player_symbol
        )

    return easy_computer_move(board)


# ==========================================
# Check Board Full
# ==========================================

def is_board_full(board):
    return " " not in board


# ==========================================
# Display Winner
# ==========================================

def display_winner(player_name, player_symbol):

    print()
    print("=" * 55)
    print(f"              {player_name} WINS!")
    print(f"                Symbol: {player_symbol}")
    print("=" * 55)
    print()


# ==========================================
# Display Draw
# ==========================================

def display_draw():

    print()
    print("=" * 55)
    print("                 IT'S A DRAW!")
    print("=" * 55)
    print()


# ==========================================
# Display Computer Move
# ==========================================

def display_computer_move(move):

    print()
    print("Computer is thinking...")
    time.sleep(0.7)
    print(f"Computer chose position {move}.")
    print()


# ==========================================
# Select Game Mode
# ==========================================

def select_game_mode():

    while True:

        print()
        print("=" * 55)
        print("                 GAME MODE")
        print("=" * 55)
        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. Back")
        print("=" * 55)

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":
            return "PvP"

        elif choice == "2":
            return "PvC"

        elif choice == "3":
            return None

        else:

            print()
            print("Invalid option.")
            print("Please choose 1, 2, or 3.")


# ==========================================
# Select Difficulty
# ==========================================

def select_difficulty():

    while True:

        print()
        print("=" * 55)
        print("              COMPUTER DIFFICULTY")
        print("=" * 55)
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("=" * 55)

        choice = input(
            "Choose difficulty: "
        ).strip()

        if choice == "1":
            return "Easy"

        elif choice == "2":
            return "Medium"

        elif choice == "3":
            return "Hard"

        else:

            print()
            print("Invalid option.")
            print("Please choose 1, 2, or 3.")


# ==========================================
# Select First Player
# ==========================================

def select_first_player():

    while True:

        print()
        print("=" * 55)
        print("               FIRST PLAYER")
        print("=" * 55)
        print("1. Player X")
        print("2. Player O")
        print("3. Random")
        print("=" * 55)

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":
            return "X"

        elif choice == "2":
            return "O"

        elif choice == "3":
            return random.choice(["X", "O"])

        else:

            print()
            print("Invalid option.")


# ==========================================
# ADDED FEATURE
# MOVE HISTORY
# ==========================================

def display_move_history(move_history):

    print()
    print("=" * 55)
    print("                  MOVE HISTORY")
    print("=" * 55)

    if not move_history:

        print("No moves have been made yet.")

    else:

        for number, move in enumerate(
            move_history,
            start=1
        ):

            print(
                f"{number}. "
                f"{move['player']} "
                f"({move['symbol']}) "
                f"- Position {move['position']}"
            )

    print("=" * 55)
    print()


# ==========================================
# ADDED FEATURE
# WINNING LINE
# ==========================================

def get_winning_line(board, symbol):

    for combination in get_winning_combinations():

        first, second, third = combination

        if (
            board[first] == symbol
            and board[second] == symbol
            and board[third] == symbol
        ):

            return combination

    return None


# ==========================================
# ADDED FEATURE
# DISPLAY WINNING LINE
# ==========================================

def display_winning_line(
    winning_line
):

    if winning_line is not None:

        positions = [
            position + 1
            for position in winning_line
        ]

        print(
            "Winning positions: "
            + ", ".join(
                map(str, positions)
            )
        )


# ==========================================
# ADDED FEATURE
# STREAK STATISTICS
# ==========================================

def update_streaks(
    statistics,
    winner
):

    if winner == "X":

        statistics["X_streak"] += 1
        statistics["O_streak"] = 0

        if (
            statistics["X_streak"]
            > statistics["X_best_streak"]
        ):

            statistics["X_best_streak"] = (
                statistics["X_streak"]
            )

    elif winner == "O":

        statistics["O_streak"] += 1
        statistics["X_streak"] = 0

        if (
            statistics["O_streak"]
            > statistics["O_best_streak"]
        ):

            statistics["O_best_streak"] = (
                statistics["O_streak"]
            )

    else:

        statistics["X_streak"] = 0
        statistics["O_streak"] = 0


# ==========================================
# ADDED FEATURE
# EXTENDED STATISTICS
# ==========================================

def display_extended_statistics(
    player_x,
    player_o,
    scores,
    statistics
):

    total_games = (
        scores["X"]
        + scores["O"]
        + scores["Draws"]
    )

    print()
    print("=" * 55)
    print("              EXTENDED STATISTICS")
    print("=" * 55)

    print()
    print(f"Total Games:       {total_games}")
    print(f"{player_x} Wins:      {scores['X']}")
    print(f"{player_o} Wins:      {scores['O']}")
    print(f"Draws:             {scores['Draws']}")

    print()
    print("MOVE STATISTICS")
    print("-" * 35)

    print(
        f"{player_x} Moves:      "
        f"{statistics['X_moves']}"
    )

    print(
        f"{player_o} Moves:      "
        f"{statistics['O_moves']}"
    )

    print(
        f"Total Moves:       "
        f"{statistics['total_moves']}"
    )

    print()
    print("STREAK STATISTICS")
    print("-" * 35)

    print(
        f"{player_x} Current Streak: "
        f"{statistics['X_streak']}"
    )

    print(
        f"{player_o} Current Streak: "
        f"{statistics['O_streak']}"
    )

    print(
        f"{player_x} Best Streak:    "
        f"{statistics['X_best_streak']}"
    )

    print(
        f"{player_o} Best Streak:    "
        f"{statistics['O_best_streak']}"
    )

    print()
    print(
        f"Games Quit:        "
        f"{statistics['games_quit']}"
    )

    if total_games > 0:

        average_moves = (
            statistics["total_moves"]
            / total_games
        )

        print(
            f"Average Moves:     "
            f"{average_moves:.2f}"
        )

    print("=" * 55)
    print()


# ==========================================
# ADDED FEATURE
# GAME COMMANDS
# ==========================================

def get_advanced_player_move(
    player_name,
    player_symbol,
    board,
    move_history
):

    while True:

        print(
            f"{player_name} ({player_symbol})"
        )

        print()
        print("Commands:")
        print("1-9 = Make a move")
        print("U   = Undo")
        print("H   = Move History")
        print("R   = Restart")
        print("Q   = Quit")

        choice = input("> ").strip().upper()

        if choice == "Q":

            return "quit"

        elif choice == "U":

            return "undo"

        elif choice == "H":

            display_move_history(
                move_history
            )

            continue

        elif choice == "R":

            return "restart"

        elif not choice.isdigit():

            print()
            print("Invalid input.")
            print()

            continue

        move = int(choice)

        if not is_valid_move(
            board,
            move
        ):

            if move < 1 or move > 9:

                print()
                print(
                    "Choose a number from 1 to 9."
                )

            else:

                print()
                print(
                    "That position is already taken."
                )

            continue

        return move


# ==========================================
# ADDED FEATURE
# UNDO MOVE
# ==========================================

def undo_last_move(
    board,
    move_history,
    mode
):

    if not move_history:

        print()
        print(
            "There are no moves to undo."
        )

        return False

    # Player vs Player
    if mode == "PvP":

        last_move = move_history.pop()

        undo_position = (
            last_move["position"]
        )

        board[undo_position - 1] = " "

        print()
        print(
            "Last move has been undone."
        )

        return True

    # Player vs Computer
    else:

        # Remove player's and computer's
        # most recent moves
        moves_to_remove = min(
            2,
            len(move_history)
        )

        for _ in range(
            moves_to_remove
        ):

            last_move = move_history.pop()

            undo_position = (
                last_move["position"]
            )

            board[
                undo_position - 1
            ] = " "

        print()
        print(
            "Last turn has been undone."
        )

        return True


# ==========================================
# ADDED FEATURE
# ABOUT GAME
# ==========================================

def display_about():

    print()
    print("=" * 55)
    print("                    ABOUT GAME")
    print("=" * 55)

    print()
    print("TIC TAC TOE")
    print("Python Edition")

    print()
    print("This project is a terminal-based")
    print("Tic Tac Toe game made with Python.")

    print()
    print("Features include:")

    print("- Player vs Player")
    print("- Player vs Computer")
    print("- Easy, Medium and Hard AI")
    print("- Minimax algorithm")
    print("- Score tracking")
    print("- Statistics")
    print("- Win streaks")
    print("- Move history")
    print("- Undo")
    print("- Restart")
    print("- Rules and instructions")

    print()
    print("Python concepts used:")

    print("- Functions")
    print("- Lists")
    print("- Dictionaries")
    print("- Loops")
    print("- Conditions")
    print("- Random module")
    print("- Recursion")
    print("- Algorithms")
    print("- Input validation")

    print()
    print("=" * 55)
    print()


# ==========================================
# Display Rules
# ==========================================

def display_rules():

    print()
    print("=" * 55)
    print("                     RULES")
    print("=" * 55)

    print()
    print("1. Tic Tac Toe is played on a 3x3 board.")
    print()
    print("2. Player X normally goes first.")
    print()
    print("3. Players take turns choosing an empty space.")
    print()
    print("4. The first player to get three symbols")
    print("   in a row wins.")
    print()
    print("5. A winning line can be:")
    print("   - Horizontal")
    print("   - Vertical")
    print("   - Diagonal")
    print()
    print("6. If all nine spaces are filled and nobody")
    print("   wins, the game ends in a draw.")
    print()
    print("7. Enter Q during a player's turn to quit")
    print("   the current game.")
    print()
    print("8. Enter U to undo your previous move.")
    print()
    print("9. Enter H to view the move history.")
    print()
    print("10. Enter R to restart the current game.")

    print()
    print("=" * 55)
    print()


# ==========================================
# How To Play
# ==========================================

def display_how_to_play():

    print()
    print("=" * 55)
    print("                 HOW TO PLAY")
    print("=" * 55)

    print()
    print("The board uses numbers from 1 to 9.")
    print()

    print("Example:")
    print()

    print("              1   |   2   |   3")
    print("            -------+-------+-------")
    print("              4   |   5   |   6")
    print("            -------+-------+-------")
    print("              7   |   8   |   9")

    print()

    print("To place your symbol, type the number")
    print("of the position you want.")

    print()
    print("Example:")
    print("> 5")

    print()
    print("Your symbol will be placed in the center.")

    print()
    print("Extra commands:")
    print("U = Undo")
    print("H = Move History")
    print("R = Restart")
    print("Q = Quit")

    print()
    print("The objective is to create a line")
    print("of three of your symbols.")

    print()
    print("=" * 55)
    print()


# ==========================================
# ADDED FEATURE
# MOVE GUIDE
# ==========================================

def display_move_guide():

    print()
    print("=" * 55)
    print("                  MOVE GUIDE")
    print("=" * 55)

    print()

    print("                      1   |   2   |   3")
    print("                    -------+-------+-------")
    print("                      4   |   5   |   6")
    print("                    -------+-------+-------")
    print("                      7   |   8   |   9")

    print()

    print("Center position: 5")
    print("Corners: 1, 3, 7, 9")
    print("Sides: 2, 4, 6, 8")

    print()
    print("=" * 55)
    print()


# ==========================================
# Play One Game
# ==========================================

def play_game(
    player_x,
    player_o,
    mode,
    difficulty=None,
    first_player="X"
):

    board = create_board()

    move_count = 0

    # ======================================
    # ADDED FEATURE
    # MOVE HISTORY
    # ======================================

    move_history = []

    # ======================================
    # ADDED FEATURE
    # TRACK CURRENT TURN
    # ======================================

    current_symbol = first_player

    if first_player == "X":

        current_player = player_x

    else:

        if mode == "PvC":
            current_player = "Computer"
        else:
            current_player = player_o

    display_position_guide()

    while True:

        print()

        # ==================================
        # DISPLAY BOARD
        # ==================================

        display_board(board)

        print(
            f"Moves made: {move_count}"
        )

        print()

        # ==================================
        # PLAYER VS COMPUTER
        # ==================================

        if (
            mode == "PvC"
            and current_symbol == "O"
        ):

            move = get_computer_move(
                board,
                difficulty,
                "O",
                "X"
            )

            display_computer_move(move)

        else:

            # ==================================
            # ADDED FEATURE
            # ADVANCED PLAYER INPUT
            # ==================================

            move = get_advanced_player_move(
                current_player,
                current_symbol,
                board,
                move_history
            )

        # ==================================
        # QUIT GAME
        # ==================================

        if move == "quit":

            print()
            print(
                f"{current_player} left the game."
            )

            print(
                "Returning to the main menu..."
            )

            print()

            return "quit", move_count

        # ==================================
        # RESTART GAME
        # ==================================

        if move == "restart":

            confirm = input(
                "Restart this game? (Y/N): "
            ).strip().upper()

            if confirm == "Y":

                print()
                print(
                    "Restarting game..."
                )

                time.sleep(0.7)

                return "restart", move_count

            continue

        # ==================================
        # UNDO MOVE
        # ==================================

        if move == "undo":

            if undo_last_move(
                board,
                move_history,
                mode
            ):

                move_count = len(
                    move_history
                )

                if mode == "PvC":

                    current_symbol = "X"
                    current_player = player_x

                else:

                    if move_count % 2 == 0:

                        current_symbol = first_player

                    else:

                        if first_player == "X":
                            current_symbol = "O"
                        else:
                            current_symbol = "X"

                    if current_symbol == "X":
                        current_player = player_x
                    else:
                        current_player = player_o

            continue

        # ==================================
        # MAKE MOVE
        # ==================================

        make_move(
            board,
            move,
            current_symbol
        )

        move_count += 1

        # ==================================
        # ADD MOVE TO HISTORY
        # ==================================

        move_history.append(
            {
                "player": current_player,
                "symbol": current_symbol,
                "position": move
            }
        )

        # ==================================
        # CHECK WINNER
        # ==================================

        if check_winner(
            board,
            current_symbol
        ):

            display_board(board)

            display_winner(
                current_player,
                current_symbol
            )

            # ==================================
            # ADDED FEATURE
            # SHOW WINNING LINE
            # ==================================

            winning_line = get_winning_line(
                board,
                current_symbol
            )

            display_winning_line(
                winning_line
            )

            print()
            print("Final Move History:")

            display_move_history(
                move_history
            )

            return current_symbol, move_count

        # ==================================
        # CHECK DRAW
        # ==================================

        if is_board_full(board):

            display_board(board)

            display_draw()

            print("Final Move History:")

            display_move_history(
                move_history
            )

            return "Draw", move_count

        # ==================================
        # SWITCH PLAYER
        # ==================================

        if current_symbol == "X":

            current_symbol = "O"

            if mode == "PvC":

                current_player = "Computer"

            else:

                current_player = player_o

        else:

            current_symbol = "X"
            current_player = player_x


# ==========================================
# Play Again
# ==========================================

def play_again():

    while True:

        print("Would you like to play again?")
        print("Y - Yes")
        print("N - No")

        choice = input(
            "> "
        ).strip().upper()

        if choice == "Y":
            return True

        elif choice == "N":
            return False

        else:

            print()
            print("Please enter Y or N.")
            print()


# ==========================================
# Reset Scores
# ==========================================

def reset_scores(scores):

    scores["X"] = 0
    scores["O"] = 0
    scores["Draws"] = 0

    print()
    print("All scores have been reset.")
    print()


# ==========================================
# ADDED FEATURE
# RESET EXTENDED STATISTICS
# ==========================================

def reset_extended_statistics(
    statistics
):

    statistics["X_moves"] = 0
    statistics["O_moves"] = 0
    statistics["total_moves"] = 0

    statistics["X_streak"] = 0
    statistics["O_streak"] = 0

    statistics["X_best_streak"] = 0
    statistics["O_best_streak"] = 0

    statistics["games_quit"] = 0


# ==========================================
# Main Menu
# ==========================================

def display_menu():

    print()
    print("=" * 55)
    print("                    MAIN MENU")
    print("=" * 55)

    print("1. Start Game")
    print("2. View Rules")
    print("3. How To Play")
    print("4. View Scores")
    print("5. View Statistics")
    print("6. Change Player Names")
    print("7. Reset Scores")

    # ======================================
    # ADDED MENU FEATURES
    # ======================================

    print("8. View Move Guide")
    print("9. View About")
    print("10. View Extended Statistics")
    print("11. Exit")

    print("=" * 55)


# ==========================================
# Main Program
# ==========================================

def original_main():

    display_title()

    # ======================================
    # Player Information
    # ======================================

    player_x, player_o = get_player_names()

    # ======================================
    # Score System
    # ======================================

    scores = {
        "X": 0,
        "O": 0,
        "Draws": 0
    }

    # ======================================
    # ADDED FEATURE
    # STATISTICS SYSTEM
    # ======================================

    statistics = {

        "X_moves": 0,
        "O_moves": 0,

        "total_moves": 0,

        "X_streak": 0,
        "O_streak": 0,

        "X_best_streak": 0,
        "O_best_streak": 0,

        "games_quit": 0
    }

    total_moves = 0

    # ======================================
    # ADDED FEATURE
    # ROUND NUMBER
    # ======================================

    round_number = 1

    # ======================================
    # Main Program Loop
    # ======================================

    while True:

        display_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        # ==================================
        # Start Game
        # ==================================

        if choice == "1":

            mode = select_game_mode()

            if mode is None:
                continue

            difficulty = None

            if mode == "PvC":

                difficulty = select_difficulty()

                print()
                print(
                    f"Difficulty selected: "
                    f"{difficulty}"
                )

            first_player = select_first_player()

            if first_player == "X":

                print()
                print(
                    f"{player_x} will go first."
                )

            else:

                print()
                print(
                    f"{player_o} will go first."
                )

            while True:

                result, moves = play_game(
                    player_x,
                    player_o,
                    mode,
                    difficulty,
                    first_player
                )

                # ==================================
                # ADDED FEATURE
                # RESTART
                # ==================================

                if result == "restart":

                    print()
                    print(
                        "Starting a new game..."
                    )

                    time.sleep(0.7)

                    continue

                # ==================================
                # Player Quit
                # ==================================

                if result == "quit":

                    statistics[
                        "games_quit"
                    ] += 1

                    break

                # ==================================
                # UPDATE TOTAL MOVES
                # ==================================

                total_moves += moves

                statistics[
                    "total_moves"
                ] += moves

                # ==================================
                # SCORE UPDATE
                # ==================================

                if result == "X":

                    scores["X"] += 1

                    update_streaks(
                        statistics,
                        "X"
                    )

                elif result == "O":

                    scores["O"] += 1

                    update_streaks(
                        statistics,
                        "O"
                    )

                elif result == "Draw":

                    scores["Draws"] += 1

                    update_streaks(
                        statistics,
                        "Draw"
                    )

                # ==================================
                # MOVE STATISTICS
                # ==================================

                if result == "X":

                    statistics[
                        "X_moves"
                    ] += moves

                elif result == "O":

                    statistics[
                        "O_moves"
                    ] += moves

                # ==================================
                # ROUND NUMBER
                # ==================================

                round_number += 1

                # ==================================
                # SHOW SCORE
                # ==================================

                display_scores(
                    player_x,
                    player_o,
                    scores
                )

                # ==================================
                # PLAY AGAIN
                # ==================================

                if not play_again():

                    break

                # ==================================
                # RANDOMIZE FIRST PLAYER
                # ==================================

                first_player = random.choice(
                    ["X", "O"]
                )

        # ==================================
        # View Rules
        # ==================================

        elif choice == "2":

            display_rules()

        # ==================================
        # How To Play
        # ==================================

        elif choice == "3":

            display_how_to_play()

        # ==================================
        # View Scores
        # ==================================

        elif choice == "4":

            display_scores(
                player_x,
                player_o,
                scores
            )

        # ==================================
        # View Statistics
        # ==================================

        elif choice == "5":

            display_statistics(
                player_x,
                player_o,
                scores,
                total_moves
            )

        # ==================================
        # Change Names
        # ==================================

        elif choice == "6":

            player_x, player_o = (
                get_player_names()
            )

            print()
            print(
                "Player names updated successfully."
            )
            print()

        # ==================================
        # Reset Scores
        # ==================================

        elif choice == "7":

            confirm = input(
                "Are you sure you want "
                "to reset scores? (Y/N): "
            ).strip().upper()

            if confirm == "Y":

                reset_scores(
                    scores
                )

                reset_extended_statistics(
                    statistics
                )

                total_moves = 0

                round_number = 1

            else:

                print()
                print(
                    "Reset cancelled."
                )
                print()

        # ==================================
        # ADDED FEATURE
        # MOVE GUIDE
        # ==================================

        elif choice == "8":

            display_move_guide()

        # ==================================
        # ADDED FEATURE
        # ABOUT
        # ==================================

        elif choice == "9":

            display_about()

        # ==================================
        # ADDED FEATURE
        # EXTENDED STATISTICS
        # ==================================

        elif choice == "10":

            display_extended_statistics(
                player_x,
                player_o,
                scores,
                statistics
            )

        # ==================================
        # Exit
        # ==================================

        elif choice == "11":

            print()
            print("=" * 55)
            print("             THANK YOU FOR PLAYING!")
            print()
            print("                  TIC TAC TOE")
            print("=" * 55)
            print()

            break

        # ==================================
        # Invalid Option
        # ==================================

        else:

            print()
            print("Invalid option.")
            print(
                "Please choose a number from 1 to 11."
            )
            print()


# ==========================================
# Run Program
# ==========================================



# ==========================================================
# NEW FEATURES - GAME CENTER
# These features are added without removing the original
# Tic Tac Toe functions above.
# ==========================================================

import json
from datetime import datetime


SAVE_FILE = "tic_tac_toe_data.json"


def create_game_data():
    """Create data used by the new Game Center."""
    return {
        "match_history": [],
        "achievements": [],
        "challenges_completed": [],
        "total_play_time": 0,
        "fastest_win": None,
        "longest_game": 0
    }


def load_game_data():
    """Load Game Center data from a file."""
    data = create_game_data()

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            saved_data = json.load(file)

        for key in data:
            if key in saved_data:
                data[key] = saved_data[key]

    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return data


def save_game_data(data):
    """Save Game Center data to a file."""
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError:
        print("Could not save Game Center data.")


def get_win_rate(player_symbol, scores):
    """Calculate a player's win percentage."""
    total_games = (
        scores["X"]
        + scores["O"]
        + scores["Draws"]
    )

    if total_games == 0:
        return 0

    return (scores[player_symbol] / total_games) * 100


def display_game_center_stats(player_x, player_o, scores, statistics, data):
    """Display a larger statistics dashboard."""
    total_games = (
        scores["X"]
        + scores["O"]
        + scores["Draws"]
    )

    print()
    print("=" * 65)
    print("                    GAME CENTER")
    print("=" * 65)

    print()
    print("PLAYER PERFORMANCE")
    print("-" * 65)

    print(f"{player_x} (X)")
    print(f"  Wins:       {scores['X']}")
    print(f"  Win Rate:   {get_win_rate('X', scores):.1f}%")
    print(f"  Best Streak:{statistics['X_best_streak']}")

    print()
    print(f"{player_o} (O)")
    print(f"  Wins:       {scores['O']}")
    print(f"  Win Rate:   {get_win_rate('O', scores):.1f}%")
    print(f"  Best Streak:{statistics['O_best_streak']}")

    print()
    print("OVERALL")
    print("-" * 65)
    print(f"Games Played:       {total_games}")
    print(f"Total Moves:        {statistics['total_moves']}")
    print(f"Games Quit:         {statistics['games_quit']}")
    print(f"Achievements:       {len(data['achievements'])}")
    print(f"Challenges:         {len(data['challenges_completed'])}")

    if data["fastest_win"] is not None:
        print(f"Fastest Win:        {data['fastest_win']:.2f} seconds")

    if data["longest_game"] > 0:
        print(f"Longest Game:       {data['longest_game']} moves")

    print("=" * 65)
    print()


def display_achievements(data):
    """Display achievement progress."""
    achievements = [
        ("FIRST_WIN", "First Victory", "Win your first game."),
        ("THREE_WINS", "Triple Threat", "Win 3 games."),
        ("FIVE_WINS", "Five Star Player", "Win 5 games."),
        ("TEN_GAMES", "Veteran", "Play 10 completed games."),
        ("STREAK_3", "On Fire", "Reach a 3-game win streak."),
        ("STREAK_5", "Unstoppable", "Reach a 5-game win streak."),
        ("HARD_AI", "AI Slayer", "Defeat the Hard computer."),
        ("PERFECT_GAME", "Perfect Game", "Win without letting the opponent win."),
        ("QUICK_WIN", "Speed Player", "Win a game in 5 moves or fewer.")
    ]

    print()
    print("=" * 65)
    print("                    ACHIEVEMENTS")
    print("=" * 65)

    unlocked = set(data["achievements"])

    for code, name, description in achievements:
        if code in unlocked:
            status = "[UNLOCKED]"
        else:
            status = "[LOCKED]  "

        print()
        print(f"{status} {name}")
        print(f"          {description}")

    print()
    print(f"Unlocked: {len(unlocked)}/{len(achievements)}")
    print("=" * 65)
    print()


def unlock_achievement(data, code, name):
    """Unlock an achievement if it has not already been unlocked."""
    if code not in data["achievements"]:
        data["achievements"].append(code)

        print()
        print("=" * 65)
        print("                 ACHIEVEMENT UNLOCKED!")
        print("=" * 65)
        print()
        print(f"                    {name}")
        print()
        print("=" * 65)
        print()

        return True

    return False


def check_achievements(
    data,
    scores,
    statistics,
    result,
    moves,
    difficulty=None,
    total_games=0,
    elapsed_time=None
):
    """Check whether the latest game unlocked achievements."""
    changed = False

    if result in ("X", "O"):
        winner_wins = scores[result]

        if winner_wins >= 1:
            changed |= unlock_achievement(
                data,
                "FIRST_WIN",
                "First Victory"
            )

        if winner_wins >= 3:
            changed |= unlock_achievement(
                data,
                "THREE_WINS",
                "Triple Threat"
            )

        if winner_wins >= 5:
            changed |= unlock_achievement(
                data,
                "FIVE_WINS",
                "Five Star Player"
            )

        if moves <= 5:
            changed |= unlock_achievement(
                data,
                "QUICK_WIN",
                "Speed Player"
            )

        if statistics[f"{result}_best_streak"] >= 3:
            changed |= unlock_achievement(
                data,
                "STREAK_3",
                "On Fire"
            )

        if statistics[f"{result}_best_streak"] >= 5:
            changed |= unlock_achievement(
                data,
                "STREAK_5",
                "Unstoppable"
            )

        if moves == 5:
            changed |= unlock_achievement(
                data,
                "PERFECT_GAME",
                "Perfect Game"
            )

        if difficulty == "Hard" and result == "X":
            changed |= unlock_achievement(
                data,
                "HARD_AI",
                "AI Slayer"
            )

    if total_games >= 10:
        changed |= unlock_achievement(
            data,
            "TEN_GAMES",
            "Veteran"
        )

    if changed:
        save_game_data(data)


def display_challenges(data):
    """Display available challenges."""
    challenges = [
        (
            "WIN_5_MOVES",
            "Speed Challenge",
            "Win a game in 5 moves or fewer."
        ),
        (
            "WIN_DIAGONAL",
            "Diagonal Master",
            "Win using a diagonal."
        ),
        (
            "WIN_CENTER",
            "Center Control",
            "Win a game after using position 5."
        ),
        (
            "NO_CENTER",
            "Outside the Box",
            "Win without using position 5."
        ),
        (
            "BEAT_HARD",
            "Hard Mode Champion",
            "Defeat the Hard AI."
        ),
        (
            "WIN_STREAK_3",
            "Three in a Row",
            "Reach a 3-game winning streak."
        )
    ]

    print()
    print("=" * 65)
    print("                      CHALLENGES")
    print("=" * 65)

    completed = set(data["challenges_completed"])

    for code, name, description in challenges:
        status = "[DONE]" if code in completed else "[ ]"

        print()
        print(f"{status} {name}")
        print(f"     {description}")

    print()
    print(
        f"Completed: {len(completed)}/{len(challenges)}"
    )
    print("=" * 65)
    print()


def complete_challenge(data, code, name):
    """Mark a challenge as completed."""
    if code not in data["challenges_completed"]:
        data["challenges_completed"].append(code)

        print()
        print("=" * 65)
        print("                    CHALLENGE COMPLETE!")
        print("=" * 65)
        print()
        print(f"                    {name}")
        print()
        print("=" * 65)
        print()

        save_game_data(data)


def display_match_history(data):
    """Display previous completed games."""
    print()
    print("=" * 75)
    print("                       MATCH HISTORY")
    print("=" * 75)

    history = data["match_history"]

    if not history:
        print()
        print("No completed matches yet.")
    else:
        for match in history[-20:]:
            print()
            print(
                f"Game #{match['game_number']} | "
                f"{match['player_x']} vs {match['player_o']}"
            )
            print(
                f"Mode: {match['mode']} | "
                f"Result: {match['result']}"
            )
            print(
                f"Moves: {match['moves']} | "
                f"Time: {match['time']:.2f}s"
            )

            if match.get("difficulty"):
                print(
                    f"Difficulty: {match['difficulty']}"
                )

            print(
                f"Date: {match['date']}"
            )

    print()
    print("=" * 75)
    print()


def display_leaderboard(player_x, player_o, scores, statistics):
    """Display a simple leaderboard."""
    players = [
        {
            "name": player_x,
            "wins": scores["X"],
            "streak": statistics["X_best_streak"]
        },
        {
            "name": player_o,
            "wins": scores["O"],
            "streak": statistics["O_best_streak"]
        }
    ]

    players.sort(
        key=lambda player: (
            player["wins"],
            player["streak"]
        ),
        reverse=True
    )

    print()
    print("=" * 65)
    print("                       LEADERBOARD")
    print("=" * 65)

    print()
    print(
        f"{'Rank':<8}"
        f"{'Player':<25}"
        f"{'Wins':<10}"
        f"{'Best Streak':<15}"
    )
    print("-" * 65)

    for index, player in enumerate(players, start=1):
        print(
            f"{index:<8}"
            f"{player['name']:<25}"
            f"{player['wins']:<10}"
            f"{player['streak']:<15}"
        )

    print("=" * 65)
    print()


def display_tournament_rules():
    """Explain tournament mode."""
    print()
    print("=" * 65)
    print("                    TOURNAMENT MODE")
    print("=" * 65)

    print()
    print("Tournament format:")
    print()
    print("1. Choose Best of 3, 5, or 7.")
    print("2. Each game is played normally.")
    print("3. The first player to reach the required")
    print("   number of wins becomes champion.")
    print("4. Draws do not count as a win.")
    print()
    print("This mode is best played with Player vs Player.")
    print()
    print("=" * 65)
    print()


def run_tournament(player_x, player_o):
    """Run a Best-of tournament using the original game system."""
    while True:
        print()
        print("=" * 65)
        print("                    TOURNAMENT MODE")
        print("=" * 65)
        print("1. Best of 3")
        print("2. Best of 5")
        print("3. Best of 7")
        print("4. Back")
        print("=" * 65)

        choice = input("Choose an option: ").strip()

        if choice == "4":
            return

        if choice == "1":
            games_needed = 2
        elif choice == "2":
            games_needed = 3
        elif choice == "3":
            games_needed = 4
        else:
            print("Invalid option.")
            continue

        tournament_x = 0
        tournament_o = 0
        tournament_draws = 0

        print()
        print(
            f"Starting tournament: first to "
            f"{games_needed} wins."
        )

        while (
            tournament_x < games_needed
            and tournament_o < games_needed
        ):
            result, moves = play_game(
                player_x,
                player_o,
                "PvP",
                None,
                random.choice(["X", "O"])
            )

            if result == "quit":
                print("Tournament ended.")
                return

            if result == "restart":
                continue

            if result == "X":
                tournament_x += 1
            elif result == "O":
                tournament_o += 1
            else:
                tournament_draws += 1

            print()
            print("-" * 65)
            print("TOURNAMENT SCORE")
            print("-" * 65)
            print(f"{player_x}: {tournament_x}")
            print(f"{player_o}: {tournament_o}")
            print(f"Draws: {tournament_draws}")
            print("-" * 65)

        print()
        print("=" * 65)
        print("                  TOURNAMENT COMPLETE")
        print("=" * 65)

        if tournament_x == games_needed:
            print()
            print(f"CHAMPION: {player_x}")
        else:
            print()
            print(f"CHAMPION: {player_o}")

        print()
        print("=" * 65)
        print()

        return


def display_game_center_menu():
    """Display the new Game Center menu."""
    print()
    print("=" * 65)
    print("                    GAME CENTER")
    print("=" * 65)
    print("1. Achievements")
    print("2. Challenges")
    print("3. Match History")
    print("4. Leaderboard")
    print("5. Advanced Statistics")
    print("6. Tournament Mode")
    print("7. Back")
    print("=" * 65)


def game_center(
    player_x,
    player_o,
    scores,
    statistics,
    data
):
    """Open the new Game Center."""
    while True:
        display_game_center_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_achievements(data)

        elif choice == "2":
            display_challenges(data)

        elif choice == "3":
            display_match_history(data)

        elif choice == "4":
            display_leaderboard(
                player_x,
                player_o,
                scores,
                statistics
            )

        elif choice == "5":
            display_game_center_stats(
                player_x,
                player_o,
                scores,
                statistics,
                data
            )

        elif choice == "6":
            run_tournament(
                player_x,
                player_o
            )

        elif choice == "7":
            return

        else:
            print()
            print("Invalid option.")
            print()


def update_new_feature_records(
    data,
    player_x,
    player_o,
    mode,
    difficulty,
    result,
    moves,
    elapsed_time
):
    """Save the completed game into the new systems."""
    if result in ("X", "O"):
        if result == "X":
            winner = player_x
        else:
            winner = player_o
    else:
        winner = "Draw"

    total_games = len(data["match_history"]) + 1

    if elapsed_time is None:
        elapsed_time = 0

    match = {
        "game_number": total_games,
        "player_x": player_x,
        "player_o": player_o,
        "mode": mode,
        "difficulty": difficulty,
        "result": winner,
        "moves": moves,
        "time": elapsed_time,
        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    data["match_history"].append(match)

    # Keep only the latest 100 matches.
    if len(data["match_history"]) > 100:
        data["match_history"] = data["match_history"][-100:]

    if result in ("X", "O"):
        if (
            data["fastest_win"] is None
            or elapsed_time < data["fastest_win"]
        ):
            data["fastest_win"] = elapsed_time

    if moves > data["longest_game"]:
        data["longest_game"] = moves

    save_game_data(data)


def check_new_challenges(
    data,
    result,
    moves,
    move_history,
    difficulty,
    statistics
):
    """Check the new challenge system."""
    if result not in ("X", "O"):
        return

    positions = [
        move["position"]
        for move in move_history
        if move["symbol"] == result
    ]

    if moves <= 5:
        complete_challenge(
            data,
            "WIN_5_MOVES",
            "Speed Challenge"
        )

    winning_line = get_winning_line(
        [
            result if position in positions else " "
            for position in range(1, 10)
        ],
        result
    )

    if winning_line is not None:
        if (
            set(winning_line) == {0, 4, 8}
            or set(winning_line) == {2, 4, 6}
        ):
            complete_challenge(
                data,
                "WIN_DIAGONAL",
                "Diagonal Master"
            )

    if 5 in positions:
        complete_challenge(
            data,
            "WIN_CENTER",
            "Center Control"
        )
    else:
        complete_challenge(
            data,
            "NO_CENTER",
            "Outside the Box"
        )

    if difficulty == "Hard" and result == "X":
        complete_challenge(
            data,
            "BEAT_HARD",
            "Hard Mode Champion"
        )

    if statistics[f"{result}_best_streak"] >= 3:
        complete_challenge(
            data,
            "WIN_STREAK_3",
            "Three in a Row"
        )


def play_game_with_timer(
    player_x,
    player_o,
    mode,
    difficulty,
    first_player
):
    """
    Wrapper around the original play_game function.

    The original game logic is still used. This wrapper adds
    timing and Game Center recording.
    """
    start_time = time.time()

    result, moves = play_game(
        player_x,
        player_o,
        mode,
        difficulty,
        first_player
    )

    elapsed_time = time.time() - start_time

    return result, moves, elapsed_time


def enhanced_main():
    """
    New launcher.

    All original game functions remain above.
    This launcher adds the Game Center features.
    """
    display_title()

    player_x, player_o = get_player_names()

    scores = {
        "X": 0,
        "O": 0,
        "Draws": 0
    }

    statistics = {
        "X_moves": 0,
        "O_moves": 0,
        "total_moves": 0,
        "X_streak": 0,
        "O_streak": 0,
        "X_best_streak": 0,
        "O_best_streak": 0,
        "games_quit": 0
    }

    total_moves = 0
    data = load_game_data()

    while True:
        display_menu()

        print("12. Game Center")

        print("=" * 55)

        choice = input(
            "Choose an option: "
        ).strip()

        if choice == "1":
            mode = select_game_mode()

            if mode is None:
                continue

            difficulty = None

            if mode == "PvC":
                difficulty = select_difficulty()

                print()
                print(
                    f"Difficulty selected: {difficulty}"
                )

            first_player = select_first_player()

            if first_player == "X":
                print()
                print(
                    f"{player_x} will go first."
                )
            else:
                print()
                print(
                    f"{player_o} will go first."
                )

            while True:
                result, moves, elapsed_time = (
                    play_game_with_timer(
                        player_x,
                        player_o,
                        mode,
                        difficulty,
                        first_player
                    )
                )

                if result == "restart":
                    print()
                    print("Starting a new game...")
                    time.sleep(0.7)
                    continue

                if result == "quit":
                    statistics["games_quit"] += 1
                    break

                total_moves += moves
                statistics["total_moves"] += moves

                if result == "X":
                    scores["X"] += 1

                    statistics["X_moves"] += moves

                    update_streaks(
                        statistics,
                        "X"
                    )

                elif result == "O":
                    scores["O"] += 1

                    statistics["O_moves"] += moves

                    update_streaks(
                        statistics,
                        "O"
                    )

                elif result == "Draw":
                    scores["Draws"] += 1

                    update_streaks(
                        statistics,
                        "Draw"
                    )

                update_new_feature_records(
                    data,
                    player_x,
                    player_o,
                    mode,
                    difficulty,
                    result,
                    moves,
                    elapsed_time
                )

                total_games = (
                    scores["X"]
                    + scores["O"]
                    + scores["Draws"]
                )

                check_achievements(
                    data,
                    scores,
                    statistics,
                    result,
                    moves,
                    difficulty,
                    total_games,
                    elapsed_time
                )

                # Recreate move history is not available after
                # play_game returns, so the main achievement
                # system handles the general achievements here.

                print()
                print(
                    f"Game time: {elapsed_time:.2f} seconds"
                )

                display_scores(
                    player_x,
                    player_o,
                    scores
                )

                if not play_again():
                    break

                first_player = random.choice(
                    ["X", "O"]
                )

        elif choice == "2":
            display_rules()

        elif choice == "3":
            display_how_to_play()

        elif choice == "4":
            display_scores(
                player_x,
                player_o,
                scores
            )

        elif choice == "5":
            display_statistics(
                player_x,
                player_o,
                scores,
                total_moves
            )

        elif choice == "6":
            player_x, player_o = get_player_names()

            print()
            print(
                "Player names updated successfully."
            )
            print()

        elif choice == "7":
            confirm = input(
                "Are you sure you want "
                "to reset scores? (Y/N): "
            ).strip().upper()

            if confirm == "Y":
                reset_scores(scores)
                reset_extended_statistics(
                    statistics
                )
                total_moves = 0

                print(
                    "Current session scores reset."
                )

            else:
                print()
                print("Reset cancelled.")
                print()

        elif choice == "8":
            display_move_guide()

        elif choice == "9":
            display_about()

        elif choice == "10":
            display_extended_statistics(
                player_x,
                player_o,
                scores,
                statistics
            )

        elif choice == "11":
            print()
            print("=" * 55)
            print("             THANK YOU FOR PLAYING!")
            print()
            print("                  TIC TAC TOE")
            print("=" * 55)
            print()

            save_game_data(data)
            break

        elif choice == "12":
            game_center(
                player_x,
                player_o,
                scores,
                statistics,
                data
            )

        else:
            print()
            print("Invalid option.")
            print(
                "Please choose a number from 1 to 12."
            )
            print()


# ==========================================================
# RUN ENHANCED PROGRAM
# ==========================================================

if __name__ == "__main__":
    enhanced_main()
