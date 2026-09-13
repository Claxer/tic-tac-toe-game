# Tic Tac Toe

A **Tic Tac Toe game built with Python**. This project started as a beginner-friendly terminal game and was expanded into a more complete Tic Tac Toe game system with computer difficulty levels, statistics, achievements, challenges, match history, tournaments, leaderboards, game timers, and a **Minimax-powered Hard AI**.

The project is designed to practice Python fundamentals while also introducing more advanced concepts such as **recursion, algorithms, game-state evaluation, file handling, JSON data storage, statistics tracking, and game management**.

---

## About the Project

Tic Tac Toe is a classic two-player game played on a **3×3 board**.

Players take turns placing their symbol, either **X** or **O**, on an empty position. The goal is to be the first player to create a line of three matching symbols.

A winning line can be:

* Horizontal
* Vertical
* Diagonal

If all nine spaces are filled and nobody gets three in a row, the game ends in a **draw**.

The game allows players to compete against another person or against a computer with multiple difficulty levels.

The expanded version also includes a **Game Center** where players can view achievements, challenges, match history, leaderboards, advanced statistics, and tournament options.

---

# Features

## Game Modes

The game supports:

* **Player vs Player**
* **Player vs Computer**

### Player vs Player

Two players can compete against each other on the same computer.

Each player can enter their own name and choose their moves.

### Player vs Computer

A player can compete against the computer.

The computer has three different difficulty levels.

---

# Computer Difficulty

## Easy

The Easy AI chooses randomly from the available board positions.

This makes it suitable for beginners and creates a simple, unpredictable opponent.

---

## Medium

The Medium AI uses basic strategy.

It can:

* Look for a winning move
* Block the player's winning move
* Prefer the center
* Prefer corners
* Choose another available position when necessary

This makes the computer more strategic than Easy mode without being unbeatable.

---

## Hard

The Hard AI uses the **Minimax algorithm**.

The computer analyzes possible future game states before deciding which move to make.

This makes the Hard AI extremely difficult to beat.

---

# Minimax Algorithm

The Hard AI uses a recursive **Minimax algorithm**.

Minimax evaluates possible moves by simulating both sides of the game.

The computer attempts to:

* Maximize its chance of winning
* Minimize the player's chance of winning
* Recognize possible draws
* Evaluate future moves
* Select the strongest available move

The scoring system considers:

* Computer wins
* Player wins
* Draws
* How quickly a win can be achieved

This introduces the programming concept of **recursion**, where a function calls itself to evaluate smaller versions of the same problem.

---

# Player Names

Players can enter their own names before starting the game.

Example:

```text
Player X name: Jose
Player O name: Mark
```

The names are displayed throughout the game and scoreboard.

If no name is entered, the program automatically uses:

```text
Player X
Player O
```

---

# Position System

The game uses numbers from **1 to 9** to represent the board.

```text
          1   |   2   |   3
        -------+-------+-------
          4   |   5   |   6
        -------+-------+-------
          7   |   8   |   9
```

For example:

```text
5
```

places the player's symbol in the center.

---

# Game Commands

During a player's turn, additional commands are available.

## Make a Move

Enter a number from:

```text
1 - 9
```

to select an empty position.

---

## Undo

Enter:

```text
U
```

to undo the previous move.

In Player vs Player mode, the most recent move is removed.

In Player vs Computer mode, the most recent player/computer turn can be undone so the player can make another decision.

---

## Move History

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

---

## Restart

Enter:

```text
R
```

to restart the current game.

The program asks for confirmation before restarting.

---

## Quit

Enter:

```text
Q
```

to leave the current game and return to the main menu.

---

# Move History

The game records the moves made during each round.

Each move stores:

* Player name
* Player symbol
* Board position

The move history can be viewed during the game and is also displayed when a game ends.

This allows players to review how the match was played.

---

# Winning Line Detection

When a player wins, the game identifies the three positions responsible for the winning combination.

Example:

```text
Winning positions: 1, 2, 3
```

This makes it clear how the winning line was created.

---

# Scoreboard

The game tracks completed matches.

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

# Statistics

The game contains a statistics system that tracks gameplay information.

Statistics include:

* Total games
* Player X wins
* Player O wins
* Draws
* Total moves
* Average moves per game
* Player move totals
* Current win streaks
* Best win streaks
* Games quit

---

# Win Streaks

The game tracks consecutive wins.

It records:

* Current Player X streak
* Current Player O streak
* Best Player X streak
* Best Player O streak

Example:

```text
Jose Current Streak: 3
Mark Current Streak: 0

Jose Best Streak:    4
Mark Best Streak:    2
```

A player's current streak resets when the other player wins or when a draw occurs.

---

# Game Center

The newest version introduces a dedicated **Game Center**.

The Game Center provides additional systems outside the normal game.

It includes:

* Achievements
* Challenges
* Match History
* Leaderboard
* Tournament Mode
* Advanced Statistics
* Game performance records

