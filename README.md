# Tic Tac Toe

A beginner-friendly **Tic Tac Toe game built with Python** that runs in the terminal. The game supports Player vs Player and Player vs Computer gameplay, customizable player names, computer difficulty levels, score tracking, game statistics, replayable matches, input validation, rules, and a structured main menu.

This project was created as a learning project to practice Python programming fundamentals while gradually developing a more complete and interactive command-line game.

---

## About the Project

**Tic Tac Toe** is a classic strategy game played on a 3×3 board.

Each player is assigned a symbol:

* **Player X**
* **Player O**

Players take turns selecting an empty position on the board. The objective is to get three of the same symbols in a row.

A player can win by creating a line:

* Horizontally
* Vertically
* Diagonally

If all nine spaces are filled without either player winning, the game ends in a draw.

The expanded version of this project builds upon the original two-player game by adding **Player vs Computer mode, difficulty levels, first-player selection, statistics, score management, improved game flow, and additional game options**.

---

# Current Version

**Version:** 3.0

The project has evolved from a basic two-player terminal game into a more complete and structured Python application.

## Version 1.0

The original version included:

* Basic 3×3 board
* Two-player gameplay
* Player turn switching
* Win detection
* Draw detection
* Basic position validation

## Version 2.0

The improved version added:

* Main menu
* Player names
* Score tracking
* Multiple games in one session
* Play Again option
* Rules section
* Better input validation
* Occupied-space protection
* Quit option during a game
* Cleaner board display
* Move tracking
* Modular functions
* Improved game flow

## Version 3.0

The expanded version now includes:

* Player vs Player mode
* Player vs Computer mode
* Easy computer difficulty
* Medium computer difficulty
* Hard computer difficulty
* Computer move generation
* Computer win detection
* Computer blocking logic
* First-player selection
* Random first-player selection
* Game statistics
* Total games played
* Total moves
* Average moves per game
* Win percentages
* Score reset option
* Improved main menu
* Separate game mode selection
* Separate difficulty selection
* Better computer turn handling
* Computer thinking message
* Improved game organization

---

# Features

## Main Menu

The game includes a main menu that allows players to access different parts of the application.

```text
=======================================================
                    MAIN MENU
=======================================================
1. Start Game
2. View Rules
3. How To Play
4. View Scores
5. View Statistics
6. Change Player Names
7. Reset Scores
8. Exit
=======================================================
```

Players can start a game, read the rules, learn how to play, view scores, view statistics, change player names, reset scores, or exit the program.

---

## Game Modes

The game now supports two different ways to play.

```text
=======================================================
                    GAME MODE
=======================================================
1. Player vs Player
2. Player vs Computer
3. Back
=======================================================
```

### Player vs Player

Two human players play against each other on the same computer.

```text
Player X
   ↓
Player O
   ↓
Player X
   ↓
Player O
```

The game automatically switches turns after each valid move.

### Player vs Computer

One human player plays against the computer.

The computer controls Player O while the human player controls Player X.

The computer automatically chooses an available position based on the selected difficulty.

---

# Computer Difficulty

When Player vs Computer mode is selected, the player can choose a difficulty level.

```text
=======================================================
              COMPUTER DIFFICULTY
=======================================================
1. Easy
2. Medium
3. Hard
=======================================================
```

## Easy

The computer selects an available position randomly.

This difficulty is useful for beginners who are learning how the game works.

The computer does not intentionally try to win or block the player.

---

## Medium

The Medium computer uses basic strategy.

It will:

1. Try to win if it has a winning move.
2. Try to block the player if they are about to win.
3. Prefer the center position.
4. Prefer available corners.
5. Choose another available position if necessary.

This makes the computer more challenging than Easy mode.

---

## Hard

The Hard difficulty uses the same strategic priorities but makes more deliberate choices when selecting its moves.

The computer:

1. Looks for a winning move.
2. Looks for a move that blocks the player.
3. Attempts to take the center.
4. Attempts to take a corner.
5. Selects another available position when necessary.

The current Hard mode is **not a full Minimax AI**. A future version can improve this further by implementing the Minimax algorithm.

---

# First Player Selection

