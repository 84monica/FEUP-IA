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
        
        return []

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

        return state
    
    def is_palindrome(self):
        # checks if the board is complete
        return True

game = GameState([[0, 0, 0, 1, 2], 
                  [0, 0, 0, 2, 0], 
                  [3, 3, 3, 0, 3],
                  [0, 1, 1, 0, 3],
                  [0, 0, 2, 0, 0]])

print(game.board)
print(game.move_history)
print(game.put_shape([1, 2], 3).board)