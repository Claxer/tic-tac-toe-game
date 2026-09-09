# Tic Tac Toe

A simple **Tic Tac Toe game built with Python**. This project is designed as a beginner-friendly programming project to practice basic Python concepts while creating a playable two-player game in the terminal.

## About the Project

Tic Tac Toe is a classic two-player game where players take turns placing **X** and **O** on a 3×3 board.

The goal is to be the first player to get three of the same symbols in a row, either:

* Horizontally
* Vertically
* Diagonally

The game automatically detects when a player wins or when the board ends in a draw.

## Features

* Two-player gameplay
* 3×3 Tic Tac Toe board
* Player turn switching
* Win detection
* Draw detection
* Prevents players from choosing occupied spaces
* Checks for invalid board positions
* Simple terminal-based interface
* Beginner-friendly Python code

## Technologies Used

* **Python**
* Lists
* Functions
* Loops
* Conditional statements
* User input

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

You can check by opening a terminal or command prompt and running:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/tic-tac-toe.git
```

Replace `your-username` with your GitHub username.

### 3. Open the Project Folder

```bash
cd tic-tac-toe
```

### 4. Run the Game

```bash
python tic_tac_toe.py
```

## How to Play

When the game starts, the board will look like this:

```text
   |   |
---+---+---
   |   |
---+---+---
   |   |
```

Choose a position from **1–9**.

The positions correspond to:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

For example, if Player X chooses `5`:

```text
   |   |
---+---+---
   | X |
---+---+---
   |   |
```

Players continue taking turns until someone wins or the game ends in a draw.

## Winning Conditions

A player wins by getting three of their symbols in a row.

### Horizontal

```text
 X | X | X
---+---+---
 O |   | O
---+---+---
   |   |
```

### Vertical

```text
 X | O |  
---+---+---
 X | O |  
---+---+---
 X |   |
```

### Diagonal

```text
 X | O |
---+---+---
   | X |
---+---+---
 O |   | X
```

## Python Concepts Practiced

This project helped practice several important Python fundamentals:

### Lists

The game board is stored inside a Python list.

```python
board = [" " for _ in range(9)]
```

### Functions

Functions are used to organize different parts of the game.

```python
def print_board():
```

```python
def check_winner(player):
```

### Loops

A `while` loop keeps the game running until a player wins or the game ends in a draw.

```python
while True:
```

### Conditional Statements

`if` statements are used to check things such as:

* Whether a move is valid
* Whether a space is occupied
* Whether a player has won
* Whether the board is full

### User Input

Players interact with the game by entering their chosen board position.

```python
input()
```

## Future Improvements

Possible improvements for future versions include:

* Computer opponent
* AI player
* Play Again option
* Score tracking
* Better input validation
* Difficulty levels
* Graphical user interface
* Game statistics
* Sound effects
* Custom player names

## Learning Purpose

This project was created as a **learning project** to strengthen my understanding of Python programming fundamentals.

It is one of my beginner projects as I continue learning programming and exploring different programming languages and technologies.

## Author

**Jose Manuel Navoa**

Information Technology Student

## License

This project is open for learning and educational purposes.