Before each game, players can choose who starts.

```text
=======================================================
                  FIRST PLAYER
=======================================================
1. Player X
2. Player O
3. Random
=======================================================
```

Players can:

* Let Player X start
* Let Player O start
* Randomly select the first player

Random first-player selection makes repeated matches less predictable.

---

# Custom Player Names

Players can enter their own names before playing.

Example:

```text
Player X name: Jose
Player O name: Alex
```

The game will then display:

```text
Jose (X)
Alex (O)
```

If no name is entered, the program automatically uses:

```text
Player X
Player O
```

---

# 3×3 Game Board

The game uses a standard 3×3 Tic Tac Toe board.

```text
             X   |   O   |
           -------+-------+-------
                 |   X   |
           -------+-------+-------
                 |       |   O
```

The board contains nine positions.

---

# Position Guide

Players can use the position guide to understand which number corresponds to each space.

```text
               1   |   2   |   3
             -------+-------+-------
               4   |   5   |   6
             -------+-------+-------
               7   |   8   |   9
```

For example:

```text
> 5
```

places the player's symbol in the center.

---

# Input Validation

The game checks player input before accepting a move.

For example, if a player enters:

```text
abc
```

The program responds:

```text
Invalid input.
Please enter a number from 1 to 9.
```

The program also rejects numbers outside the valid range.

Example:

```text
> 15
```

Output:

```text
Invalid position.
Please choose a number from 1 to 9.
```

---

# Occupied Position Protection

Players cannot overwrite an existing move.

For example:

```text
             X   |       |
           -------+-------+-------
                 |   O   |
           -------+-------+-------
                 |       |
```

If a player attempts to select position `5` again, the program responds:

```text
That position is already taken.
Please choose another position.
```

---

# Win Detection

The program checks for a winner after every valid move.

There are eight possible winning combinations:

* 3 horizontal lines
* 3 vertical lines
* 2 diagonal lines

Example:

```text
             X   |   X   |   X
           -------+-------+-------
             O   |       |   O
           -------+-------+-------
                 |       |
```

Player X wins because three X symbols are placed horizontally.

---

# Draw Detection

If all nine positions are filled and neither player wins, the game recognizes the result as a draw.

Example:

```text
             X   |   O   |   X
           -------+-------+-------
             X   |   O   |   O
           -------+-------+-------
             O   |   X   |   X
```

The program displays:

```text
=======================================================
                 IT'S A DRAW!
=======================================================
```

---

# Score Tracking

The game keeps track of scores throughout the current program session.

The scoreboard tracks:

* Player X wins
* Player O wins
* Draws
* Total games played

Example:

```text
=======================================================
                    SCOREBOARD
=======================================================
Jose (X): 3 wins
Alex (O): 2 wins
Draws:    1
Games Played: 6
=======================================================
```

The score is automatically updated after every completed game.

---

# Win Percentage

The game also calculates the percentage of games won or drawn.

Example:

```text
Win Statistics
-----------------------------------
Jose: 50.0%
Alex: 33.3%
Draws: 16.7%
```

The percentages are calculated based on the total number of completed games.

---

# Game Statistics

The game includes a separate statistics section.

It displays:

* Total games
* Player X wins
* Player O wins
* Draws
* Total moves
* Average moves per game

Example:

```text
=======================================================
                GAME STATISTICS
=======================================================
Total Games:       10
Jose Wins:         5
Alex Wins:         3
Draws:             2
Total Moves:       72
Average Moves:     7.20
=======================================================
```

This provides a better overview of the player's performance over multiple matches.

---

# Move Tracking

The program keeps track of the number of moves made during each game.

For example:

```text
Move 1
Move 2
Move 3
Move 4
...
```

The total number of moves is also used when calculating the average number of moves per game.

---

# Computer Thinking

When playing against the computer, the game displays a short thinking message before the computer makes its move.

Example:

```text
Computer is thinking...

Computer chose position 5.
```

This makes the computer mode feel more like an actual game.

---

# Play Again

After a completed game, players can choose whether they want to play another match.

```text
Would you like to play again?
Y - Yes
N - No
```

Choosing `Y` starts another game without restarting the Python program.

