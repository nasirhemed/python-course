# Assignment 1

Goals of this assignment
------------------------

-   Practice learning about a problem domain in order to write code about that domain.
-   Use the Function Design Recipe to plan, implement, and test functions.
-   Write function bodies using variables, numeric types, strings, and conditional statements. (You can do this whole assignment with only the concepts from Weeks 1, 2, 3, and 4 of the course.)
-   Learn to use Python 3, provided starter code, a type-check module, and other tools.

Tic-Tac-Toe
-----------

Tic-tac-toe is a two-player game that children often play to pass the time. The game is usually played using a 3-by-3 game board. Each player has a symbol to play with (usually an **X** or an **O**) and the goal is to be the first player to place 3 of their symbols in a straight line on the game board (either across a row on the board, down a column or along one of the two main diagonals). The game may be known to you by another name, for example, as ''Noughts and Crosses'', or ''X's and O's''. The Wikipedia page [Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) (have a look!) provides a good description of the game and its rules.

In this Assignment, you are to complete some functions that make up part of a larger program for playing tic-tac-toe. In the program, game boards are not restricted to being 3-by-3, but are instead N-by-N, where N is one of the integers from 1 through 9, inclusive. Our game boards will **always** be square. When you have completed your functions for this Assignment, you will be able to play games of tic-tac-toe on your computer! The graphics won't be fancy, but we think that's okay, since the purpose of the assignment is to give you some practice with the parts of Python that you will learn in the first few weeks of the course.

Preliminary details and terminology
-----------------------------------

So far in the course, you have learned how to use variables to refer to objects that hold a single numerical or logical value, or a string of characters. For this assignment, we'll use what you've learned so far to write code that works with variables that refer to objects that represent game boards. We can think of our tic-tac-toe game boards as looking like this:
```
 X | O | X
---+---+---
   | O | X
---+---+---
 O | X |
 ```

To get started, we will need some terminology so that we can discuss tic-tac-toe game boards and their parts.

Let's describe the game board given above as being a 3-by-3 grid of **cell**s. We will say that the **game board size** is 3, since the number of cells along each side of the board is 3. There are 3 cells in each horizontal **row** of the board, and 3 cells in each vertical **column**. There are two main diagonals on the board, the **down_diagonal** that runs from the upper-left corner to the bottom-right corner, and the **up_diagonal** that runs from the bottom-left corner to the upper-right corner.

We will need a way to describe the position of each cell on the board. This can be done by using an ordered pair of numbers, representing row and column indices. In the example board above, the **first row** (the row with row index 1) has a cell with an X (in the column with column index 1), a cell with an O (column index 2), and another cell with an X (column index 3). The **second column** has two cells containing O's (row indices 1 and 2), and a cell containing an X (row index 3). The down_diagonal contains, in order, an X, an O and an empty cell, while the up_diagonal contains, in order, an O, another O and an X. For each cell in our example 3-by-3 board, the row index will be either 1, 2, or 3, and the column index will also be either 1, 2 or 3. The cell in position (row, column) = (1, 2) contains an O, while the cell in position (row, column) = (3, 3) is empty. **If at this point you are confused by the terminology, ask a question in class or on Piazza!** You will have a hard time completing the assignment if you don't understand the terms that have been used!

Representing the game board
---------------------------

When representing a game board like the one above in a program, we only need to store the contents of each cell, not the divider symbols (i.e., `|`, `-`, and `+`) that are used to separate cells when game boards are displayed. This leaves us with a game board that looks like this:
```
XOX
 OX
OX
```
It can be difficult to interpret boards that contain a lot of empty cells, so let's use the hyphen symbol `-` to fill empty cells, as shown below:
```
XOX
-OX
OX-
```
We have not yet studied how to store 2-dimensional information in Python programs, so we will need a different way to represent our game board. The approach that we will take for this Assignment is to store the rows one after another, starting with the first row. For the example board above, we would get:
```
XOX-OXOX-
```
And how might we store this information? We will use a Python `str`. With these choices, the Python statement:
```
game_board = 'X-OX'
```
creates a variable named `game_board` that refers to the `str` object with length 4 `'X-OX'`, which represents a 2-by-2 game board that looks like this:
```
 X | -
---+---
 O | X
```
Accessing cells
---------------

We have used row **and** column indices to describe the position of each cell in the grid representation of a game board. But each character in a Python `str` is in a position that is described by a single index. How is the Python program going to translate between row and column indices and `str` indices? To answer this question, we will have to determine a formula!

