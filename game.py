from copy import deepcopy
import time
import heapq

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

# Uninformed Search Methods
def breadth_first_search(problem):
    # solves game using bfs

    # problem(GameState) - the initial state
    queue = [problem]
    visited = set() # to not visit the same state twice

    while queue:
        state = queue.pop()
        visited.add(state)

        if state.is_palindrome():
            return state.move_history

        for child in state.children():
            if child not in visited:
                queue.append(child) 
    return None

def depth_first_search(problem):
    return None

def iterative_deepening(problem):
    return None

def uniform_cost(problem):
    return None

# Heuristics Functions
def h1(state):
    # number of rows and columns that aren’t palindromes / 2
    total = 0
    for i in range(len(state.board)):
            if not (state.row_palindrome(i)):
                total += 1
            if not (state.col_palindrome(i)):
                total += 1
    return total / 2

# Heuristic Search Methods
def greedy_search(problem, heuristic):
    # problem (NPuzzleState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer
    setattr(GameState, "__lt__", lambda self, other: heuristic(self) < heuristic(other))
    states = [problem]
    visited = set() # to not visit the same state twice
    

    while states:
        # heapq.heappop(states) can be used to POP a state from the state list
        # heapq.heappush(states, new_state) can be used to APPEND a new state to the state list
        
        # state heap
        state = heapq.heappop(states)
        # add to visited
        visited.add(state)

        # found solution
        if state.is_palindrome():
            return state

        # get list of possible states ordered by heuristic
        ordered_states = []
        for child in state.children():
            if child not in visited:
                heapq.heappush(ordered_states, (heuristic(child), child))
        ordered_states.sort()

        # push ordered states into heap
        for state in ordered_states:
            heapq.heappush(states, state[1]) 
    
    return None

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

solution1 = GameState([[0, 0, 2, 1, 2], 
                  [2, 1, 1, 2, 0], 
                  [3, 3, 3, 0, 3],
                  [3, 1, 1, 1, 3],
                  [2, 0, 2, 0, 2]])

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

# -------------------------------------------------
# SEARCH ALGORITHMS TEST
# -------------------------------------------------

# ------------------------------
# NOTE : not working (maybe it's suposed to not work?)
# ------------------------------
# Test BFS
# start_time = time.time()
# solution = breadth_first_search(game)
# finish_time = time.time()
# solution.print_move_history()
# print("TIME: " + str(finish_time-start_time))

# ------------------------------
# NOTE : doesn't work well for game, game3 and game4
# ------------------------------
# Test Greedy Search
start_time = time.time()
solution = greedy_search(game2, h1)
finish_time = time.time()
solution.print_move_history()
print("TIME: " + str(finish_time-start_time))