The scores remain available throughout the current session.

---

# Random Rematches

When players choose to continue playing, the game can randomly determine who starts the next match.

This prevents the same player from always starting every game.

---

# Change Player Names

Players can change their names from the main menu.

```text
6. Change Player Names
```

This allows the same program session to be used by different players.

---

# Reset Scores

The game includes an option to reset the current scores.

```text
7. Reset Scores
```

Before resetting, the program asks for confirmation:

```text
Are you sure you want to reset scores? (Y/N):
```

If the player enters `Y`, the scores and move statistics are reset.

If the player enters `N`, the reset is cancelled.

---

# View Rules

The Rules section explains the basic rules of Tic Tac Toe.

The rules include:

1. Tic Tac Toe is played on a 3×3 board.
2. Players take turns selecting empty spaces.
3. The objective is to get three symbols in a row.
4. A player can win horizontally, vertically, or diagonally.
5. If all nine spaces are filled without a winner, the game ends in a draw.

---

# How To Play

The game also includes a dedicated **How To Play** section.

It explains the numbered board:

```text
              1   |   2   |   3
            -------+-------+-------
              4   |   5   |   6
            -------+-------+-------
              7   |   8   |   9
```

To make a move, enter the number of the position you want.

Example:

```text
> 5
```

The symbol is placed in the center.

---

# Quit During a Game

Players can enter:

```text
Q
```

during their turn to leave the current game.

The program returns to the main menu instead of completely closing.

---

# How the Game Works

The expanded game follows this general process:

```text
Start Program
      ↓
Display Title
      ↓
Enter Player Names
      ↓
Display Main Menu
      ↓
Choose Start Game
      ↓
Select Game Mode
      ↓
+-----------------------+
|                       |
PvP                    PvC
|                       |
|                 Select Difficulty
|                       |
+-----------+-----------+
            ↓
    Select First Player
            ↓
      Create Board
            ↓
       Display Board
            ↓
       Make a Move
            ↓
      Validate Move
            ↓
       Place Symbol
            ↓
      Check Winner
            ↓
       Check Draw
            ↓
      Game Finished?
        /        \
      No          Yes
      |            |
 Switch Turn    Update Score
      |            |
      +------→  Play Again?
                  /    \
                Yes     No
                 |       |
              New Game   Menu
```

---

# Computer Decision System

The computer uses different decision strategies depending on the difficulty.

## Easy

```text
Get Available Spaces
        ↓
Choose Random Space
        ↓
Make Move
```

## Medium

```text
Check Winning Move
        ↓
Check Blocking Move
        ↓
Take Center
        ↓
Take Corner
        ↓
Choose Available Space
```

## Hard

```text
Check Winning Move
        ↓
Check Blocking Move
        ↓
Take Center
        ↓
Take Corner
        ↓
Choose Available Space
```

This system allows the project to demonstrate basic decision-making and game logic without requiring advanced artificial intelligence.

---

# Project Structure

The project is intentionally kept simple because it is a beginner Python project.

```text
Tic-Tac-Toe-game/
│
├── tic_tac_toe.py
│
└── README.md
```

## `tic_tac_toe.py`

Contains the complete Tic Tac Toe application.

The file includes:

* Main menu
* Board creation
* Board display
* Player name input
* Game mode selection
* Difficulty selection
* First-player selection
* Move validation
* Player movement
* Computer movement
* Win detection
* Draw detection
* Score tracking
* Statistics
* Move tracking
* Replay functionality
* Score reset
* Rules
* How-to-play instructions
* Game loop

## `README.md`

Contains the documentation for the project, including:

* Project information
* Features
* Game modes
* Computer difficulty
* How the game works
* Installation
* How to play
* Game rules
* Python concepts
* Project structure
* Development roadmap

---

# Main Functions

The expanded version separates different responsibilities into individual functions.

This makes the code easier to read, understand, maintain, and expand.

## `display_title()`

Displays the title when the program starts.

```python
def display_title():
```

---

## `create_board()`

Creates a new empty board.

```python
def create_board():
    return [" " for _ in range(9)]
```

---

## `display_board(board)`

Displays the current state of the Tic Tac Toe board.