One good way to figure out the formula is to play with a concrete example. Suppose a game board was 4-by-4, and that each cell was filled with a different letter from A through P. (Yes, in a tic-tac-toe game, only two symbols would be used, but for this example, it helps to put a different letter in each cell.) The grid representation could look like this:

ABCD
EFGH
IJKL
MNOP

and then the `str` representation would look like this:

'ABCDEFGHIJKLMNOP'

Consider the same grid representation as above, with index labels added:

|  | 1 | 2 | 3 | 4 |
| --- | --- | --- | ---| ---|
| 1 | A | B | C | D |
| 2 | E | F | G | H |
| 3 | I | J | K | L |
| 4 | M | N | O | P |

... and the string representation from above, again with index labels added:

| str_index |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 | 11 | 12 | 13 | 14 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| str | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P |

We now explore how `str_index` changes as we move across a row and down a column. This will help us determine a formula that relates row and column indices and `str` indices.

In the example above, we see that the character in the cell with position (row, column) = (2,1) has `str_index` 4. The other cells in that row have `str` indices 5, 6 and 7. We conclude that when moving one cell across a row, the `str_index` increases by 1. The cells in the column with column index 3 have `str` indices 2, 6, 10 and 14. Moving one cell down a column increases the `str_index` by 4, the size of the game board. We conclude that when moving one cell down a column, the `str_index` increases by the game board size.

We now introduce variables that will allow us to express the formula explicitly.

Let a variable named `str_index` refer to the position of a cell in the `str` representation of a game board with size `board_size`, and let variables `row_index` and `col_index` refer to the position of the same cell in the grid representation of a game board. From what we have seen, we can conclude that `str_index` depends on `row_index`, `col_index` and `board_size`.

Plugging in a few examples will show that the following formula will compute `str_index`, given a `row_index`, `col_index` and `board_size`:

    str_index == (row_index - 1) * board_size + (col_index - 1)

