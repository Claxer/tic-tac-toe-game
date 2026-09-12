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

def main():

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

if __name__ == "__main__":
    main()
