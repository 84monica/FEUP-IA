from copy import deepcopy

class GameState:
    def __init__(self, board, move_history=[]):
        # initializer of the game state

        # board(list[list[int]]) - the state of the board
        # move_history(list[list[list[int]]]) - the history of the moves up until this state

        # 0 for empty space
        # 1 for triangle
        # 2 for rectangle
        # 3 for circle 

        self.board = deepcopy(board)

        # create an empty array and append move_history
        self.move_history = [] + move_history + [self.board]

    def children(self):
        # function that returns the possible moves

        states = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                for shape in range(1, 4):
                    state = self.put_shape([row, col], shape)
                    if state != None:
                        states.append(state)
        return states

    def check_put_shape(self, position, shape):
        # function that checks if its possible to put shape in a certain position 

        row, col = position[0], position[1]

        # there is an empty space
        if (self.board[row][col] != 0):
            return False

        # checks if piece type is already present on row or col
        piece_is_present = False
        for piece in self.board[row]: 
            if piece == shape:
                piece_is_present = True
        
        for piece in self.get_col(col):
            if piece == shape:
                piece_is_present = True
        
        if not piece_is_present:
            return False

        # check if row and col are already palindromes
        if (self.row_palindrome(row) and self.col_palindrome(col)):
            return False
        return True

    def put_shape(self, position, shape):
        # function that performs a move given the row and column number and returns the new state
        
        state = GameState(self.board, self.move_history)

        # checks if put shape is possible
        if not self.check_put_shape(position, shape):
            return None

        # updates board
        row, col = position[0], position[1]
        state.board[row][col] = shape

        return state

    def get_col(self, col_idx):
        # function that gets col given col index

        col = []
        for i in range(len(self.board)):
            col.append(self.board[i][col_idx])
        return col

    def remove_zeros(self, list):
        # function that remove zeros from list (to check later if its palindrome)

        final_list = []
        for item in list:
            if item != 0:
                final_list.append(item)
        return final_list

    def row_palindrome(self, row_pos):
        # function that checks if row is palindrome

        # get row
        row = self.board[row_pos]

        # get row without zeros
        row = self.remove_zeros(row)
        
        # check palindrome
        return row == row[::-1]

    def col_palindrome(self, col_pos):
        # function that checks if col  is palindrome

        # get col
        col = self.get_col(col_pos)

        # get col without zeros
        col = self.remove_zeros(col)

        # check palindrome
        return col == col[::-1]
    
    def is_palindrome(self):
        # function that checks if the board is palindrome

        for i in range(len(self.board)):
            if not (self.row_palindrome(i) and self.col_palindrome(i)):
                return False
        return True

    def print_move_history(self):
        # function that prints move history up until a certain point

        print("History:\n")
        i = 0
        for state in self.move_history:
            print("move " + str(i) + ":")
            i += 1
            for row in state:
                print("        " + str(row))
            print("\n")


# TESTING
game = GameState([[0, 0, 0, 1, 2], 
                  [0, 0, 0, 2, 0], 
                  [3, 3, 3, 0, 3],
                  [0, 1, 1, 0, 3],
                  [0, 0, 2, 0, 0]])


game1 = GameState([[0, 0, 0, 0, 0], 
                  [1, 0, 2, 0, 0], 
                  [1, 1, 1, 1, 0],
                  [0, 0, 0, 2, 3],
                  [0, 0, 3, 0, 3]])

game2 = GameState([[0, 0, 0, 0, 0], 
                  [3, 2, 0, 0, 0], 
                  [0, 2, 1, 0, 3],
                  [2, 0, 3, 1, 0],
                  [0, 0, 0, 2, 0]])

game3 = GameState([[1, 1, 0, 0, 0], 
                  [2, 0, 0, 0, 0], 
                  [0, 3, 3, 2, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 3, 0]])

game4 = GameState([[0, 0, 0, 3, 0], 
                  [3, 3, 0, 0, 0], 
                  [0, 0, 0, 0, 1],
                  [2, 1, 3, 0, 0],
                  [0, 0, 2, 0, 0]])

game5 = GameState([[1, 1, 0, 0, 0], 
                  [0, 2, 2, 0, 3], 
                  [0, 2, 0, 1, 2],
                  [3, 0, 3, 3, 0],
                  [0, 0, 0, 0, 0]])

easy_game = GameState([[0, 0, 0, 1, 2], 
                    [0, 0, 0, 2, 0], 
                    [3, 3, 3, 0, 3],
                    [3, 0, 1, 1, 3],
                    [2, 0, 2, 0, 2]])


def games():
    return (
        game,
        game1,
        game2,
        game3,
        game4,
        game5,
        easy_game
    )

# -------------------------------------------------
# TESTS
# -------------------------------------------------

# solution1 = GameState([[0, 0, 2, 1, 2], 
#                   [2, 1, 1, 2, 0], 
#                   [3, 3, 3, 0, 3],
#                   [3, 1, 1, 1, 3],
#                   [2, 0, 2, 0, 2]])

# print(game.board)
# print(game.move_history)

# Test Put Piece
# print(game.put_shape([1, 4], 1))
# print(game.put_shape([1, 0], 3))
# print(game.put_shape([1, 0], 4))
# print(game.put_shape([4, 3], 3))

# Test Print Move History
# state1 = game.put_shape([0, 0], 3)
# state2 = state1.put_shape([0, 1], 1)
# print(state2.print_move_history())

# Test Palindrome
# print(game.is_palindrome())
# print(game.col_palindrome(1))
# print(game.row_palindrome(4))
# print(solution1.is_palindrome())