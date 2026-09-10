# Tic Tac Toe

A beginner-friendly **Tic Tac Toe game built with Python** that runs in the terminal. The game supports two players, player names, score tracking, replayable matches, input validation, game rules, and a simple main menu.

This project was created as a learning project to practice Python programming fundamentals while building a complete and interactive command-line game.

---

## About the Project

**Tic Tac Toe** is a classic two-player strategy game played on a 3×3 board.

Each player is assigned a symbol:

* **Player X**
* **Player O**

Players take turns selecting an empty position on the board. The objective is to get three of the same symbols in a row.

A player can win by creating a line:

* Horizontally
* Vertically
* Diagonally

If all nine spaces are filled without either player winning, the game ends in a draw.

The improved version expands the original basic game by adding a **menu system, player names, score tracking, replay functionality, rules, better input validation, and a more organized program structure**.

---

## Current Version

**Version:** 2.0

The project has evolved from a basic two-player terminal game into a more complete and structured Python application.

### Version 1.0

The original version included:

* Basic 3×3 board
* Two-player gameplay
* Player turn switching
* Win detection
* Draw detection
* Basic position validation

### Version 2.0

The improved version now includes:

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

---

## Features

### Main Menu

The game now includes a main menu that allows players to choose what they want to do.

```text
=============================================
                MAIN MENU
=============================================
1. Start Game
2. View Rules
3. View Scores
4. Change Player Names
5. Exit
=============================================
```

Players can start a game, view the rules, check the current score, change player names, or exit the program.

---

### Two-Player Gameplay

The game supports two players playing on the same computer.

Player X always starts the game, followed by Player O.

Example:

```text
Player X
   ↓
Player O
   ↓
Player X
   ↓
Player O
```

The program automatically switches between players after each valid move.

---

### Custom Player Names

Players can enter their own names before starting the game.

Example:

```text
Player X name: Jose
Player O name: Alex
```

The game will then display:

```text
Jose (X) - choose a position:
```

instead of only displaying `Player X`.

If a player does not enter a name, the program automatically uses:

```text
Player X
Player O
```

---

### 3×3 Game Board

The game uses a standard 3×3 Tic Tac Toe board.

```text
       X   |   O   |
     -------+-------+-------
           |   X   |
     -------+-------+-------
           |       |   O
```

The board contains nine available positions.

---

### Position Guide

Players can view the position guide before starting.

```text
       1   |   2   |   3
     -------+-------+-------
       4   |   5   |   6
     -------+-------+-------
       7   |   8   |   9
```

The player simply enters the number of the position they want to use.

---

### Input Validation

The improved version provides better protection against invalid input.

For example, if a player enters:

```text
abc
```

the program responds with:

```text
Invalid input.
Please enter a number from 1 to 9.
```

The program also checks numbers outside the valid range.

For example:

```text
15
```

will not be accepted.

---

### Occupied Position Protection

Players cannot overwrite another player's move.

For example:

```text
 X |   |
---+---+---
   | O |
---+---+---
   |   |
```

If a player tries to select position `5` again, the program responds:

```text
That position is already taken.
Please choose another position.
```

---

### Win Detection

The game automatically checks for a winner after every valid move.

There are eight possible winning combinations:

* 3 horizontal lines
* 3 vertical lines
* 2 diagonal lines

For example:

```text
 X | X | X
---+---+---
 O |   | O
---+---+---
   |   |
```

Player X wins because they have three X symbols horizontally.

---

### Draw Detection

If all nine positions are filled and neither player has won, the game recognizes the result as a draw.

Example:

```text
 X | O | X
---+---+---
 X | O | O
---+---+---
 O | X | X
```

The program displays:

```text
=============================================
              IT'S A DRAW!
=============================================
```

---

### Score Tracking

The improved version keeps track of scores throughout the current program session.

The scoreboard tracks:

* Player X wins
* Player O wins
* Draws

Example:

```text
=============================================
                    SCORE
=============================================
Jose (X):  3
Alex (O):  2
Draws:     1
=============================================
```

The score is updated automatically after every completed game.

---

### Play Again

After finishing a game, players can choose whether they want to play another match.

```text
Would you like to play again?
Y - Yes
N - No
```

Choosing `Y` starts another game using the same player names and score.

This means players do not have to restart the Python program after every match.

---

### Change Player Names

Players can change their names from the main menu.

```text
4. Change Player Names
```

This allows the same program session to be used by different players.

---

### View Rules

The main menu includes a rules section that explains how Tic Tac Toe works.

```text
1. Tic Tac Toe is played by two players.

2. Player X goes first.

3. Players take turns selecting an empty
   position on the board.

4. The first player to get three symbols
   in a row wins.

5. A player can win horizontally, vertically,
   or diagonally.

6. If all nine spaces are filled and nobody
   wins, the game ends in a draw.
```

---

### Quit During a Game

Players can enter:

```text
Q
```

during their turn to leave the current game and return to the main menu.

This gives players an easy way to stop a match without closing the entire application.

---

# How the Game Works

The improved game follows a structured process:

```text
Start Program
      ↓
Display Title
      ↓
Enter Player Names
      ↓
Display Main Menu
      ↓
Choose an Option
      ↓
Start Game
      ↓
Create Empty Board
      ↓
Display Board
      ↓
Ask for Player Move
      ↓
Validate Move
      ↓
Place X or O
      ↓
Check Winner
      ↓
Check Draw
      ↓
Switch Player
      ↓
Repeat
      ↓
Game Ends
      ↓
Update Score
      ↓
Play Again?
      ↓
Return to Menu
```

This structure makes the program easier to understand and modify.

---

# Project Structure

The current project is intentionally kept simple because it is a beginner Python project.

```text
Tic-Tac-Toe-game/
│
├── game.py
│
└── README.md
```

### `tic_tac_toe.py`

Contains the complete Tic Tac Toe application.

The file includes:

* Main menu
* Board creation
* Board display
* Player name input
* Move validation
* Player movement
* Win detection
* Draw detection
* Score tracking
* Replay functionality
* Rules
* Game loop

### `README.md`

Contains the documentation for the project, including:

* Project information
* Features
* Installation
* How to play
* Game rules
* Python concepts
* Project structure
* Development roadmap

---

# Main Functions

The improved version separates different responsibilities into individual functions.

This makes the code easier to read and maintain.

## `display_title()`

Displays the title when the program starts.

```python
def display_title():
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

## `create_board()`

Creates a new empty board.

```python
def create_board():
    return [" " for _ in range(9)]
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

Displays the current game scores.

```python
def display_scores(player_x, player_o, scores):
```

---

## `is_valid_move()`

Checks whether a player's selected position is valid and available.

```python
def is_valid_move(board, move):
```

It checks:

* Whether the position is between 1 and 9
* Whether the selected space is empty

---

## `get_player_move()`

Handles player input and keeps asking until a valid move is provided.

```python
def get_player_move(player_name, player_symbol, board):
```

It also allows the player to enter `Q` to quit the current game.

---

## `make_move()`

Places the player's symbol on the board.

```python
def make_move(board, move, player_symbol):
```

---

## `check_winner()`

Checks all possible winning combinations.

```python
def check_winner(board, player_symbol):
```

It returns `True` when the player has won and `False` when they have not.

---

## `is_board_full()`

Checks whether all nine positions have been filled.

```python
def is_board_full(board):
```

---

## `display_winner()`

Displays the winner message after a successful game.

```python
def display_winner(player_name, player_symbol):
```

---

## `display_draw()`

Displays the draw message when nobody wins.

```python
def display_draw():
```

---

## `play_game()`

Controls the main gameplay.

```python
def play_game(player_x, player_o):
```

This function manages:

* Board creation
* Player turns
* Player moves
* Win checking
* Draw checking
* Turn switching

---

## `play_again()`

Asks the players whether they want to start another game.

```python
def play_again():
```

---

## `display_menu()`

Displays the main menu.

```python
def display_menu():
```

---

## `display_rules()`

Displays the rules of Tic Tac Toe.

```python
def display_rules():
```

---

## `main()`

The `main()` function controls the overall application.

```python
def main():
```

It connects the different functions together and controls the main menu.

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

However, players interact with it using positions `1–9`:

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

The program stores the possible winning combinations in a list.

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

The program checks each combination after a player makes a move.

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
* Basic Game Logic

No external libraries or packages are required.

---

# Requirements

You only need:

* Python 3
* A terminal or command prompt
* A code editor

The project does not require any third-party dependencies.

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

The application will start in the terminal.

---

# How to Play

### Step 1 — Enter Player Names

When the program starts:

```text
Player X name:
Player O name:
```

Enter the names of both players.

---

### Step 2 — Open the Main Menu

You will see:

```text
1. Start Game
2. View Rules
3. View Scores
4. Change Player Names
5. Exit
```

Choose the desired option.

---

### Step 3 — Start the Game

Choose:

```text
1
```

The board position guide will appear.

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

---

### Step 4 — Make a Move

The current player enters a number from `1` to `9`.

Example:

```text
Jose (X) - choose a position (1-9):
> 5
```

The X symbol is placed in position 5.

---

### Step 5 — Continue Playing

Players take turns until:

* Player X wins
* Player O wins
* The game ends in a draw
* A player quits

---

### Step 6 — Check the Score

After a completed game, the scoreboard is updated.

Example:

```text
Jose (X): 1
Alex (O): 0
Draws:    0
```

Players can then choose whether to play again.

---

# Example Gameplay

```text
=============================================
              TIC TAC TOE
=============================================

Player X name: Jose
Player O name: Alex

=============================================
                MAIN MENU
=============================================
1. Start Game
2. View Rules
3. View Scores
4. Change Player Names
5. Exit
=============================================

Choose an option: 1
```

The game starts:

```text
       1   |   2   |   3
     -------+-------+-------
       4   |   5   |   6
     -------+-------+-------
       7   |   8   |   9

       |   |   
     -------+-------+-------
       |   |   
     -------+-------+-------
       |   |
```