(The minus `1`'s are needed for the arithmetic to work out. This is because we chose to index our rows and columns starting at 1. As a thought exercise, what would the formula be if we chose to index the rows and columns starting at 0?)

Now that we have described how our tic-tac-toe game boards can be stored in a Python program, we move to a discussion of what files to download, and then a specification of the functions that you will need to write to complete your Assignment solution.

Files to download
-----------------

All of the files that you need to download for the assignment are listed in this section. These files must all be placed in the same folder. Download the files by right-clicking on the link and using your web-browser's "Save as" option. Do not use "cut and paste" as sometimes this can cause undesirable (and possibly hidden) formatting characters to be added to the Python code.

-   Starter code is code that we provide for you to revise and turn into a complete assignment solution. The starter code for this assignment is in a file named `tictactoe_functions.py`. Download and save this file. Complete it by following the instructions in the **What to do** section of this handout (see below).

-   [tictactoe_functions.py]()

-   The main game playing code is in a file named `tictactoe_program.py`. Download and save this file. **Do not change this file** as it is complete. You will be able to play a game of tic-tac-toe after completing `tictactoe_functions.py` and then running the `tictactoe_program.py` file.

-   [tictactoe_program.py]()

-   The Assignment 1 simple check code is in a file named `a1_simple_check.py`. Download and save this file. It is complete and must not be changed. More details on this code are given below.

-   [a1_simple_check.py]()

What to do
----------

In the starter code file `tictactoe_functions.py`, complete the following function definitions.

We have included the type contracts in the table below. We will be evaluating your docstrings in addition to your code. You must include two examples in your docstrings. You will need to paraphrase the full descriptions of the functions to get an appropriate docstring decscription; copying and pasting what you see in the table below is not sufficient. Check the steps of the Function Design Recipe to make sure you have properly paraphrased.

You may care to read through `tictactoe_program.py` to see how the functions that you will write can be used. The code in the `tictactoe_program.py` file uses Python statements that you may not have learned yet, so don't worry if you do not understand it fully.

Examination of the provided `tictactoe_functions.py` starter code file will show that it starts with the definition of the named constant variable `EMPTY` (which refers to the character used to show that a tic-tac-toe game board cell has not been chosen), and a complete docstring for the `is_between` function. In your Assignment 1 solution, **do not** change the code that we have provided. You are to **add your Python statements** to this starter code file and fulfill the requirements listed in the table below.

| Function name | Full Description |
| --- | --- |
| `is_between` | The first parameter refers to a numerical value, the second to the minimum value for a range of values, and the third to the maximum value for a range of values. Assume that the value of the second parameter is less than or equal to the value of the third parameter. (That means that, when you write your code, you don't need to worry about other situations.) This function is to return `True` if and only if the value of the first parameter is not less than the second parameter and not more than the third parameter. In other words, `True` is returned if and only if the first parameter is between the second and third parameters, or equal to one or both of them. (More formally, it lies in the [closed interval](https://www.thefreedictionary.com/closed+interval) [second parameter, third parameter].) |
| `game_board_full` | The parameter refers to a valid tic-tac-toe game board. This function is to return `True` if and only if all of the cells in the game board have been chosen. That is, `True` is returned if and only if there are no EMPTY characters in the game board. (See above for discussion of the EMPTY character.) |
| `get_board_size` | The parameter refers to a valid tic-tac-toe game board. Given that our tic-tac-toe game boards are square, this means that the length of the parameter is a [perfect square](https://www.mathsisfun.com/definitions/perfect-square.html). This function is to return the length of each side of the given tic-tac-toe game board. NOTE: Make sure that your `get_board_size` function's return type is correct. |
| `make_empty_board` | The parameter refers to the size of a valid tic-tac-toe game board. You may assume that its value is ≥ 1 and ≤ 9. This function is to return a string for storing information about a tic-tac-toe game board whose size is given by the parameter. Each character in the returned string is to have been set to the EMPTY character, to indicate that no cells have been chosen yet. |
| `get_str_index` | The first and second parameters refer to the row and column indices, respectively, of a cell in a valid tic-tac-toe game board whose size is given by the third parameter. You may assume that the parameters refer to valid values. This function is to return the `str_index` of the cell in the string representation of the game board corresponding to the given row and column indices. |
| `make_move` | The first parameter refers to a one character string containing a symbol (usually, but not necessarily, an 'X' or 'O'). The second and third parameters refer to row and column indices, respectively, of a cell in the valid tic-tac-toe game board refered to by the fourth parameter. This function is to return the tic-tac-toe game board that results when the given symbol is placed at the given cell position in the given tic-tac-toe game board. |

#### No printing, input or import!

The final version of your `tictactoe_functions.py` file should contain the starter code, plus the function definitions specified above. Your `tictactoe_functions.py` file must *not* contain any statements that call the functions `print` or `input`. Also, do *not* include any extra code outside of the function definitions. And do *not* add any import statements.

#### Want to earn a good mark? Test your work!

You should carefully verify your code *before submitting* to determine whether it works: the Test step of the Function Design Recipe is particularly important for assignments. Once the deadline has passed, we will run our own set of tests on your submission, and use the results to help determine your assignment solution's grade.

To test your work, you should call each function with a variety of different arguments and check that the function returns the correct value in each case. This can be done in the shell or using another `.py` file, but must not be done in `tictactoe_functions.py`. Don't forget to test your functions with game boards of different sizes.

#### A simple check program

We are providing a simple program that can be used to test whether your functions have both the correct number of parameters and the correct return type, and also work correctly for one simple case. To use the simple check program, place the file `a1_simple_check.py` in the **same** folder as your `tictactoe_functions.py` file and run it.

**If** running the simple check program produces a report starting with `Yippee! The simple checker program completed without error.`, you can conclude the the function parameters and return types match the assignment specifications, and that the functions each work correctly for one simple case. **This does not mean that your code works correctly in all situations.** We will do a thorough job of testing your code once you hand it in, so be sure to thoroughly test your code yourself before submitting.

**Otherwise,** if running the simple check program does **not** produce the **Yippee!** message, look carefully at the message(s) provided by the simple check program. One or more of your parameter definitions or return types does not match the assignment specification, or your functions may return the wrong result or cause Python to crash. Fix your code and re-run the simple check program. Make sure the simple check program produces the **Yippee!** message before submitting your solution.

Evaluation
----------

The following aspects of your work will be graded:

-   **Correctness:** Your functions should work as specified. Correctness, as measured by our tests, will count for the largest part of your assignment grade. If your code does not execute when we test it, your Correctness grade will be zero. Make sure that you do not introduce typos when making last minute changes. Run your code before submitting!
-   **Commenting and docstrings**: We want to see great docstrings and internal comments. 

What to hand in
---------------

**The very last thing you do before submitting should be to run the `a1_simple_check.py` program one last time.** Otherwise, you could make a small error in your final changes before submitting that causes your code to receive zero for correctness.

Submit your `tictactoe_functions.py` file according to the instructions on the course website. Remember that spelling of filenames, including case, counts: your file must be named exactly as above.