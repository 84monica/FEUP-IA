from copy import deepcopy

class GameState:
    def __init__(self, board, move_history=[]):
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
        # returns the possible moves
        states = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                for shape in range(1, 4):
                    states.append(self.put_shape([row, col], shape))
        return states

    def put_shape(self, position, shape):
        # function that performs a move given the row and column number and returns the new state
        state = GameState(self.board, self.move_history)

        row, col = position[0], position[1]

        # checks if its possible 
        if (state.board[row][col] != 0):
            return None

        # updates board
        state.board[row][col] = shape

        # adds new state to move_history
        state.move_history.append(state.board)

        print(state.board)

        return state

    def row_palindrome(self, row_pos):
        # get row
        row = self.board[row_pos]

        # get row without zeros
        check_row = []
        for item in row:
            if item != 0:
                check_row.append(item)
        
        # check palindrome
        return check_row == check_row[::-1]

    def col_palindrome(self, col_pos):
        # get col without zeros
        col = []
        for i in range(len(self.board)):
            if self.board[i][col_pos] != 0:
                col.append(self.board[i][col_pos])

        # check palindrome
        return col == col[::-1]
    
    def is_palindrome(self):
        # checks if the board is palindrome
        for i in range(len(self.board)):
            if not (self.row_palindrome(i) and self.col_palindrome(i)):
                return False
        return True

    def print_move_history(self):
        print("History:\n")
        i = 1
        for state in self.move_history:
            print("move " + str(i) + ":")
            i += 1
            for row in state:
                print("        " + str(row))
            print("\n")

game = GameState([[0, 0, 0, 1, 2], 
                  [0, 0, 0, 2, 0], 
                  [3, 3, 3, 0, 3],
                  [0, 1, 1, 0, 3],
                  [0, 0, 2, 0, 0]])

game1 = GameState([[0, 0, 2, 1, 2], 
                  [2, 1, 1, 2, 0], 
                  [3, 3, 3, 0, 3],
                  [3, 1, 1, 1, 3],
                  [2, 0, 2, 0, 2]])

print(game.board)
print(game.move_history)
print(game.children()[0].board)
print(game.put_shape([1, 2], 3).board)
print(game.is_palindrome())

print(game1.is_palindrome())