The Game Center makes the project feel more like a complete game application instead of only a basic Tic Tac Toe program.

---

# Achievements

The game includes an **Achievement System**.

Achievements are unlocked by completing specific actions or milestones.

Examples include:

* Winning your first game
* Reaching multiple wins
* Building a win streak
* Playing multiple games
* Winning difficult matches
* Completing special challenges

When an achievement is unlocked, the game displays a special notification.

Example:

```text
=======================================================
              ACHIEVEMENT UNLOCKED!
=======================================================
```

Achievements provide additional goals for players beyond simply winning individual matches.

---

# Challenges

The game includes a **Challenge System**.

Challenges give players additional objectives to complete while playing.

Examples can include goals related to:

* Winning games
* Winning within a certain number of moves
* Creating specific winning patterns
* Reaching certain milestones
* Defeating difficult computer opponents

Completed challenges are tracked by the Game Center.

Example:

```text
=======================================================
                CHALLENGE COMPLETE!
=======================================================
```

This gives players additional reasons to keep playing and experimenting with different strategies.

---

# Match History

The game keeps a record of completed matches.

Match history can show information such as:

* Match number
* Players
* Game mode
* Winner
* Result
* Number of moves
* Difficulty when playing against the computer
* Game duration

Example:

```text
Game #1
Jose vs Computer
Result: Jose Wins
Moves: 7
```

This allows players to review previous games.

---

# Game Timer

The expanded version includes a **game timer**.

The timer records how long a game takes.

The game can use this information to track performance records such as:

* Fastest win
* Game duration
* Longest games by moves

Example:

```text
Game Time: 18.42 seconds
```

This adds another way for players to challenge themselves.

---

# Fastest Win

The Game Center keeps track of the player's fastest recorded winning game.

Example:

```text
Fastest Win: 12.45 seconds
```

Players can attempt to beat their previous record.

---

# Longest Game

The program also tracks the longest completed game based on the number of moves.

Example:

```text
Longest Game: 9 moves
```

This can be useful for comparing different matches and seeing how long games typically last.

---

# Persistent Game Center Data

The newest version can save Game Center information to a JSON file.

The save file is:

```text
tic_tac_toe_data.json
```

This allows selected Game Center information to remain available even after the program is closed.

The program can load previously saved data when it starts and save updated information as the player progresses.

---

# JSON Data Storage

The project uses Python's built-in `json` module to handle saved Game Center information.

Example:

```python
import json
```

JSON is used because it provides a simple way to store structured data in a readable file.

This introduces another practical Python concept beyond the original game logic.

---

# Leaderboard

The Game Center includes a **Leaderboard** system.

The leaderboard can be used to compare player performance.

Information can include:

* Player names
* Wins
* Losses
* Draws
* Win rate
* Best streak
* Total games

This gives the game a more competitive feeling.

---

# Tournament Mode

The expanded version includes a **Tournament Mode**.

Players can select a tournament format such as:

* Best of 3
* Best of 5
* Best of 7

The game keeps track of tournament wins until one player reaches the required number of victories.

For example, in a Best of 5 tournament:

```text
Player X: 3
Player O: 1

Player X is the Tournament Champion!
```

Tournament Mode turns multiple individual games into one larger competition.

---

# Advanced Statistics

The Game Center provides additional statistics beyond the original scoreboard.

It can track:

* Total games
* Total wins
* Total draws
* Total moves
* Average moves
* Current streak
* Best streak
* Games quit
* Fastest win
* Longest game

This allows players to examine their overall performance.

---

# Round Tracking

The program keeps track of the round number while the game session is active.

This helps organize multiple games during the same session.

---

# Reset Scores

The main menu contains an option to reset the current game statistics.

When confirmed, the program can reset information such as:

* Player X wins
* Player O wins
* Draws
* Move statistics
* Current streaks
* Best streaks
* Games quit
* Total moves
* Round counter

A confirmation is required before resetting the information.

---

# Rules

The game follows standard Tic Tac Toe rules:

1. The game uses a 3×3 board.
2. Players take turns placing X or O.
3. Players must select an empty position.
4. The first player to create three matching symbols in a row wins.
5. Winning lines can be horizontal, vertical, or diagonal.
6. If the board becomes full without a winner, the game ends in a draw.

---

# Main Menu

The main menu provides access to the original game systems and the expanded Game Center features.

The original menu includes options such as:

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

The expanded version also provides access to the additional Game Center systems.

---

# Move Guide

The Move Guide explains the different types of board positions.

## Center

```text
5
```

## Corners

```text
1, 3, 7, 9
```

## Sides

```text
2, 4, 6, 8
```

This is useful for understanding basic Tic Tac Toe strategy and the decisions used by the Medium and Hard AI.

---

# About Section

The game includes an About section describing the project and the Python concepts used.

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
* Statistics
* File handling
* JSON data storage
* Game management

---