```python
def display_board(board):
```

---

## `display_position_guide()`

Shows players which numbers correspond to each board position.

```python
def display_position_guide():
```

---

## `get_player_names()`

Allows players to enter their names.

```python
def get_player_names():
```

The function also provides default names if the user leaves the input empty.

---

## `display_scores()`

Displays the current scoreboard.

```python
def display_scores(player_x, player_o, scores):
```

It also calculates the win percentage of each player and the percentage of draws.

---

## `display_statistics()`

Displays detailed game statistics.

```python
def display_statistics(
    player_x,
    player_o,
    scores,
    total_moves
):
```

It calculates the average number of moves per completed game.

---

## `is_valid_move()`

Checks whether a selected position is valid and available.

```python
def is_valid_move(board, move):
```

It checks:

* Whether the position is between 1 and 9
* Whether the selected space is empty

---

## `get_available_moves()`

Returns all currently available board positions.

```python
def get_available_moves(board):
```

This function is especially useful for the computer player.

---

## `get_player_move()`

Handles player input and keeps asking until a valid move is provided.

```python
def get_player_move(player_name, player_symbol, board):
```

It also allows the player to enter `Q` to quit the current game.

---

## `make_move()`

Places a player's symbol on the board.

```python
def make_move(board, move, player_symbol):
```

---

## `get_winning_combinations()`

Returns all possible winning combinations.

```python
def get_winning_combinations():
```

---

## `check_winner()`

Checks whether a player has completed a winning combination.

```python
def check_winner(board, player_symbol):
```

It returns `True` if the player wins and `False` otherwise.

---

## `find_winning_move()`

Checks whether a specific symbol can win by making a particular move.

```python
def find_winning_move(board, symbol):
```

This function is used by the computer's Medium and Hard strategies.

---

## `easy_computer_move()`

Selects a random available position for the computer.

```python
def easy_computer_move(board):
```

---

## `medium_computer_move()`

Uses basic strategy to make a computer move.

```python
def medium_computer_move(
    board,
    computer_symbol,
    player_symbol
):
```

The computer tries to:

1. Win
2. Block
3. Take center
4. Take a corner
5. Choose another available position

---

## `hard_computer_move()`

Uses a more strategic computer decision process.

```python
def hard_computer_move(
    board,
    computer_symbol,
    player_symbol
):
```

---

## `get_computer_move()`

Selects the appropriate computer strategy based on the chosen difficulty.

```python
def get_computer_move(
    board,
    difficulty,
    computer_symbol,
    player_symbol
):
```

---

## `select_game_mode()`

Allows the player to choose between Player vs Player and Player vs Computer.

```python
def select_game_mode():
```

---

## `select_difficulty()`

Allows the player to choose the computer difficulty.

```python
def select_difficulty():
```

---

## `select_first_player()`

Allows the player to choose who starts the game.

```python
def select_first_player():
```

---

## `is_board_full()`

Checks whether all nine positions have been filled.

```python
def is_board_full(board):
```

---

## `display_winner()`

Displays the winner message.

```python
def display_winner(player_name, player_symbol):
```

---

## `display_draw()`

Displays the draw message.

```python
def display_draw():
```

---

## `display_computer_move()`

Displays the computer's selected move.

```python
def display_computer_move(move):
```

---

## `play_game()`

Controls the main gameplay.

```python
def play_game(
    player_x,
    player_o,
    mode,
    difficulty=None,
    first_player="X"
):
```

This function manages:

* Board creation
* Player turns
* Computer turns
* Player moves
* Computer moves
* Win checking
* Draw checking
* Turn switching
* Move counting
* Game completion

---

## `play_again()`

Asks players whether they want to start another game.

```python
def play_again():
```

---

## `reset_scores()`

Resets the current scoreboard.

```python
def reset_scores(scores):
```

---

## `display_rules()`

Displays the rules of Tic Tac Toe.

```python
def display_rules():
```

---

## `display_how_to_play()`

Displays instructions for new players.

```python
def display_how_to_play():
```

---

## `display_menu()`

Displays the main menu.

```python
def display_menu():
```

---

## `main()`

Controls the entire application.

