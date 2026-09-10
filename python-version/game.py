# ==========================================
# TIC TAC TOE
# Beginner Python Project
# ==========================================


# ------------------------------------------
# Display the Game Title
# ------------------------------------------

def display_title():
    print()
    print("=" * 45)
    print("              TIC TAC TOE")
    print("=" * 45)
    print()


# ------------------------------------------
# Display the Board
# ------------------------------------------

def display_board(board):
    print()
    print(f"       {board[0]}   |   {board[1]}   |   {board[2]}")
    print("     -------+-------+-------")
    print(f"       {board[3]}   |   {board[4]}   |   {board[5]}")
    print("     -------+-------+-------")
    print(f"       {board[6]}   |   {board[7]}   |   {board[8]}")
    print()


# ------------------------------------------
# Display Position Guide
# ------------------------------------------

def display_position_guide():
    print()
    print("Board Positions:")
    print()
    print("       1   |   2   |   3")
    print("     -------+-------+-------")
    print("       4   |   5   |   6")
    print("     -------+-------+-------")
    print("       7   |   8   |   9")
    print()


# ------------------------------------------
# Create a New Board
# ------------------------------------------

def create_board():
    return [" " for _ in range(9)]


# ------------------------------------------
# Get Player Names
# ------------------------------------------

def get_player_names():
    print("Enter Player Information")
    print("-" * 30)

    player_x = input("Player X name: ").strip()
    player_o = input("Player O name: ").strip()

    # Give default names if nothing was entered
    if player_x == "":
        player_x = "Player X"

    if player_o == "":
        player_o = "Player O"

    return player_x, player_o


# ------------------------------------------
# Display Current Scores
# ------------------------------------------

def display_scores(player_x, player_o, scores):
    print()
    print("=" * 45)
    print("                    SCORE")
    print("=" * 45)
    print(f"{player_x} (X): {scores['X']}")
    print(f"{player_o} (O): {scores['O']}")
    print(f"Draws:      {scores['Draws']}")
    print("=" * 45)
    print()


# ------------------------------------------
# Check if a Move is Valid
# ------------------------------------------

def is_valid_move(board, move):
    # Check if position is between 1 and 9
    if move < 1 or move > 9:
        return False

    # Convert player position to Python list index
    index = move - 1

    # Check if the position is empty
    if board[index] != " ":
        return False

    return True


# ------------------------------------------
# Get Player Move
# ------------------------------------------

def get_player_move(player_name, player_symbol, board):
    while True:

        print(f"{player_name} ({player_symbol})", end="")
        print(" - choose a position (1-9) or Q to quit:")

        choice = input("> ").strip().upper()

        # Allow player to quit
        if choice == "Q":
            return None

        # Check if the input is a number
        if not choice.isdigit():
            print()
            print("Invalid input.")
            print("Please enter a number from 1 to 9.")
            print()
            continue

        move = int(choice)

        # Check if the move is valid
        if not is_valid_move(board, move):

            if move < 1 or move > 9:
                print()
                print("Invalid position.")
                print("Please choose a number from 1 to 9.")
                print()
            else:
                print()
                print("That position is already taken.")
                print("Please choose another position.")
                print()

            continue

        return move


# ------------------------------------------
# Place Player Symbol on Board
# ------------------------------------------

def make_move(board, move, player_symbol):
    index = move - 1
    board[index] = player_symbol


# ------------------------------------------
# Check for a Winner
# ------------------------------------------