# Python Concepts Used

## Functions

The project is divided into many functions.

Examples include:

```python
create_board()
display_board()
check_winner()
play_game()
hard_computer_move()
```

Functions allow different parts of the program to be separated and organized.

---

## Lists

The Tic Tac Toe board is stored as a Python list.

```python
board = [" " for _ in range(9)]
```

Each index represents one position on the board.

---

## Dictionaries

Dictionaries are used to store information such as scores, statistics, move history, and saved game data.

Example:

```python
scores = {
    "X": 0,
    "O": 0,
    "Draws": 0
}
```

---

## Loops

Loops are used for:

* Game turns
* Menu navigation
* Input validation
* Checking available moves
* Searching for winning combinations
* Tournament games
* Repeated challenges and game systems

---

## Conditional Statements

`if`, `elif`, and `else` statements control the game's logic.

They determine:

* Who won
* Whether the board is full
* Whose turn it is
* Which difficulty was selected
* Whether a move is valid
* Whether an achievement has been unlocked
* Whether a challenge has been completed
* Whether a tournament has ended

---

## Random Module

The `random` module is used by the Easy AI and for random first-player selection.

```python
import random
```

---

## Time Module

The `time` module is used for:

* Computer thinking delays
* Game timing
* Measuring game duration

```python
import time
```

---

## JSON

The `json` module is used to save and load Game Center information.

```python
import json
```

The saved information is stored in:

```text
tic_tac_toe_data.json
```

---

## Recursion

The Hard AI uses recursion through the Minimax algorithm.

The algorithm repeatedly evaluates possible future board states until it reaches a winning, losing, or drawing position.

---

## Algorithms

The project uses algorithms to determine:

* Winning combinations
* Available moves
* Winning moves
* Blocking moves
* Best AI decisions
* Tournament results
* Player statistics
* Achievement progress

---

## Input Validation

The program checks user input before performing actions.

It prevents problems such as:

* Invalid numbers
* Invalid menu selections
* Selecting positions outside 1–9
* Selecting occupied spaces
* Invalid commands

---

# Technologies Used

* **Python**
* Python Standard Library
* `random`
* `time`
* `json`

No external Python packages are required.

---

# Project Structure

The project can be kept as a simple Python project:

```text
Tic Tac Toe/
│
├──python-version
    ├── game.py
│
├── LICENSE
└── README.md
```

The main game logic is contained in:

```text
main.py
```

The JSON file stores persistent Game Center information when created by the program.

---

# How to Run

## 1. Install Python

Make sure Python is installed on your computer.

Check your Python installation using:

```bash
python --version
```

---

## 2. Open the Project

Open the project folder in your preferred Python editor.

Examples:

* PyCharm
* Visual Studio Code
* IDLE

---

## 3. Run the Program

Run:

```bash
python main.py
```

The Tic Tac Toe main menu should appear.

---

# How a Normal Game Works

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
Update Statistics
      ↓
Check Achievements
      ↓
Check Challenges
      ↓
Save Game Center Data
      ↓
Display Results
      ↓
Play Again or Return to Menu
```

---

# Game Center Flow

The expanded systems follow a larger flow:

```text
                 GAME CENTER
                      ↓
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
 Achievements    Challenges    Match History
        ↓             ↓             ↓
        └─────────────┼─────────────┘
                      ↓
                 Statistics
                      ↓
                 Leaderboard
                      ↓
              Tournament Mode
                      ↓
               Saved Game Data
```

---

# Learning Goals

This project is designed to help practice Python programming through a real playable application.

The original game demonstrates basic programming concepts while the expanded version introduces more advanced ideas.

The project provides practice with:

* Game development logic
* Artificial intelligence
* Algorithms
* Recursion
* Data structures
* State management
* Statistics
* File handling
* JSON data
* Persistent information
* Input validation
* Game timers
* Achievement systems
* Tournament systems

---

# Why This Project Was Expanded

The original goal of the project was to create a simple Tic Tac Toe game.

As new features were added, the project evolved into a larger application that demonstrates how a simple Python game can be expanded with:

* AI
* Player statistics
* Achievements
* Challenges
* Match records
* Competitive systems
* Persistent data
* Tournaments

The project therefore serves as both a playable game and a practical Python learning project.

---

# Future Improvements

Possible future upgrades include:

* Graphical user interface
* Sound effects
* Background music
* Animated board
* Custom themes
* Custom symbols
* Larger board sizes
* Online multiplayer
* Network multiplayer
* Player accounts
* Cloud-based leaderboard
* More AI personalities
* More AI difficulty levels
* Replay system
* Full game replays
* Custom challenges
* More achievements
* Player profiles
* Statistics graphs
* Game data export
* Web version
* Mobile version

---

# Author

**Jose Navoa**

A beginner Python project created for learning programming, practicing Python concepts, and developing practical programming projects.

---

# License

This project is intended for educational and personal learning purposes.