```python
def main():
```

It connects the different functions together and manages the main program loop.

---

# Board System

The board is stored using a Python list containing nine spaces.

```python
board = [" " for _ in range(9)]
```

Python uses indexes starting from `0`.

Internally, the board looks like:

```text
 0 | 1 | 2
---+---+---
 3 | 4 | 5
---+---+---
 6 | 7 | 8
```

However, players interact with the board using positions `1–9`:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

The program converts the player's position into the appropriate list index.

For example:

```python
move = 5
```

becomes:

```python
index = move - 1
```

which results in:

```text
index = 4
```

The program can then access:

```python
board[4]
```

---

# Winning Combinations

The program stores the possible winning combinations in a list of tuples.

```python
winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]
```

These represent:

```text
Horizontal:
(0, 1, 2)
(3, 4, 5)
(6, 7, 8)

Vertical:
(0, 3, 6)
(1, 4, 7)
(2, 5, 8)

Diagonal:
(0, 4, 8)
(2, 4, 6)
```

The program checks these combinations after every move.

---

# Technologies Used

This project uses:

* **Python 3**
* Python Lists
* Functions
* Loops
* Conditional Statements
* Dictionaries
* Tuples
* String Methods
* User Input
* Random Module
* Time Module
* Boolean Values
* Basic Game Logic
* Modular Programming

No external libraries or third-party packages are required.

---

# Requirements

You only need:

* Python 3
* A terminal or command prompt
* A code editor

The project does not require any third-party dependencies.

The `random` and `time` modules used by the project are included with Python.

---

# How to Run

## 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python installation:

```bash
python --version
```

You should see something similar to:

```text
Python 3.x.x
```

---

## 2. Clone the Repository

Clone the repository using Git:

```bash
git clone https://github.com/your-username/tic-tac-toe.git
```

Replace `your-username` with your GitHub username.

---

## 3. Open the Project

Move into the project directory:

```bash
cd tic-tac-toe
```

---

## 4. Run the Game

Run:

```bash
python tic_tac_toe.py
```

The game will start in the terminal.

---

# How to Play

## Step 1 — Enter Player Names

When the program starts:

```text
Player X name:
Player O name:
```

Enter the names of the players.

---

## Step 2 — Open the Main Menu

You will see:

```text
1. Start Game
2. View Rules
3. How To Play
4. View Scores
5. View Statistics
6. Change Player Names
7. Reset Scores
8. Exit
```

---

## Step 3 — Start a Game

Choose:

```text
1
```

The game will ask you to select a game mode.

```text
1. Player vs Player
2. Player vs Computer
3. Back
```

---

## Step 4 — Select Difficulty

If Player vs Computer is selected, choose:

```text
1. Easy
2. Medium
3. Hard
```

---

## Step 5 — Select the First Player

Choose:

```text
1. Player X
2. Player O
3. Random
```

---

## Step 6 — Make a Move

The position guide will appear:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

Enter a number from `1` to `9`.

Example:

```text
Jose (X)
Choose a position from 1-9

> 5
```

The X symbol will be placed in position 5.

---

## Step 7 — Continue Playing

The game continues until:

* Player X wins
* Player O wins
* The computer wins
* The game ends in a draw
* A player quits

---

## Step 8 — View the Result

After the game ends, the program displays the result and updates the scoreboard.

Example:

```text
=======================================================
                    SCOREBOARD
=======================================================
Jose (X): 1 wins
Computer (O): 0 wins
Draws: 0
Games Played: 1
=======================================================
```

---

# Example Gameplay

```text
=======================================================
                 TIC TAC TOE
              Python Edition
=======================================================

Enter Player Information
-----------------------------------
Player X name: Jose
Player O name: Alex

=======================================================
                    MAIN MENU
=======================================================
1. Start Game
2. View Rules
3. How To Play
4. View Scores
5. View Statistics
6. Change Player Names
7. Reset Scores
8. Exit
=======================================================

Choose an option: 1

=======================================================
                    GAME MODE
=======================================================
1. Player vs Player
2. Player vs Computer
3. Back
=======================================================

Choose an option: 2

=======================================================
              COMPUTER DIFFICULTY
=======================================================
1. Easy
2. Medium
3. Hard
=======================================================

Choose difficulty: 2

=======================================================
                  FIRST PLAYER
=======================================================
1. Player X
2. Player O
3. Random
=======================================================

Choose an option: 1

Jose will go first.
```

