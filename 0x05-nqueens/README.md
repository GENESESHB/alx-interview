0x05. N Queens
==============

AlgorithmPython

-   By: Alexa Orrico, Software Engineer at Holberton School

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `PEP 8` style (version 1.7.*)
-   All your files must be executable

Tasks
-----

### 0\. N queens

mandatory

![](http://www.crestbook.com/files/Judit-photo1_602x433.jpg)\
Chess grandmaster [Judit Polgár](https://alx-intranet.hbtn.io/rltoken/fZ1ecpPEmVL9nvkBn8WQGg "Judit Polgár"), the strongest female chess player of all time

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

-   Usage: `nqueens N`
    -   If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
-   where N must be an integer greater or equal to `4`
    -   If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
    -   If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
-   The program should print every possible solution to the problem
    -   One solution per line
    -   Format: see example
    -   You don't have to print the solutions in a specific order
-   You are only allowed to import the `sys` module

Read: [Queen](https://alx-intranet.hbtn.io/rltoken/ghWqI1wvx6g-Ul7nrufMKA "Queen"), [Backtracking](https://alx-intranet.hbtn.io/rltoken/-hgZbgRFkwmxaKnLnCIuEQ "Backtracking")

```
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$

```

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x05-nqueens`
-   File: `0-nqueens.py`


# task:
1. **Shebang Line**: This line specifies the interpreter to be used for running the script.

```python
#!/usr/bin/python3
```

2. **Docstring**: This triple-quote string provides documentation for the script. It describes what the script does.

```python
"""N Queens"""
```

3. **Imports**: The script imports the `sys` module. This module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. 

```python
import sys
```

4. **Function Definitions**:
   
   a. `print_board`: This function prints the positions allocated to the queen on the chessboard.

   ```python
   def print_board(board, n):
       """Print allocated positions to the queen"""
       b = []

       for i in range(n):
           for j in range(n):
               if j == board[i]:
                   b.append([i, j])
       print(b)
   ```
   
   b. `is_position_safe`: This function checks if the position is safe for the queen.

   ```python
   def is_position_safe(board, i, j, r):
       """Checks if the position is safe for the queen"""
       return board[i] in (j, j - i + r, i - r + j)
   ```
   
   c. `safe_positions`: This function finds all safe positions where the queen can be allocated.

   ```python
   def safe_positions(board, row, n):
       """Find all safe positions where the queen can be allocated"""
       if row == n:
           print_board(board, n)
       else:
           for j in range(n):
               allowed = True
               for i in range(row):
                   if is_position_safe(board, i, j, row):
                       allowed = False
               if allowed:
                   board[row] = j
                   safe_positions(board, row + 1, n)
   ```
   
   d. `create_board`: This function generates the board.

   ```python
   def create_board(size):
       """Generates the board"""
       return [0 * size for i in range(size)]
   ```

5. **Input Validation**:
   
   a. The script checks if the command-line arguments are valid.

   ```python
   if len(sys.argv) != 2:
       print("Usage: nqueens N")
       exit(1)
   ```
   
   b. It tries to parse the input argument as an integer.

   ```python
   try:
       n = int(sys.argv[1])
   except BaseException:
       print("N must be a number")
       exit(1)
   ```

   c. It checks if the value of `n` is at least 4.

   ```python
   if (n < 4):
       print("N must be at least 4")
       exit(1)
   ```

6. **Board Initialization and Function Call**:
   
   The script initializes the board and calls the `safe_positions` function with the initial row and board size as parameters.

   ```python
   board = create_board(int(n))
   row = 0
   safe_positions(board, row, int(n))
   ```

This script essentially solves the N Queens problem, which is to place N chess queens on an N×N chessboard so that no two queens threaten each other. It recursively finds all possible placements of queens on the board where they do not threaten each other.