def check_winner(board, player_symbol):

    winning_combinations = [

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

    for first, second, third in winning_combinations:

        if (
            board[first] == player_symbol
            and board[second] == player_symbol
            and board[third] == player_symbol
        ):
            return True

    return False


# ------------------------------------------
# Check if Board is Full
# ------------------------------------------

def is_board_full(board):
    return " " not in board


# ------------------------------------------
# Display Winner Message
# ------------------------------------------

def display_winner(player_name, player_symbol):
    print()
    print("=" * 45)
    print(f"        {player_name} WINS!")
    print(f"        Congratulations! {player_symbol}!")
    print("=" * 45)
    print()


# ------------------------------------------
# Display Draw Message
# ------------------------------------------

def display_draw():
    print()
    print("=" * 45)
    print("              IT'S A DRAW!")
    print("=" * 45)
    print()


# ------------------------------------------
# Play One Game
# ------------------------------------------

def play_game(player_x, player_o):

    board = create_board()

    current_player = player_x
    current_symbol = "X"

    move_count = 0

    display_position_guide()

    while True:

        display_board(board)

        # Get player's move
        move = get_player_move(
            current_player,
            current_symbol,
            board
        )

        # Player chose to quit
        if move is None:
            print()
            print(f"{current_player} left the game.")
            print("Returning to the main menu...")
            print()
            return "quit"

        # Make the move
        make_move(
            board,
            move,
            current_symbol
        )

        move_count += 1

        # Check for winner
        if check_winner(board, current_symbol):

            display_board(board)

            display_winner(
                current_player,
                current_symbol
            )

            return current_symbol

        # Check for draw
        if is_board_full(board):

            display_board(board)

            display_draw()

            return "Draw"

        # Switch player
        if current_symbol == "X":

            current_symbol = "O"
            current_player = player_o

        else:

            current_symbol = "X"
            current_player = player_x


# ------------------------------------------
# Ask if Players Want to Play Again
# ------------------------------------------

def play_again():

    while True:

        print("Would you like to play again?")
        print("Y - Yes")
        print("N - No")

        choice = input("> ").strip().upper()

        if choice == "Y":
            return True

        if choice == "N":
            return False

        print()
        print("Please enter Y or N.")
        print()


# ------------------------------------------
# Main Menu
# ------------------------------------------

def display_menu():
    print()
    print("=" * 45)
    print("                MAIN MENU")
    print("=" * 45)
    print("1. Start Game")
    print("2. View Rules")
    print("3. View Scores")
    print("4. Change Player Names")
    print("5. Exit")
    print("=" * 45)


# ------------------------------------------
# Display Rules
# ------------------------------------------

def display_rules():

    print()
    print("=" * 45)
    print("                  RULES")
    print("=" * 45)

    print()
    print("1. Tic Tac Toe is played by two players.")
    print()
    print("2. Player X goes first.")
    print()
    print("3. Players take turns selecting an empty")
    print("   position on the board.")
    print()
    print("4. The first player to get three symbols")
    print("   in a row wins.")
    print()
    print("5. A player can win horizontally, vertically,")
    print("   or diagonally.")
    print()
    print("6. If all nine spaces are filled and nobody")
    print("   wins, the game ends in a draw.")
    print()

    print("=" * 45)
    print()


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    display_title()

    # Get player names
    player_x, player_o = get_player_names()

    # Create score system
    scores = {
        "X": 0,
        "O": 0,
        "Draws": 0
    }

    # Main program loop
    while True:

        display_menu()

        choice = input("Choose an option: ").strip()

        # ----------------------------------
        # Start Game
        # ----------------------------------

        if choice == "1":

            while True:

                result = play_game(
                    player_x,
                    player_o
                )

                # If player quit, return to menu
                if result == "quit":
                    break

                # Update score
                if result == "X":
                    scores["X"] += 1

                elif result == "O":
                    scores["O"] += 1

                elif result == "Draw":
                    scores["Draws"] += 1

                # Show updated scores
                display_scores(
                    player_x,
                    player_o,
                    scores
                )

                # Ask if players want another game
                if not play_again():
                    break

        # ----------------------------------
        # View Rules
        # ----------------------------------

        elif choice == "2":

            display_rules()

        # ----------------------------------
        # View Scores
        # ----------------------------------

        elif choice == "3":

            display_scores(
                player_x,
                player_o,
                scores
            )

        # ----------------------------------
        # Change Player Names
        # ----------------------------------

        elif choice == "4":

            player_x, player_o = get_player_names()

            print()
            print("Player names updated successfully.")
            print()

        # ----------------------------------
        # Exit
        # ----------------------------------

        elif choice == "5":

            print()
            print("=" * 45)
            print("        Thank you for playing!")
            print("             Goodbye!")
            print("=" * 45)
            print()

            break

        # ----------------------------------
        # Invalid Menu Option
        # ----------------------------------

        else:

            print()
            print("Invalid option.")
            print("Please choose a number from 1 to 5.")
            print()


# ------------------------------------------
# Run the Program
# ------------------------------------------

if __name__ == "__main__":
    main()