Jose chooses position 5:

```text
Jose (X) - choose a position (1-9):
> 5
```

The board becomes:

```text
       |   |   
     -------+-------+-------
       | X |
     -------+-------+-------
       |   |
```

The game continues until there is a winner or a draw.

---

# Error Handling

The improved version handles several common input problems.

### Invalid Text

Input:

```text
hello
```

Output:

```text
Invalid input.
Please enter a number from 1 to 9.
```

### Number Too High

Input:

```text
20
```

Output:

```text
Invalid position.
Please choose a number from 1 to 9.
```

### Number Too Low

Input:

```text
0
```

Output:

```text
Invalid position.
Please choose a number from 1 to 9.
```

### Occupied Position

If a player selects a position already containing a symbol:

```text
That position is already taken.
Please choose another position.
```

### Quit

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

---

## Functions

The program is divided into multiple functions.

For example:

```python
def check_winner(board, player_symbol):
```

This makes individual parts of the program easier to understand.

---

## Loops

`while` loops keep the game running.

```python
while True:
```

`for` loops are used to check winning combinations.

---

## Conditional Statements

`if`, `elif`, and `else` statements control the game's logic.

They are used to determine:

* Whether a move is valid
* Whether a position is occupied
* Whether a player has won
* Whether the board is full
* Which player should play next

---

## Dictionaries

A dictionary is used to store the game scores.

```python
scores = {
    "X": 0,
    "O": 0,
    "Draws": 0
}
```

This allows the program to easily update and display scores.

---

## Tuples

Tuples are used to represent winning combinations.

```python
(0, 1, 2)
```

---

## String Methods

The program uses string methods such as:

```python
.strip()
```

and:

```python
.upper()
```

to clean and process user input.

---

## Boolean Values

The program uses `True` and `False` to determine whether conditions are satisfied.

For example:

```python
if check_winner(board, current_symbol):
```

---

## Modular Programming

One of the biggest improvements in Version 2 is the use of separate functions.

Instead of putting the entire game inside one large block of code, different responsibilities are separated.

```text
Display
   ↓
Input
   ↓
Validation
   ↓
Game Logic
   ↓
Score System
   ↓
Menu
```

This makes the project easier to expand in future versions.

---

# Current Limitations

Although the game has been improved significantly, it is still intentionally simple.

Current limitations include:

* The game is terminal-based.
* Both players need to use the same computer.
* There is no computer opponent.
* There is no AI.
* Scores are only stored while the program is running.
* Scores are not saved to a file or database.
* There is no graphical interface.
* There are no difficulty levels.
* There are no sound effects.

These limitations provide opportunities for future development.

---

# Future Improvements

The project can continue to grow into a more advanced application.

## Version 3 — Computer Opponent

Add a computer-controlled player.

Possible game modes:

```text
1. Player vs Player
2. Player vs Computer
```

---

## Version 4 — Difficulty Levels

Add different AI difficulties:

```text
Easy
Medium
Hard
Impossible
```

---

## Version 5 — Smarter AI

Implement the **Minimax algorithm** so the computer can analyze possible moves.

The hardest difficulty could be designed so that the computer cannot easily be defeated.

---

## Version 6 — Persistent Scoreboard

Save scores to a file so that they remain available after closing the program.

For example:

```text
scores.txt
```

---

## Version 7 — Graphical Interface

Create a graphical version using **Tkinter**.

Instead of typing:

```text
5
```

players could click directly on the board.

---

## Version 8 — Statistics

Add statistics such as:

* Total games
* Player X wins
* Player O wins
* Draws
* Win percentage
* Current winning streak
* Longest winning streak

---

## Version 9 — Database

Use SQLite to store:

* Player names
* Match history
* Scores
* Game results
* Statistics

This would turn the project into a more complete application.

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
[x] Add score tracking
[x] Add Play Again option
[x] Add Change Player Names
[x] Add quit option during a game
[x] Organize code into functions
[ ] Add computer opponent
[ ] Add AI difficulty levels
[ ] Add persistent scores
[ ] Add game statistics
[ ] Create graphical interface
[ ] Add SQLite database
```

---

# Learning Purpose

This project was created as part of my journey in learning **Python programming and software development**.

The first version of the project focused on learning the basic concepts needed to create a playable game. The improved version expands those concepts into a more structured application.

Through this project, I am practicing how to take a simple idea and gradually improve it by adding features, organizing code, handling errors, and improving the overall user experience.

This project also serves as an example of how a beginner Python project can evolve over multiple versions.

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
* Designing basic game logic
* Organizing code into separate functions
* Managing multiple game states
* Tracking scores
* Creating menu systems
* Improving an existing program instead of rebuilding it from scratch

---

# Project Goals

The long-term goal of this project is to continue improving it as my Python skills develop.

The project can eventually evolve from a simple terminal game into a complete Tic Tac Toe application with:

```text
Terminal Version
       ↓
Improved Terminal Version
       ↓
Computer Opponent
       ↓
AI Difficulty
       ↓
Graphical Interface
       ↓
Statistics
       ↓
Database
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
