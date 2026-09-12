# Tic Tac Toe

A **Tic Tac Toe game built with Python**. This project started as a beginner-friendly terminal game and was expanded with additional gameplay features, computer difficulty levels, statistics, move tracking, and a **Minimax-powered Hard AI**.

The project is designed to practice Python fundamentals while also introducing more advanced concepts such as **recursion, algorithms, game-state evaluation, and basic statistics tracking**.

---

## About the Project

Tic Tac Toe is a classic two-player game played on a **3×3 board**.

Players take turns placing their symbol, either **X** or **O**, on an empty position. The goal is to be the first player to create a line of three matching symbols.

A winning line can be:

* Horizontal
* Vertical
* Diagonal

If all nine spaces are filled and nobody gets three in a row, the game ends in a **draw**.

This project allows the player to play against another person or against a computer with multiple difficulty levels.

---

## Features

### Game Modes

The game currently supports:

* **Player vs Player**
* **Player vs Computer**

In Player vs Player mode, two people can play against each other.

In Player vs Computer mode, the player competes against an AI opponent.

---

### Computer Difficulty

The computer has three difficulty levels:

#### Easy

The computer chooses from the available positions randomly.

This mode is designed for a simple and unpredictable opponent.

#### Medium

The computer uses basic game strategy.

It can:

* Look for a winning move
* Block the player's winning move
* Prefer the center
* Prefer corners
* Choose another available position when necessary

#### Hard

The Hard difficulty uses the **Minimax algorithm**.

Instead of simply choosing a random or strategically obvious move, the computer evaluates possible future game states to determine the strongest move.

This makes the Hard AI extremely difficult to beat and allows it to properly analyze the possible outcomes of the game.

---

## Minimax Algorithm

The Hard AI uses a recursive **Minimax algorithm**.

Minimax evaluates possible moves by simulating both sides of the game.

The computer attempts to:

* Maximize its chance of winning
* Minimize the player's chance of winning
* Recognize possible draws
* Evaluate future moves before making a decision

The scoring system considers:

* Computer wins
* Player wins
* Draws
* How quickly a win can be achieved

This feature introduces an important programming concept called **recursion**, where a function calls itself to solve smaller versions of the same problem.

---

## Player Names

Players can enter their own names before starting the game.

For example:

```text
Player X name: Jose
Player O name: Mark
```

The names are then displayed throughout the game and scoreboard.

If no name is entered, the game automatically uses:

* Player X
* Player O

---

## Position System

The game uses numbers from **1 to 9** to represent the board.

```text
          1   |   2   |   3
        -------+-------+-------
          4   |   5   |   6
        -------+-------+-------
          7   |   8   |   9
```

For example, entering:

```text
5
```

places the player's symbol in the center.

---

## Game Commands

During a player's turn, additional commands are available.

### Make a Move

Enter a number from:

```text
1 - 9
```

to select an empty board position.

### Undo

Enter:

```text
U
```

to undo the previous move.

In Player vs Player mode, the most recent move is removed.

In Player vs Computer mode, the most recent player/computer turn can be undone so the player can make another decision.

### Move History

Enter:

```text
H
```

to display the moves made during the current game.

Example:

```text
1. Jose (X) - Position 5
2. Computer (O) - Position 1
3. Jose (X) - Position 9
```

### Restart

Enter:

```text
R
```

to restart the current game.

The player is asked to confirm before the game restarts.

### Quit

Enter:

```text
Q
```

to leave the current game and return to the main menu.

---

## Move History

The game now records the moves made during each round.

Each move stores:

* Player name
* Player symbol
* Board position

This makes it easier to review how the game was played.

The move history is also displayed after a game ends.

---

## Winning Line Detection

When a player wins, the game identifies the three positions that created the winning combination.

For example:

```text
Winning positions: 1, 2, 3
```

This helps clearly show how the player won.

---

## Scoreboard

The game keeps track of the results of completed games.

The scoreboard displays:

* Player X wins
* Player O wins
* Draws
* Total games
* Win percentages

Example:

```text
Jose (X): 3 wins
Mark (O): 2 wins
Draws:     1
Games Played: 6
```

The game also calculates the percentage of games won by each player.

---

## Statistics

The game includes a statistics system that tracks gameplay information.

Statistics include:

* Total games
* Player X wins
* Player O wins
* Draws
* Total moves
* Average moves per game

The average number of moves is calculated based on the total number of moves made across completed games.

---

## Win Streaks

The expanded version also tracks player win streaks.

The game records:

* Current Player X streak
* Current Player O streak
* Best Player X streak
* Best Player O streak

For example:

```text
Jose Current Streak: 3
Mark Current Streak: 0

Jose Best Streak:    4
Mark Best Streak:    2
```

A player's streak resets when the other player wins or when a draw occurs.

---

## Move Statistics

The game tracks how many moves each player has made.

The extended statistics include:

```text
Player X Moves
Player O Moves
Total Moves
```

This provides additional information about how games are played.

---

## Round Tracking

The game keeps track of the current round number while the program is running.

This helps organize multiple games played during the same session.

---

## Extended Statistics

An additional statistics section provides more detailed information.

It includes:

* Total games
* Player X wins
* Player O wins
* Draws
* Player X moves
* Player O moves
* Total moves
* Current win streaks
* Best win streaks
* Games quit
* Average moves

This makes the project more than just a simple Tic Tac Toe game and introduces basic data tracking.

---

## Reset Scores

The main menu includes an option to reset the game's statistics.

When confirmed, the game resets:

* Player X wins
* Player O wins
* Draws
* Move statistics
* Win streaks
* Best streaks
* Games quit
* Total moves
* Round counter

A confirmation is required before resetting the data.

---

## Rules

The game follows the standard Tic Tac Toe rules:

1. The game uses a 3×3 board.
2. Players take turns placing X or O.
3. Players must select an empty position.
4. The first player to create three matching symbols in a row wins.
5. Winning lines can be horizontal, vertical, or diagonal.
6. If the board becomes full without a winner, the game ends in a draw.

---

## Main Menu

The expanded main menu contains:

```text
1. Start Game
2. View Rules
3. How To Play
4. View Scores
5. View Statistics
6. Change Player Names
7. Reset Scores
8. View Move Guide
9. View About
10. View Extended Statistics
11. Exit
```

This gives the player access to the game's different systems without needing to restart the program.

---

## Move Guide

The Move Guide explains the different types of board positions.

### Center

```text
5
```

### Corners

```text
1, 3, 7, 9
```

### Sides

```text
2, 4, 6, 8
```

This is especially useful for understanding the strategies used by the Medium and Hard computer opponents.

---

## About Section

The game includes an About section explaining the project and the Python concepts used to create it.

The project demonstrates:

* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Input validation
* Random selection
* Recursion
* Algorithms
* Game-state evaluation
* Statistics tracking

---

## Python Concepts Used

### Functions

The project is divided into multiple functions.

Examples include:

```python
create_board()
display_board()
check_winner()
play_game()
hard_computer_move()
```

This keeps different parts of the program organized.

### Lists

The board is stored as a Python list.

```python
board = [" " for _ in range(9)]
```

Each index represents a position on the Tic Tac Toe board.

### Dictionaries

Dictionaries are used to store information such as scores and move history.

Example:

```python
scores = {
    "X": 0,
    "O": 0,
    "Draws": 0
}
```

### Loops

Loops are used for:

* Game turns
* Menu navigation
* Input validation
* Checking available moves
* Searching for winning combinations

### Conditional Statements

`if`, `elif`, and `else` statements control the game's logic.

They are used to determine:

* Who won
* Whether the board is full
* Which player's turn it is
* Which difficulty is selected
* Whether a move is valid

### Random Module

The `random` module is used by the Easy AI and for random first-player selection.

```python
import random
```

### Recursion

The Hard AI uses recursion through the Minimax algorithm.

The algorithm repeatedly evaluates possible future board states until it reaches a winning, losing, or drawing position.

### Input Validation

The program checks whether the player's input is valid before making a move.

It prevents:

* Invalid numbers
* Letters when a position is expected
* Selecting positions outside 1–9
* Selecting occupied spaces

---

## Technologies Used

* **Python**
* Python Standard Library
* `random`
* `time`

No external Python packages are required.

---

## Project Structure

The project can be kept as a simple Python project:

```text
Tic Tac Toe/
│
├── main.py
│
└── README.md
```

The main game logic is contained in:

```text
main.py
```

---

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

You can check by opening a terminal and running:

```bash
python --version
```

### 2. Open the Project

Open the project folder in your preferred Python editor.

Examples:

* PyCharm
* Visual Studio Code
* IDLE

### 3. Run the Program

Run:

```bash
python main.py
```

The Tic Tac Toe main menu should appear.

---

## How a Game Works

The basic game flow is:

```text
Start Program
      ↓
Main Menu
      ↓
Start Game
      ↓
Choose Game Mode
      ↓
Choose Difficulty
      ↓
Choose First Player
      ↓
Create Board
      ↓
Player Makes Move
      ↓
Check Winner
      ↓
Check Draw
      ↓
Computer Makes Move
      ↓
Check Winner
      ↓
Check Draw
      ↓
Continue Until Game Ends
      ↓
Update Scores
      ↓
Display Statistics
      ↓
Play Again or Return to Menu
```

---

## Future Improvements

Possible future upgrades include:

* Graphical user interface
* Sound effects
* Background music
* Animated board
* Save statistics to a file
* Persistent leaderboard
* Player profiles
* Custom board sizes
* Online multiplayer
* Network multiplayer
* Tournament mode
* Best-of-three mode
* Best-of-five mode
* More advanced AI
* Difficulty customization
* Game replay system
* Match history
* Custom symbols
* Themes and colors

---

## Learning Goals

This project is intended to help practice Python programming through a real playable application.

The project demonstrates how simple programming concepts can be combined to create a more complete application.

The expanded version also provides an introduction to:

* Game development logic
* Algorithms
* Recursion
* Artificial intelligence
* Data structures
* State management
* Statistics
* Input validation

---

## Author

**Jose Navoa**

A beginner Python project created as part of learning programming and developing practical programming projects.

---

## License

This project is intended for educational and personal learning purposes.
