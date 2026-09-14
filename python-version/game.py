# ==========================================================
# TIC TAC TOE
# Game Center Edition
# Single-File Python Project
# ==========================================================

import random
import time
import json
from datetime import datetime


# ==========================================================
# SETTINGS
# ==========================================================

SAVE_FILE = "tic_tac_toe_data.json"


# ==========================================================
# DISPLAY GAME TITLE
# ==========================================================

def display_title():
    print()
    print("=" * 65)
    print("                    TIC TAC TOE")
    print("                 Python Game Center")
    print("=" * 65)
    print()


# ==========================================================
# CREATE BOARD
# ==========================================================

def create_board():
    return [" " for _ in range(9)]


# ==========================================================
# DISPLAY BOARD
# ==========================================================

def display_board(board):
    print()
    print("                         BOARD")
    print()

    print(f"                    {board[0]}   |   {board[1]}   |   {board[2]}")
    print("                  -------+-------+-------")
    print(f"                    {board[3]}   |   {board[4]}   |   {board[5]}")
    print("                  -------+-------+-------")
    print(f"                    {board[6]}   |   {board[7]}   |   {board[8]}")
    print()


# ==========================================================
# POSITION GUIDE
# ==========================================================

def display_position_guide():
    print()
    print("                    POSITION GUIDE")
    print()

    print("                      1   |   2   |   3")
    print("                    -------+-------+-------")
    print("                      4   |   5   |   6")
    print("                    -------+-------+-------")
    print("                      7   |   8   |   9")
    print()


# ==========================================================
# PLAYER NAMES
# ==========================================================

def get_player_names():
    print()
    print("=" * 65)
    print("                  PLAYER INFORMATION")
    print("=" * 65)

    player_x = input("Player X name: ").strip()
    player_o = input("Player O name: ").strip()

    if player_x == "":
        player_x = "Player X"

    if player_o == "":
        player_o = "Player O"

    return player_x, player_o


# ==========================================================
# CREATE SESSION STATISTICS
# ==========================================================

def create_statistics():

    return {
        "X_moves": 0,
        "O_moves": 0,
        "total_moves": 0,

        "X_streak": 0,
        "O_streak": 0,

        "X_best_streak": 0,
        "O_best_streak": 0,

        "games_quit": 0,

        "X_fastest_win": None,
        "O_fastest_win": None,

        "X_longest_win": 0,
        "O_longest_win": 0
    }


# ==========================================================
# CREATE SAVED GAME DATA
# ==========================================================

def create_game_data():

    return {
        "match_history": [],
        "achievements": [],
        "challenges_completed": [],

        "lifetime_games": 0,
        "lifetime_wins_x": 0,
        "lifetime_wins_o": 0,
        "lifetime_draws": 0,

        "total_play_time": 0,

        "fastest_win": None,
        "longest_game": 0,

        "total_moves": 0
    }


# ==========================================================
# LOAD SAVED DATA
# ==========================================================