The game then begins.

```text
             POSITION GUIDE

               1   |   2   |   3
             -------+-------+-------
               4   |   5   |   6
             -------+-------+-------
               7   |   8   |   9
```

The player selects a position:

```text
Jose (X)
Choose a position from 1-9

> 5
```

The computer then makes its move:

```text
Computer is thinking...

Computer chose position 1.
```

The game continues until there is a winner or a draw.

---

# Error Handling

The game handles several common input problems.

## Invalid Text

Input:

```text
hello
```

Output:

```text
Invalid input.
Please enter a number from 1 to 9.
```

## Number Too High

Input:

```text
20
```

Output:

```text
Invalid position.
Please choose a number from 1 to 9.
```

## Number Too Low

Input:

```text
0
```

Output:

```text
Invalid position.
Please choose a number from 1 to 9.
```

## Occupied Position

If a player selects an occupied position:

```text
That position is already taken.
Please choose another position.
```

## Quit

Players can enter:

```text
Q
```

to leave the current game.

---

# Python Concepts Practiced

This project provides practice with several fundamental Python concepts.

## Variables

Variables store information such as:

```python
current_player = player_x
current_symbol = "X"
```

---

## Lists

The board is stored using a list:

```python
board = [" " for _ in range(9)]
```

Lists are also used for available moves and winning combinations.

---

## Functions

The program is divided into many reusable functions.

For example:

```python
def check_winner(board, player_symbol):
```

This makes individual parts of the program easier to understand and maintain.

---

## Loops

`while` loops keep the game running:

```python
while True:
```

`for` loops are used to check winning combinations:

```python
for first, second, third in winning_combinations:
```

---

## Conditional Statements

`if`, `elif`, and `else` statements control the game's logic.

They are used to determine:

* Whether a move is valid
* Whether a position is occupied
* Whether a player has won
* Whether the board is full
* Which player should play next
* Which computer difficulty is selected
* Whether the player wants to continue

---

## Dictionaries

A dictionary stores the game scores:

```python
scores = {
    "X": 0,
    "O": 0,
    "Draws": 0
}
```

---

## Tuples

Tuples are used for winning combinations:

```python
(0, 1, 2)
```

---

## Random Module

The `random` module is used for:

* Easy computer moves
* Random first-player selection
* Random corner selection

Example:

```python
random.choice(available_moves)
```

---

## Time Module

The `time` module is used to create a short delay when the computer makes a move.

Example:

```python
time.sleep(0.7)
```

---

## Boolean Values

The program uses `True` and `False` to determine whether conditions are satisfied.

Example:

```python
if check_winner(board, current_symbol):
```

---

## Modular Programming

One of the biggest improvements in the project is the use of separate functions.

Instead of placing the entire game inside one large block of code, different responsibilities are separated.

```text
Input
  ↓
Validation
  ↓
Game Logic
  ↓
Computer Logic
  ↓
Score System
  ↓
Statistics
  ↓
Menu
```

This makes the project easier to understand and expand.

---

# Current Limitations

Although the game has been expanded significantly, it still has some limitations.

Current limitations include:

* The game is terminal-based.
* Player vs Computer currently uses basic computer decision-making.
* The Hard difficulty is not a true Minimax AI.
* Scores are only stored while the program is running.
* Scores are not saved to a file or database.
* There is no graphical interface.
* There are no sound effects.
* There is no online multiplayer.
* There is no player account system.
* Game history is not permanently saved.

These limitations provide opportunities for future development.

---

# Future Improvements

The project can continue to grow into a more advanced application.

## Version 4 — Advanced AI

Improve the computer opponent using the **Minimax algorithm**.

Possible difficulty levels:

```text
Easy
Medium
Hard
Impossible
```

The Impossible difficulty could use Minimax to analyze possible future moves.

---

## Version 5 — Persistent Scoreboard

Save scores so they remain available after closing the program.

