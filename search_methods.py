import time
import heapq
from game_state import GameState, easy_games, normal_difficulty_games, hard_games, very_hard_games


# -------------------------------------------------
# Uninformed Search Methods
# -------------------------------------------------

def breadth_first_search(problem):
    # solves game using bfs

    # problem(GameState) - the initial state
    queue = [problem]
    visited = set() # to not visit the same state twice

    i = 0
    while queue:
        i+=1
        state = queue.pop(0)
        visited.add(state)

        if state.is_palindrome():
            return state, i

        for child in state.children():
            if child not in visited:
                queue.append(child) 
    return None

def depth_first_search(problem):
    # solves game using dfs

    # problem(GameState) - the initial state
    stack = [problem]
    visited = set() # to not visit the same state twice

    i = 0
    while stack:
        i+=1
        state = stack.pop(0)
        visited.add(state)

        if state.is_palindrome():
            return state, i

        for child in state.children():
            if child not in visited:
                stack.insert(0,child) 
    return None

def depth_limited_search(problem, depth):
    stack = [(problem, 0)] # start with depth 0
    visited = set() # to not visit the same state twice

    i = 0
    while stack:
        (state, current_depth) = stack.pop(0)
        visited.add(state)
        i+=1
        if state.is_palindrome():
            return state, i

        if current_depth < depth:
            for child in state.children():
                if child not in visited:
                    stack.insert(0,(child, current_depth+1)) # add depth
    return None, i

def iterative_deepening(problem):
    # solves game using iterative deepening
    i = 0
    for depth in range(100):
        result, j = depth_limited_search(problem, depth)
        i += j
        if result != None: return result, i
    return None

def uniform_cost(problem):
    # Uniform Cost Search is equal to Breadth first Search 
    return breadth_first_search(problem)

# -------------------------------------------------
# Heuristic Search Methods
# -------------------------------------------------

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

def h2(state):
    # assigns a score to each row and column based on how close it is to being a palindrome
    # higher score less close to being a palindrome
    score = 0

    for i in range(len(state.board)):
        row = state.board[i]
        col = state.get_col(i)

        row = state.remove_zeros(row)
        col = state.remove_zeros(col)

        for i in range(len(row) // 2):
            if row[i] != row[-i-1]: score += 1

        for i in range(len(col) // 2):
            if col[i] != col[-i-1]: score += 1

    return score / 2

def h3(state):
    # makes an estimation of the number of pieces that need to be placed to end the game
    estimate = 0

    for i in range(len(state.board)):
        row = state.board[i]
        col = state.get_col(i)

        if not (state.row_palindrome(i)):
            row = state.remove_zeros(row)
            estimate += len(set(row) & set(row[::-1]))
        
        if not (state.col_palindrome(i)):
            col = state.remove_zeros(col)
            estimate += len(set(col) & set(col[::-1]))
    return estimate / 2

def greedy_search(problem, heuristic):
    # problem (GameState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer
    setattr(GameState, "__lt__", lambda self, other: heuristic(self) < heuristic(other))
    states = [(problem, heuristic(problem))]
    visited = set() # to not visit the same state twice

    i = 0
    while states:
        # heapq.heappop(states) can be used to POP a state from the state list
        # heapq.heappush(states, new_state) can be used to APPEND a new state to the state list
        i+=1
        # state heap
        state, _ = heapq.heappop(states)
        
        # add to visited
        visited.add(state)

        # found solution
        if state.is_palindrome():
            return state, i

        # get possible states
        for child in state.children():
            if child not in visited:
                heapq.heappush(states, (child, heuristic(child)))

        states.sort()
    return None

def a_star_search(problem, heuristic):
    # problem (GameState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer

    # this is very similar to greedy, the difference is that it takes into account the cost of the path so far
    return greedy_search(problem, lambda state: heuristic(state) + len(state.move_history))


def weighted_a_star_search(problem, W, heuristic):
    return greedy_search(problem, lambda state: W*heuristic(state) + len(state.move_history))

# -------------------------------------------------
# SEARCH ALGORITHMS TEST
# -------------------------------------------------

# Test BFS
# easy_games
start_time = time.time()
solution, steps = breadth_first_search(easy_games()[0])
finish_time = time.time()
print("BFS --------------------")
# solution.print_move_history()
print("TIME: " + str(finish_time-start_time))
print("STEPS: " + str(steps))
print("\n")

# Test iterative deepening
# easy_games
start_time = time.time()
solution, steps = iterative_deepening(easy_games()[0])
finish_time = time.time()
print("Iterative Deepening --------------------")
# solution.print_move_history()
print("TIME: " + str(finish_time-start_time))
print("STEPS: " + str(steps))
print("\n")

# Test Greedy Search with h1
# normal_difficulty_games
start_time = time.time()
solution, steps = greedy_search(normal_difficulty_games()[0], h1)
finish_time = time.time()
print("Greedy h1 --------------------")
# solution.print_move_history()
print("TIME: " + str(finish_time-start_time))
print("STEPS: " + str(steps))
print("\n")

# Test Greedy Search with h2
# hard_games (just the 4th one)
start_time = time.time()
solution, steps = greedy_search(hard_games()[4], h2)
finish_time = time.time()
print("Greedy h2 --------------------")
# solution.print_move_history()
print("TIME: " + str(finish_time-start_time))
print("STEPS: " + str(steps))
print("\n")

# Test Greedy Search with h3
# normal_difficulty_games (0, 2, 3)
start_time = time.time()
solution, steps = greedy_search(normal_difficulty_games()[0], h3)
finish_time = time.time()
print("Greedy h3 --------------------")
# solution.print_move_history()
print("TIME: " + str(finish_time-start_time))
print("STEPS: " + str(steps))
print("\n")

# Test A* Search
# normal_difficulty_games (2, 3)
start_time = time.time()
solution, steps = a_star_search(normal_difficulty_games()[2], h3)
finish_time = time.time()
print("A* h3 --------------------")
# solution.print_move_history()
print("TIME: " + str(finish_time-start_time))
print("STEPS: " + str(steps))
print("\n")

# Test weighted A* Search
# normal_difficulty_games
normal_difficulty_games
start_time = time.time()
solution, steps = weighted_a_star_search(normal_difficulty_games()[0], 8, h1)
finish_time = time.time()
print("Weighted A* h1 --------------------")
# solution.print_move_history()
print("TIME: " + str(finish_time-start_time))
print("STEPS: " + str(steps))
print("\n")

# Test weighted A* Search
# normal_difficulty_games
start_time = time.time()
solution, steps = weighted_a_star_search(normal_difficulty_games()[0], 8, h2)
finish_time = time.time()
print("Weighted A* h2 --------------------")
# solution.print_move_history()
print("TIME: " + str(finish_time-start_time))
print("STEPS: " + str(steps))
print("\n")

# Test weighted A* Search
# hard_games (1, 2, 4, 5)
start_time = time.time()
solution, steps = weighted_a_star_search(hard_games()[1], 8, h3)
finish_time = time.time()
print("Weighted A* h3 --------------------")
# solution.print_move_history()
print("TIME: " + str(finish_time-start_time))
print("STEPS: " + str(steps))
print("\n")