def load_game_data():

    data = create_game_data()

    try:

        with open(
            SAVE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            saved_data = json.load(file)

        for key in data:

            if key in saved_data:
                data[key] = saved_data[key]

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        pass

    return data


# ==========================================================
# SAVE DATA
# ==========================================================

def save_game_data(data):

    try:

        with open(
            SAVE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    except OSError:

        print("Could not save game data.")


# ==========================================================
# SCOREBOARD
# ==========================================================

def display_scores(
    player_x,
    player_o,
    scores
):

    total_games = (
        scores["X"]
        + scores["O"]
        + scores["Draws"]
    )

    print()
    print("=" * 65)
    print("                       SCOREBOARD")
    print("=" * 65)

    print()
    print(f"{player_x} (X): {scores['X']} wins")
    print(f"{player_o} (O): {scores['O']} wins")
    print(f"Draws:         {scores['Draws']}")
    print(f"Games Played:  {total_games}")

    if total_games > 0:

        x_rate = (
            scores["X"]
            / total_games
        ) * 100

        o_rate = (
            scores["O"]
            / total_games
        ) * 100

        draw_rate = (
            scores["Draws"]
            / total_games
        ) * 100

        print()
        print("Win Statistics")
        print("-" * 40)

        print(
            f"{player_x}: "
            f"{x_rate:.1f}%"
        )

        print(
            f"{player_o}: "
            f"{o_rate:.1f}%"
        )

        print(
            f"Draws: "
            f"{draw_rate:.1f}%"
        )

    print("=" * 65)
    print()


# ==========================================================
# STATISTICS
# ==========================================================

def display_statistics(
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
    print("=" * 65)
    print("                   GAME STATISTICS")
    print("=" * 65)

    print()
    print(f"Total Games:       {total_games}")
    print(f"{player_x} Wins:      {scores['X']}")
    print(f"{player_o} Wins:      {scores['O']}")
    print(f"Draws:             {scores['Draws']}")

    print()
    print("MOVE STATISTICS")
    print("-" * 40)

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

    if total_games > 0:

        average = (
            statistics["total_moves"]
            / total_games
        )

        print(
            f"Average Moves:     "
            f"{average:.2f}"
        )

    print()
    print("STREAKS")
    print("-" * 40)

    print(
        f"{player_x} Current:     "
        f"{statistics['X_streak']}"
    )

    print(
        f"{player_o} Current:     "
        f"{statistics['O_streak']}"
    )

    print(
        f"{player_x} Best:        "
        f"{statistics['X_best_streak']}"
    )

    print(
        f"{player_o} Best:        "
        f"{statistics['O_best_streak']}"
    )

    print()
    print("OTHER")
    print("-" * 40)

    print(
        f"Games Quit:        "
        f"{statistics['games_quit']}"
    )

    print("=" * 65)
    print()


# ==========================================================
# VALID MOVE
# ==========================================================

def is_valid_move(board, move):

    if move < 1 or move > 9:
        return False

    return board[move - 1] == " "


# ==========================================================
# AVAILABLE MOVES
# ==========================================================

def get_available_moves(board):

    return [
        i + 1
        for i in range(9)
        if board[i] == " "
    ]


# ==========================================================
# BOARD FULL
# ==========================================================

def is_board_full(board):

    return " " not in board


# ==========================================================
# MAKE MOVE
# ==========================================================

def make_move(
    board,
    move,
    symbol
):

    board[move - 1] = symbol


# ==========================================================
# WINNING COMBINATIONS
# ==========================================================

def get_winning_combinations():

    return [

        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),
        (2, 4, 6)
    ]


# ==========================================================
# CHECK WINNER
# ==========================================================

def check_winner(
    board,
    symbol
):

    for first, second, third in get_winning_combinations():

        if (
            board[first] == symbol
            and board[second] == symbol
            and board[third] == symbol
        ):

            return True

    return False


# ==========================================================
# GET WINNING LINE
# ==========================================================

def get_winning_line(
    board,
    symbol
):

    for combination in get_winning_combinations():

        first, second, third = combination

        if (
            board[first] == symbol
            and board[second] == symbol
            and board[third] == symbol
        ):

            return combination

    return None


# ==========================================================
# DISPLAY WINNING LINE
# ==========================================================

def display_winning_line(
    winning_line
):

    if winning_line is None:
        return

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


# ==========================================================
# FIND WINNING MOVE
# ==========================================================

def find_winning_move(
    board,
    symbol
):

    for move in get_available_moves(board):

        test_board = board.copy()

        make_move(
            test_board,
            move,
            symbol
        )

        if check_winner(
            test_board,
            symbol
        ):

            return move

    return None


# ==========================================================
# EASY AI
# ==========================================================

def easy_computer_move(board):

    available = get_available_moves(board)

    if available:
        return random.choice(available)

    return None


# ==========================================================
# MEDIUM AI
# ==========================================================

def medium_computer_move(
    board,
    computer_symbol,
    player_symbol
):

    # Try to win
    winning_move = find_winning_move(
        board,
        computer_symbol
    )

    if winning_move:
        return winning_move

    # Block player
    blocking_move = find_winning_move(
        board,
        player_symbol
    )

    if blocking_move:
        return blocking_move

    # Center
    if board[4] == " ":
        return 5

    # Corners
    corners = [
        move for move in [1, 3, 7, 9]
        if move in get_available_moves(board)
    ]

    if corners:
        return random.choice(corners)

    return easy_computer_move(board)


# ==========================================================
# MINIMAX
# ==========================================================

def minimax(
    board,
    depth,
    maximizing,
    computer_symbol,
    player_symbol
):

    if check_winner(
        board,
        computer_symbol
    ):

        return 10 - depth

    if check_winner(
        board,
        player_symbol
    ):

        return depth - 10

    if is_board_full(board):
        return 0

    if maximizing:

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


# ==========================================================
# HARD AI
# ==========================================================

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


# ==========================================================
# COMPUTER MOVE
# ==========================================================

def get_computer_move(
    board,
    difficulty
):

    if difficulty == "Easy":

        return easy_computer_move(board)

    if difficulty == "Medium":

        return medium_computer_move(
            board,
            "O",
            "X"
        )

    return hard_computer_move(
        board,
        "O",
        "X"
    )


# ==========================================================
# DISPLAY COMPUTER MOVE
# ==========================================================

def display_computer_move(move):

    print()
    print("Computer is thinking...")
    time.sleep(0.7)

    print(
        f"Computer chose position {move}."
    )

    print()


# ==========================================================
# MOVE HISTORY
# ==========================================================

def display_move_history(
    move_history
):

    print()
    print("=" * 65)
    print("                    MOVE HISTORY")
    print("=" * 65)

    if not move_history:

        print()
        print("No moves have been made.")

    else:

        for number, move in enumerate(
            move_history,
            start=1
        ):

            print(
                f"{number:>2}. "
                f"{move['player']} "
                f"({move['symbol']}) "
                f"-> Position "
                f"{move['position']}"
            )

    print("=" * 65)
    print()


# ==========================================================
# PLAYER MOVE
# ==========================================================

def get_player_move(
    player_name,
    symbol,
    board,
    move_history
):

    while True:

        print(
            f"{player_name} ({symbol})"
        )

        print(
            "1-9 = Move | U = Undo | H = History"
        )

        print(
            "R = Restart | Q = Quit"
        )

        choice = input("> ").strip().upper()

        if choice == "Q":
            return "quit"

        if choice == "U":
            return "undo"

        if choice == "H":

            display_move_history(
                move_history
            )

            continue

        if choice == "R":
            return "restart"

        if not choice.isdigit():

            print(
                "Please enter a number from 1 to 9."
            )

            continue

        move = int(choice)

        if not is_valid_move(
            board,
            move
        ):

            if move < 1 or move > 9:

                print(
                    "Please choose a number from 1 to 9."
                )

            else:

                print(
                    "That position is already taken."
                )

            continue

        return move


# ==========================================================
# UNDO
# ==========================================================

def undo_last_move(
    board,
    move_history,
    mode
):

    if not move_history:

        print()
        print("There are no moves to undo.")
        print()

        return False

    if mode == "PvP":

        last_move = move_history.pop()

        board[
            last_move["position"] - 1
        ] = " "

        print()
        print("Last move undone.")
        print()

        return True

    # Player vs Computer
    moves_to_remove = min(
        2,
        len(move_history)
    )

    for _ in range(
        moves_to_remove
    ):

        last_move = move_history.pop()

        board[
            last_move["position"] - 1
        ] = " "

    print()
    print("Last turn undone.")
    print()

    return True


# ==========================================================
# GAME MODE
# ==========================================================

def select_game_mode():

    while True:

        print()
        print("=" * 65)
        print("                     GAME MODE")
        print("=" * 65)

        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. Back")

        print("=" * 65)

        choice = input("> ").strip()

        if choice == "1":
            return "PvP"

        if choice == "2":
            return "PvC"

        if choice == "3":
            return None

        print("Invalid option.")


# ==========================================================
# DIFFICULTY
# ==========================================================

def select_difficulty():

    while True:

        print()
        print("=" * 65)
        print("                  COMPUTER DIFFICULTY")
        print("=" * 65)

        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        print("=" * 65)

        choice = input("> ").strip()

        if choice == "1":
            return "Easy"

        if choice == "2":
            return "Medium"

        if choice == "3":
            return "Hard"

        print("Invalid option.")


# ==========================================================
# FIRST PLAYER
# ==========================================================

def select_first_player():

    while True:

        print()
        print("=" * 65)
        print("                    FIRST PLAYER")
        print("=" * 65)

        print("1. Player X")
        print("2. Player O")
        print("3. Random")

        print("=" * 65)

        choice = input("> ").strip()

        if choice == "1":
            return "X"

        if choice == "2":
            return "O"

        if choice == "3":
            return random.choice(
                ["X", "O"]
            )

        print("Invalid option.")


# ==========================================================
# WINNER DISPLAY
# ==========================================================

def display_winner(
    player_name,
    symbol
):

    print()
    print("=" * 65)
    print(f"                    {player_name}")
    print("                       WINS!")
    print()
    print(f"                     Symbol: {symbol}")
    print("=" * 65)
    print()


# ==========================================================
# DRAW DISPLAY
# ==========================================================

def display_draw():

    print()
    print("=" * 65)
    print("                     IT'S A DRAW!")
    print("=" * 65)
    print()


# ==========================================================
# UPDATE STREAK
# ==========================================================

def update_streaks(
    statistics,
    winner
):

    if winner == "X":

        statistics["X_streak"] += 1
        statistics["O_streak"] = 0

        statistics["X_best_streak"] = max(
            statistics["X_best_streak"],
            statistics["X_streak"]
        )

    elif winner == "O":

        statistics["O_streak"] += 1
        statistics["X_streak"] = 0

        statistics["O_best_streak"] = max(
            statistics["O_best_streak"],
            statistics["O_streak"]
        )

    else:

        statistics["X_streak"] = 0
        statistics["O_streak"] = 0


# ==========================================================
# PLAY ONE GAME
# ==========================================================

def play_game(
    player_x,
    player_o,
    mode,
    difficulty,
    first_player
):

    board = create_board()

    move_history = []

    move_count = 0

    current_symbol = first_player

    if current_symbol == "X":
        current_player = player_x
    else:
        if mode == "PvC":
            current_player = "Computer"
        else:
            current_player = player_o

    start_time = time.time()

    display_position_guide()

    while True:

        display_board(board)

        print(
            f"Moves made: {move_count}"
        )

        # Computer turn
        if (
            mode == "PvC"
            and current_symbol == "O"
        ):

            move = get_computer_move(
                board,
                difficulty
            )

            display_computer_move(move)

        else:

            move = get_player_move(
                current_player,
                current_symbol,
                board,
                move_history
            )

        # Quit
        if move == "quit":

            return {
                "result": "quit",
                "moves": move_count,
                "history": move_history,
                "time": time.time() - start_time
            }

        # Restart
        if move == "restart":

            return {
                "result": "restart",
                "moves": move_count,
                "history": move_history,
                "time": time.time() - start_time
            }

        # Undo
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

        # Make move
        make_move(
            board,
            move,
            current_symbol
        )

        move_count += 1

        move_history.append(
            {
                "player": current_player,
                "symbol": current_symbol,
                "position": move
            }
        )

        # Winner
        if check_winner(
            board,
            current_symbol
        ):

            elapsed_time = (
                time.time()
                - start_time
            )

            display_board(board)

            display_winner(
                current_player,
                current_symbol
            )

            winning_line = get_winning_line(
                board,
                current_symbol
            )

            display_winning_line(
                winning_line
            )

            display_move_history(
                move_history
            )

            return {
                "result": current_symbol,
                "moves": move_count,
                "history": move_history,
                "winning_line": winning_line,
                "time": elapsed_time
            }

        # Draw
        if is_board_full(board):

            elapsed_time = (
                time.time()
                - start_time
            )

            display_board(board)

            display_draw()

            display_move_history(
                move_history
            )

            return {
                "result": "Draw",
                "moves": move_count,
                "history": move_history,
                "winning_line": None,
                "time": elapsed_time
            }

        # Switch turn
        if current_symbol == "X":

            current_symbol = "O"

            if mode == "PvC":
                current_player = "Computer"
            else:
                current_player = player_o

        else:

            current_symbol = "X"
            current_player = player_x


# ==========================================================
# ACHIEVEMENTS
# ==========================================================

def get_achievements():

    return [

        (
            "FIRST_WIN",
            "First Victory",
            "Win your first game."
        ),

        (
            "THREE_WINS",
            "Triple Threat",
            "Win 3 games."
        ),

        (
            "FIVE_WINS",
            "Five Star Player",
            "Win 5 games."
        ),

        (
            "TEN_GAMES",
            "Veteran",
            "Complete 10 games."
        ),

        (
            "STREAK_3",
            "On Fire",
            "Reach a 3-game win streak."
        ),

        (
            "STREAK_5",
            "Unstoppable",
            "Reach a 5-game win streak."
        ),

        (
            "QUICK_WIN",
            "Speed Player",
            "Win in 5 moves or fewer."
        ),

        (
            "DIAGONAL",
            "Diagonal Master",
            "Win using a diagonal."
        ),

        (
            "CENTER",
            "Center Control",
            "Win while using position 5."
        ),

        (
            "NO_CENTER",
            "Outside the Box",
            "Win without using position 5."
        ),

        (
            "HARD_AI",
            "AI Slayer",
            "Defeat the Hard AI."
        )
    ]


# ==========================================================
# UNLOCK ACHIEVEMENT
# ==========================================================

def unlock_achievement(
    data,
    code,
    name
):

    if code in data["achievements"]:
        return

    data["achievements"].append(code)

    print()
    print("=" * 65)
    print("                 ACHIEVEMENT UNLOCKED")
    print("=" * 65)
    print()
    print(f"                    {name}")
    print()
    print("=" * 65)
    print()

    save_game_data(data)


# ==========================================================
# CHECK ACHIEVEMENTS
# ==========================================================

def check_achievements(
    data,
    scores,
    statistics,
    result,
    game,
    difficulty
):

    if result not in ("X", "O"):
        return

    wins = scores[result]

    # First win
    if wins >= 1:

        unlock_achievement(
            data,
            "FIRST_WIN",
            "First Victory"
        )

    # Three wins
    if wins >= 3:

        unlock_achievement(
            data,
            "THREE_WINS",
            "Triple Threat"
        )

    # Five wins
    if wins >= 5:

        unlock_achievement(
            data,
            "FIVE_WINS",
            "Five Star Player"
        )

    # Ten games
    total_games = (
        scores["X"]
        + scores["O"]
        + scores["Draws"]
    )

    if total_games >= 10:

        unlock_achievement(
            data,
            "TEN_GAMES",
            "Veteran"
        )

    # Streak
    if statistics[
        f"{result}_best_streak"
    ] >= 3:

        unlock_achievement(
            data,
            "STREAK_3",
            "On Fire"
        )

    if statistics[
        f"{result}_best_streak"
    ] >= 5:

        unlock_achievement(
            data,
            "STREAK_5",
            "Unstoppable"
        )

    # Quick win
    if game["moves"] <= 5:

        unlock_achievement(
            data,
            "QUICK_WIN",
            "Speed Player"
        )

    # Diagonal
    winning_line = game.get(
        "winning_line"
    )

    if winning_line in [
        (0, 4, 8),
        (2, 4, 6)
    ]:

        unlock_achievement(
            data,
            "DIAGONAL",
            "Diagonal Master"
        )

    # Center
    player_positions = [
        move["position"]
        for move in game["history"]
        if move["symbol"] == result
    ]

    if 5 in player_positions:

        unlock_achievement(
            data,
            "CENTER",
            "Center Control"
        )

    else:

        unlock_achievement(
            data,
            "NO_CENTER",
            "Outside the Box"
        )

    # Hard AI
    if (
        difficulty == "Hard"
        and result == "X"
    ):

        unlock_achievement(
            data,
            "HARD_AI",
            "AI Slayer"
        )


# ==========================================================
# CHALLENGES
# ==========================================================

def get_challenges():

    return [

        (
            "WIN_5_MOVES",
            "Speed Challenge",
            "Win a game in 5 moves or fewer."
        ),

        (
            "DIAGONAL",
            "Diagonal Master",
            "Win using a diagonal."
        ),

        (
            "CENTER",
            "Center Control",
            "Win while using position 5."
        ),

        (
            "NO_CENTER",
            "Outside the Box",
            "Win without position 5."
        ),

        (
            "BEAT_HARD",
            "Hard Mode Champion",
            "Defeat the Hard AI."
        ),

        (
            "STREAK_3",
            "Three in a Row",
            "Reach a 3-game winning streak."
        )
    ]


# ==========================================================
# COMPLETE CHALLENGE
# ==========================================================

def complete_challenge(
    data,
    code,
    name
):

    if code in data["challenges_completed"]:
        return

    data[
        "challenges_completed"
    ].append(code)

    print()
    print("=" * 65)
    print("                  CHALLENGE COMPLETE")
    print("=" * 65)
    print()
    print(f"                    {name}")
    print()
    print("=" * 65)
    print()

    save_game_data(data)


# ==========================================================
# CHECK CHALLENGES
# ==========================================================

def check_challenges(
    data,
    result,
    game,
    difficulty,
    statistics
):

    if result not in ("X", "O"):
        return

    positions = [
        move["position"]
        for move in game["history"]
        if move["symbol"] == result
    ]

    # Speed
    if game["moves"] <= 5:

        complete_challenge(
            data,
            "WIN_5_MOVES",
            "Speed Challenge"
        )

    # Diagonal
    if game["winning_line"] in [
        (0, 4, 8),
        (2, 4, 6)
    ]:

        complete_challenge(
            data,
            "DIAGONAL",
            "Diagonal Master"
        )

    # Center
    if 5 in positions:

        complete_challenge(
            data,
            "CENTER",
            "Center Control"
        )

    else:

        complete_challenge(
            data,
            "NO_CENTER",
            "Outside the Box"
        )

    # Hard AI
    if (
        difficulty == "Hard"
        and result == "X"
    ):

        complete_challenge(
            data,
            "BEAT_HARD",
            "Hard Mode Champion"
        )

    # Streak
    if statistics[
        f"{result}_best_streak"
    ] >= 3:

        complete_challenge(
            data,
            "STREAK_3",
            "Three in a Row"
        )


# ==========================================================
# MATCH HISTORY
# ==========================================================

def save_match(
    data,
    player_x,
    player_o,
    mode,
    difficulty,
    game
):

    result = game["result"]

    if result == "X":
        winner = player_x
    elif result == "O":
        winner = player_o
    else:
        winner = "Draw"

    match = {

        "game_number":
            data["lifetime_games"] + 1,

        "player_x":
            player_x,

        "player_o":
            player_o,

        "mode":
            mode,

        "difficulty":
            difficulty,

        "result":
            winner,

        "symbol":
            result,

        "moves":
            game["moves"],

        "time":
            round(
                game["time"],
                2
            ),

        "date":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
    }

    data["match_history"].append(
        match
    )

    # Keep latest 100
    if len(
        data["match_history"]
    ) > 100:

        data["match_history"] = (
            data["match_history"][-100:]
        )


# ==========================================================
# UPDATE LIFETIME DATA
# ==========================================================

def update_lifetime_data(
    data,
    game
):

    result = game["result"]

    if result == "quit":
        return

    data["lifetime_games"] += 1

    data["total_moves"] += game["moves"]

    data["total_play_time"] += game["time"]

    if result == "X":

        data["lifetime_wins_x"] += 1

    elif result == "O":

        data["lifetime_wins_o"] += 1

    elif result == "Draw":

        data["lifetime_draws"] += 1

    if result in ("X", "O"):

        if (
            data["fastest_win"] is None
            or game["time"]
            < data["fastest_win"]
        ):

            data["fastest_win"] = game["time"]

    if (
        game["moves"]
        > data["longest_game"]
    ):

        data["longest_game"] = game["moves"]


# ==========================================================
# MATCH HISTORY DISPLAY
# ==========================================================

def display_match_history(data):

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
                f"Game #{match['game_number']}"
            )

            print(
                f"{match['player_x']} "
                f"vs "
                f"{match['player_o']}"
            )

            print(
                f"Mode: {match['mode']}"
            )

            if match["difficulty"]:

                print(
                    f"Difficulty: "
                    f"{match['difficulty']}"
                )

            print(
                f"Result: {match['result']}"
            )

            print(
                f"Moves: {match['moves']}"
            )

            print(
                f"Time: {match['time']:.2f}s"
            )

            print(
                f"Date: {match['date']}"
            )

    print()
    print("=" * 75)
    print()


# ==========================================================
# ACHIEVEMENTS DISPLAY
# ==========================================================

def display_achievements(data):

    achievements = get_achievements()

    unlocked = set(
        data["achievements"]
    )

    print()
    print("=" * 70)
    print("                      ACHIEVEMENTS")
    print("=" * 70)

    for code, name, description in achievements:

        if code in unlocked:
            status = "[UNLOCKED]"
        else:
            status = "[LOCKED]  "

        print()
        print(
            f"{status} {name}"
        )

        print(
            f"          {description}"
        )

    print()
    print(
        f"Unlocked: "
        f"{len(unlocked)}/{len(achievements)}"
    )

    print("=" * 70)
    print()


# ==========================================================
# CHALLENGES DISPLAY
# ==========================================================

def display_challenges(data):

    challenges = get_challenges()

    completed = set(
        data["challenges_completed"]
    )

    print()
    print("=" * 70)
    print("                       CHALLENGES")
    print("=" * 70)

    for code, name, description in challenges:

        status = (
            "[DONE]"
            if code in completed
            else "[   ]"
        )

        print()
        print(
            f"{status} {name}"
        )

        print(
            f"      {description}"
        )

    print()
    print(
        f"Completed: "
        f"{len(completed)}/{len(challenges)}"
    )

    print("=" * 70)
    print()


# ==========================================================
# LEADERBOARD
# ==========================================================

def display_leaderboard(
    player_x,
    player_o,
    scores,
    statistics
):

    players = [

        {
            "name": player_x,
            "wins": scores["X"],
            "streak":
                statistics["X_best_streak"]
        },

        {
            "name": player_o,
            "wins": scores["O"],
            "streak":
                statistics["O_best_streak"]
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
    print("=" * 70)
    print("                       LEADERBOARD")
    print("=" * 70)

    print()
    print(
        f"{'Rank':<8}"
        f"{'Player':<25}"
        f"{'Wins':<10}"
        f"{'Best Streak':<15}"
    )

    print("-" * 70)

    for index, player in enumerate(
        players,
        start=1
    ):

        print(
            f"{index:<8}"
            f"{player['name']:<25}"
            f"{player['wins']:<10}"
            f"{player['streak']:<15}"
        )

    print("=" * 70)
    print()


# ==========================================================
# GAME CENTER STATISTICS
# ==========================================================

def display_game_center_stats(
    player_x,
    player_o,
    scores,
    statistics,
    data
):

    print()
    print("=" * 70)
    print("                    GAME CENTER STATS")
    print("=" * 70)

    print()
    print("CURRENT SESSION")
    print("-" * 70)

    print(
        f"{player_x}: "
        f"{scores['X']} wins"
    )

    print(
        f"{player_o}: "
        f"{scores['O']} wins"
    )

    print(
        f"Draws: "
        f"{scores['Draws']}"
    )

    print(
        f"Total Moves: "
        f"{statistics['total_moves']}"
    )

    print()
    print("LIFETIME RECORD")
    print("-" * 70)

    print(
        f"Completed Games: "
        f"{data['lifetime_games']}"
    )

    print(
        f"Lifetime X Wins: "
        f"{data['lifetime_wins_x']}"
    )

    print(
        f"Lifetime O Wins: "
        f"{data['lifetime_wins_o']}"
    )

    print(
        f"Lifetime Draws: "
        f"{data['lifetime_draws']}"
    )

    print(
        f"Lifetime Moves: "
        f"{data['total_moves']}"
    )

    print(
        f"Play Time: "
        f"{data['total_play_time']:.2f} seconds"
    )

    if data["fastest_win"] is not None:

        print(
            f"Fastest Win: "
            f"{data['fastest_win']:.2f} seconds"
        )

    print(
        f"Longest Game: "
        f"{data['longest_game']} moves"
    )

    print()
    print("UNLOCKS")
    print("-" * 70)

    print(
        f"Achievements: "
        f"{len(data['achievements'])}"
    )

    print(
        f"Challenges: "
        f"{len(data['challenges_completed'])}"
    )

    print("=" * 70)
    print()


# ==========================================================
# RESET SESSION
# ==========================================================

def reset_session(
    scores,
    statistics
):

    scores["X"] = 0
    scores["O"] = 0
    scores["Draws"] = 0

    new_statistics = create_statistics()

    statistics.clear()

    statistics.update(
        new_statistics
    )

    print()
    print("Current session has been reset.")
    print()


# ==========================================================
# RESET ALL SAVED DATA
# ==========================================================

def reset_all_data(data):

    confirm = input(
        "Delete ALL saved Game Center data? (YES/NO): "
    ).strip().upper()

    if confirm != "YES":

        print()
        print("Reset cancelled.")
        print()

        return

    new_data = create_game_data()

    data.clear()

    data.update(
        new_data
    )

    save_game_data(data)

    print()
    print("All saved Game Center data has been deleted.")
    print()


# ==========================================================
# RULES
# ==========================================================

def display_rules():

    print()
    print("=" * 65)
    print("                         RULES")
    print("=" * 65)

    print()
    print("1. The game is played on a 3x3 board.")
    print()
    print("2. Players take turns placing their symbol.")
    print()
    print("3. X and O are the two symbols.")
    print()
    print("4. The first player to get three symbols")
    print("   in a row wins.")
    print()
    print("5. A winning line can be horizontal,")
    print("   vertical, or diagonal.")
    print()
    print("6. If the board is full and nobody wins,")
    print("   the game ends in a draw.")
    print()
    print("7. U = Undo")
    print("8. H = Move History")
    print("9. R = Restart")
    print("10. Q = Quit")

    print()
    print("=" * 65)
    print()


# ==========================================================
# HOW TO PLAY
# ==========================================================

def display_how_to_play():

    print()
    print("=" * 65)
    print("                      HOW TO PLAY")
    print("=" * 65)

    display_position_guide()

    print("Choose a number from 1 to 9.")

    print()
    print("Example:")
    print("> 5")

    print()
    print("This places your symbol in the center.")

    print()
    print("During your turn:")

    print("U = Undo")
    print("H = Move History")
    print("R = Restart")
    print("Q = Quit")

    print()
    print("Try to create three of your symbols")
    print("in a horizontal, vertical, or diagonal line.")

    print()
    print("=" * 65)
    print()


# ==========================================================
# ABOUT
# ==========================================================

def display_about():

    print()
    print("=" * 65)
    print("                         ABOUT")
    print("=" * 65)

    print()
    print("TIC TAC TOE")
    print("Python Game Center Edition")

    print()
    print("A terminal-based Tic Tac Toe game")
    print("created as a Python learning project.")

    print()
    print("FEATURES")
    print("-" * 40)

    print("Player vs Player")
    print("Player vs Computer")
    print("Easy / Medium / Hard AI")
    print("Minimax Algorithm")
    print("Score Tracking")
    print("Statistics")
    print("Win Streaks")
    print("Move History")
    print("Undo")
    print("Restart")
    print("Achievements")
    print("Challenges")
    print("Match History")
    print("Leaderboard")
    print("Game Timer")
    print("Persistent JSON Data")
    print("Tournament Mode")

    print()
    print("PYTHON CONCEPTS")
    print("-" * 40)

    print("Functions")
    print("Lists")
    print("Dictionaries")
    print("Loops")
    print("Conditions")
    print("File Handling")
    print("JSON")
    print("Random")
    print("Datetime")
    print("Recursion")
    print("Algorithms")
    print("Input Validation")

    print()
    print("=" * 65)
    print()


# ==========================================================
# MOVE GUIDE
# ==========================================================

def display_move_guide():

    print()
    print("=" * 65)
    print("                      MOVE GUIDE")
    print("=" * 65)

    print()
    print("                      1   |   2   |   3")
    print("                    -------+-------+-------")
    print("                      4   |   5   |   6")
    print("                    -------+-------+-------")
    print("                      7   |   8   |   9")

    print()
    print("Center: 5")
    print("Corners: 1, 3, 7, 9")
    print("Sides: 2, 4, 6, 8")

    print()
    print("=" * 65)
    print()


# ==========================================================
# PLAY AGAIN
# ==========================================================

def play_again():

    while True:

        choice = input(
            "Play again? (Y/N): "
        ).strip().upper()

        if choice == "Y":
            return True

        if choice == "N":
            return False

        print(
            "Please enter Y or N."
        )


# ==========================================================
# TOURNAMENT
# ==========================================================

def run_tournament(
    player_x,
    player_o
):

    print()
    print("=" * 65)
    print("                    TOURNAMENT MODE")
    print("=" * 65)

    print("1. Best of 3")
    print("2. Best of 5")
    print("3. Best of 7")
    print("4. Back")

    print("=" * 65)

    choice = input("> ").strip()

    if choice == "4":
        return

    if choice == "1":
        wins_needed = 2

    elif choice == "2":
        wins_needed = 3

    elif choice == "3":
        wins_needed = 4

    else:

        print("Invalid option.")
        return

    x_wins = 0
    o_wins = 0
    draws = 0

    print()
    print(
        f"First to {wins_needed} wins becomes champion."
    )

    while (
        x_wins < wins_needed
        and o_wins < wins_needed
    ):

        first_player = random.choice(
            ["X", "O"]
        )

        game = play_game(
            player_x,
            player_o,
            "PvP",
            None,
            first_player
        )

        if game["result"] == "quit":

            print(
                "Tournament ended."
            )

            return

        if game["result"] == "restart":

            continue

        if game["result"] == "X":

            x_wins += 1

        elif game["result"] == "O":

            o_wins += 1

        else:

            draws += 1

        print()
        print("=" * 65)
        print("                 TOURNAMENT SCORE")
        print("=" * 65)

        print(
            f"{player_x}: {x_wins}"
        )

        print(
            f"{player_o}: {o_wins}"
        )

        print(
            f"Draws: {draws}"
        )

        print("=" * 65)

    print()
    print("=" * 65)
    print("                TOURNAMENT COMPLETE")
    print("=" * 65)

    if x_wins == wins_needed:

        print(
            f"CHAMPION: {player_x}"
        )

    else:

        print(
            f"CHAMPION: {player_o}"
        )

    print("=" * 65)
    print()


# ==========================================================
# GAME CENTER MENU
# ==========================================================

def game_center_menu():

    print()
    print("=" * 65)
    print("                      GAME CENTER")
    print("=" * 65)

    print("1. Achievements")
    print("2. Challenges")
    print("3. Match History")
    print("4. Leaderboard")
    print("5. Game Center Statistics")
    print("6. Tournament Mode")
    print("7. Reset All Saved Data")
    print("8. Back")

    print("=" * 65)


# ==========================================================
# GAME CENTER
# ==========================================================

def game_center(
    player_x,
    player_o,
    scores,
    statistics,
    data
):

    while True:

        game_center_menu()

        choice = input("> ").strip()

        if choice == "1":

            display_achievements(
                data
            )

        elif choice == "2":

            display_challenges(
                data
            )

        elif choice == "3":

            display_match_history(
                data
            )

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

            reset_all_data(
                data
            )

        elif choice == "8":

            return

        else:

            print(
                "Invalid option."
            )


# ==========================================================
# PROCESS COMPLETED GAME
# ==========================================================

def process_completed_game(
    game,
    player_x,
    player_o,
    mode,
    difficulty,
    scores,
    statistics,
    data
):

    result = game["result"]

    if result == "quit":

        statistics["games_quit"] += 1

        return

    if result == "restart":

        return

    moves = game["moves"]

    # Score
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

    else:

        scores["Draws"] += 1

        update_streaks(
            statistics,
            "Draw"
        )

    statistics[
        "total_moves"
    ] += moves

    # Fastest player win
    if result in ("X", "O"):

        current_fastest = statistics[
            f"{result}_fastest_win"
        ]

        if (
            current_fastest is None
            or game["time"] < current_fastest
        ):

            statistics[
                f"{result}_fastest_win"
            ] = game["time"]

        statistics[
            f"{result}_longest_win"
        ] = max(
            statistics[
                f"{result}_longest_win"
            ],
            moves
        )

    # Lifetime
    update_lifetime_data(
        data,
        game
    )

    # Match history
    save_match(
        data,
        player_x,
        player_o,
        mode,
        difficulty,
        game
    )

    # Achievements
    check_achievements(
        data,
        scores,
        statistics,
        result,
        game,
        difficulty
    )

    # Challenges
    check_challenges(
        data,
        result,
        game,
        difficulty,
        statistics
    )

    save_game_data(data)

    print()
    print(
        f"Game Time: "
        f"{game['time']:.2f} seconds"
    )

    print()

    display_scores(
        player_x,
        player_o,
        scores
    )


# ==========================================================
# MAIN MENU
# ==========================================================

def display_menu():

    print()
    print("=" * 65)
    print("                       MAIN MENU")
    print("=" * 65)

    print("1. Start Game")
    print("2. Game Center")
    print("3. Tournament Mode")
    print("4. View Scores")
    print("5. View Statistics")
    print("6. View Rules")
    print("7. How To Play")
    print("8. Move Guide")
    print("9. Change Player Names")
    print("10. About Game")
    print("11. Reset Session")
    print("12. Exit")

    print("=" * 65)


# ==========================================================
# MAIN PROGRAM
# ==========================================================

def main():

    display_title()

    player_x, player_o = (
        get_player_names()
    )

    scores = {
        "X": 0,
        "O": 0,
        "Draws": 0
    }

    statistics = create_statistics()

    data = load_game_data()

    while True:

        display_menu()

        choice = input(
            "Choose an option: "
        ).strip()

        # --------------------------------------------------
        # START GAME
        # --------------------------------------------------

        if choice == "1":

            mode = select_game_mode()

            if mode is None:
                continue

            difficulty = None

            if mode == "PvC":

                difficulty = select_difficulty()

            first_player = (
                select_first_player()
            )

            print()

            if first_player == "X":

                print(
                    f"{player_x} will go first."
                )

            else:

                if mode == "PvC":

                    print(
                        "Computer will go first."
                    )

                else:

                    print(
                        f"{player_o} will go first."
                    )

            print()

            while True:

                game = play_game(
                    player_x,
                    player_o,
                    mode,
                    difficulty,
                    first_player
                )

                if game["result"] == "restart":

                    print()
                    print(
                        "Restarting game..."
                    )

                    time.sleep(0.7)

                    continue

                process_completed_game(
                    game,
                    player_x,
                    player_o,
                    mode,
                    difficulty,
                    scores,
                    statistics,
                    data
                )

                if game["result"] == "quit":

                    break

                if not play_again():

                    break

                first_player = random.choice(
                    ["X", "O"]
                )

        # --------------------------------------------------
        # GAME CENTER
        # --------------------------------------------------

        elif choice == "2":

            game_center(
                player_x,
                player_o,
                scores,
                statistics,
                data
            )

        # --------------------------------------------------
        # TOURNAMENT
        # --------------------------------------------------

        elif choice == "3":

            run_tournament(
                player_x,
                player_o
            )

        # --------------------------------------------------
        # SCORES
        # --------------------------------------------------

        elif choice == "4":

            display_scores(
                player_x,
                player_o,
                scores
            )

        # --------------------------------------------------
        # STATISTICS
        # --------------------------------------------------

        elif choice == "5":

            display_statistics(
                player_x,
                player_o,
                scores,
                statistics
            )

        # --------------------------------------------------
        # RULES
        # --------------------------------------------------

        elif choice == "6":

            display_rules()

        # --------------------------------------------------
        # HOW TO PLAY
        # --------------------------------------------------

        elif choice == "7":

            display_how_to_play()

        # --------------------------------------------------
        # MOVE GUIDE
        # --------------------------------------------------

        elif choice == "8":

            display_move_guide()

        # --------------------------------------------------
        # CHANGE NAMES
        # --------------------------------------------------

        elif choice == "9":

            player_x, player_o = (
                get_player_names()
            )

            print()
            print(
                "Player names updated successfully."
            )

        # --------------------------------------------------
        # ABOUT
        # --------------------------------------------------

        elif choice == "10":

            display_about()

        # --------------------------------------------------
        # RESET SESSION
        # --------------------------------------------------

        elif choice == "11":

            confirm = input(
                "Reset current session? (Y/N): "
            ).strip().upper()

            if confirm == "Y":

                reset_session(
                    scores,
                    statistics
                )

            else:

                print(
                    "Reset cancelled."
                )

        # --------------------------------------------------
        # EXIT
        # --------------------------------------------------

        elif choice == "12":

            save_game_data(data)

            print()
            print("=" * 65)
            print("                 THANK YOU FOR PLAYING!")
            print()
            print("                       TIC TAC TOE")
            print()
            print("                  Python Game Center")
            print("=" * 65)
            print()

            break

        # --------------------------------------------------
        # INVALID
        # --------------------------------------------------

        else:

            print()
            print(
                "Invalid option."
            )

            print(
                "Please choose 1-12."
            )


# ==========================================================
# RUN PROGRAM
# ==========================================================

if __name__ == "__main__":
    main()
