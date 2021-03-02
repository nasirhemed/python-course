EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """

    # TODO: Your code here
    # Hint: if min_value <= value and value <= max_value, Do something

   
    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.

    pass

def game_board_full(game_board):
    """ (str) -> bool
    
    Return True if and only if all of the cells in the game board 
    have been chosen.
     
    >>> game_board_full("XOOXXOOX")
    True
    >>> game_board_full("XX-OO-XO-")
    False
    """
    # TODO: Your code here
    # Hint: Check if '-' is in the board
    pass

    
def get_board_size(game_board):
    """(str) -> int
    
    Return the length of each side of the given tic-tac-toe game board.
    
    >>> get_board_size("XXOOXXOOX")
    3
    >>> get_board_size("OOXX")
    2
    """
    
    # TODO: Your code here
    # Hint: A board is always a square
    # 3x3 board => 9 characters
    # 2x2 board => 4 characters
    # If you are given x^2 = n, how do you find x ?
    pass


def make_empty_board(size):
    """(int) -> str
    
    Return a string for storing information about a tic-tac-toe game board 
    whose size is given by the parameter.
    Each character in the returned string is to have been set to the EMPTY 
    character, to indicate that no cells have been chosen yet.
    
    >>> make_empty_board(2)
    "----"
    >>> make_empty_board(3)
    "---------"
    """

    # TODO: Your code here
    pass

def get_position(row_index, col_index, board_size):
    """(int, int, int) -> int
    
    Return the str_index of the cell in the string representation of 
    the game board corresponding to the given row and column indices.
    
    >>> get_position(2, 1, 2)
    2
    >>> get_position(1, 2, 2)
    1
    """
    # TODO: Your code here
    # Hint take a look at this board
    #    1   2  
    # 1  - | -
    #   ---+---
    # 2  O | -
    # Board Representation in string: "--0-"
    # Where is O located ?
    # The row_index is 2
    # The column index is 1
    # We want to return 2

    # More hints in the handout instruction
    
        
    pass    

def make_move(symbol, row, col, game_board):
    """(str, int, int, str) -> str
    
    Return the tic-tac-toe game board that results when the given symbol is 
    placed at the given cell position in the given tic-tac-toe game board.
    
    >>> make_move("O", 2, 1, "X--O")
    "X-OO"
    >>> make_move("X", 1, 2, "X--O")
    "XX-O"
    """
    
    # TODO: Your code here
    # Hint: Use get_position function to get the postion
    # Hint: Can we do s[position] = symbol ? This is a string
    # We will have to construct the string by ourselves
    # Use string slices and + to concatenate
    #   str[start:finish] + new_symbol + str[finish:end]
    pass

def extract_line(game_board, direction, row_or_column):
    """(str, str, int) -> str 
    
    Return the characters that make up the specified row 
    (when the second parameter is 'across'), 
    column (when the second parameter is 'down') or 
    diagonal from the given tic-tac-toe game board. 
    When the second parameter is 'down_diagonal' or 'up_diagonal', 
    the value of the third parameter should not be used, 
    since the 'down_diagonal' is known to start in 
    the upper-left corner of the game_board, 
    and the 'up_diagonal' is known to start in 
    the lower-left corner of the game_board.
    
    >>> extract_line("XXOO", "down", 2)
    "XO"
    >>> extract_line("XXXOOOXXX", "across", 1)
    "XXX"
    """
    game_board_size = int(len(game_board) ** 0.5)  
    #According to get_board_size function, get game board size again
    if direction == "across":  
        return game_board[game_board_size * (row_or_column - 1):
                          (game_board_size * (row_or_column - 1)) 
                          + game_board_size]
    #Use the result above and numbers of row or col, 
    #imagine the game board is a long string(started char's index is 0), 
    #find the regulation between row, col, size and position index, 
    #then use game_board[:] and get one of the rows in this board.     
    elif direction == "down": 
        return game_board[row_or_column - 1:
                          game_board_size * (game_board_size - 1) 
                          + row_or_column:game_board_size]
    #Use game board size and numbers of row or col, 
    #imagine the game board is a long string(started char's index is 0), 
    #find the regulation between row, col, size and position index, 
    #then use game_board[::] and get one of the columns in this board.     
    elif direction == "down_diagonal":  
        return game_board[::game_board_size + 1]
    #Use game board size and numbers of row or col, 
    #imagine the game board is a long string(starting char's index is 0), 
    #find the regulation between row, col, size and position index, 
    #then use game_board[::] and get down_diagonal in this board.     
    elif direction == "up_diagonal":  
        return game_board[game_board_size ** 2 - 
                          game_board_size:game_board_size - 2:
                          -(game_board_size - 1)]
    #Use game board size and numbers of row or col, 
    #imagine the game board is a long string(starting char's index is 0), 
    #find the regulation between row, col, size and position index, 
    #then use game_board[::] and get up_diagonal in this board.     