Possible storage:

```text
scores.json
```

or:

```text
scores.txt
```

---

## Version 6 — Game History

Store completed matches.

Possible information:

```text
Player X
Player O
Game Mode
Difficulty
Winner
Number of Moves
Date
```

---

## Version 7 — Graphical Interface

Create a graphical version using **Tkinter** or **CustomTkinter**.

Instead of typing:

```text
5
```

players could click directly on the board.

---

## Version 8 — Database

Use SQLite to store:

* Player names
* Match history
* Scores
* Game results
* Statistics
* Winning streaks

This would turn the project into a more complete application.

---

## Version 9 — Advanced Statistics

Add statistics such as:

* Total games
* Player X wins
* Player O wins
* Draws
* Win percentage
* Current winning streak
* Longest winning streak
* Average moves
* Most common first move
* Games against the computer
* Games against another player

---

## Version 10 — Multiple Board Sizes

Allow players to select different board sizes.

Possible options:

```text
3 × 3
4 × 4
5 × 5
```

This would require more advanced win-detection logic.

---

# Development Roadmap

```text
[x] Create 3×3 game board
[x] Add two-player gameplay
[x] Add player turn switching
[x] Add position selection
[x] Add win detection
[x] Add draw detection
[x] Prevent occupied positions
[x] Add invalid input validation
[x] Add player names
[x] Add main menu
[x] Add rules section
[x] Add How To Play section
[x] Add score tracking
[x] Add Play Again option
[x] Add Change Player Names
[x] Add quit option during a game
[x] Organize code into functions
[x] Add Player vs Computer mode
[x] Add Easy difficulty
[x] Add Medium difficulty
[x] Add Hard difficulty
[x] Add computer move logic
[x] Add first-player selection
[x] Add random first-player option
[x] Add move tracking
[x] Add win percentages
[x] Add game statistics
[x] Add average moves calculation
[x] Add Reset Scores
[ ] Improve Hard mode with Minimax
[ ] Add Impossible difficulty
[ ] Add persistent scores
[ ] Add game history
[ ] Add SQLite database
[ ] Create graphical interface
[ ] Add sound effects
[ ] Add multiple board sizes
[ ] Add online multiplayer
```

---

# Learning Purpose

This project was created as part of my journey in learning **Python programming and software development**.

The first version focused on learning the basic concepts needed to create a playable game. Later versions expanded those concepts into a more structured application.

The current version demonstrates how a simple programming project can gradually become more advanced by adding:

* New game modes
* Computer decision-making
* Difficulty levels
* Statistics
* Score management
* Better input handling
* Modular programming
* Improved user experience

This project also demonstrates the process of taking an existing program and continuously improving it instead of rebuilding it from scratch.

---

# What I Learned

By building this project, I practiced:

* Creating Python programs from scratch
* Using lists to store data
* Creating reusable functions
* Using loops
* Using conditional statements
* Working with user input
* Validating user input
* Using dictionaries
* Using tuples
* Working with list indexes
* Using the `random` module
* Using the `time` module
* Designing basic game logic
* Creating computer decision logic
* Organizing code into functions
* Managing multiple game states
* Tracking scores
* Calculating statistics
* Creating menu systems
* Handling invalid input
* Improving an existing program
* Planning future software improvements

---

# Project Goals

The long-term goal of this project is to continue improving it as my Python programming skills develop.

The project can eventually evolve from a simple terminal game into a more complete Tic Tac Toe application.

```text
Basic Terminal Game
        ↓
Improved Terminal Game
        ↓
Player vs Computer
        ↓
Difficulty Levels
        ↓
Advanced AI
        ↓
Persistent Statistics
        ↓
Database
        ↓
Graphical Interface
        ↓
Advanced Tic Tac Toe Application
```

Each version provides an opportunity to learn new programming concepts and apply them to an existing project.

---

# Author

**Jose Manuel Navoa**

Information Technology Student

This project is part of my collection of beginner programming projects as I continue learning Python, exploring different programming languages, and developing my software development skills.

---

# License

This project is intended primarily for **learning and educational purposes**.

You are welcome to study the code, modify it, and use it as a reference for your own programming practice.
