import time
import heapq
from game_state import GameState, games


# -------------------------------------------------
# Uninformed Search Methods
# -------------------------------------------------

def breadth_first_search(problem):
    # solves game using bfs

    # problem(GameState) - the initial state
    queue = [problem]
    visited = set() # to not visit the same state twice

    while queue:
        state = queue.pop(0)
        visited.add(state)

        if state.is_palindrome():
            return state

        for child in state.children():
            if child not in visited:
                queue.append(child) 
    return None

def depth_first_search(problem):
    # solves game using dfs

    # problem(GameState) - the initial state
    stack = [problem]
    visited = set() # to not visit the same state twice

    while stack:
        state = stack.pop(0)
        visited.add(state)

        if state.is_palindrome():
            return state

        for child in state.children():
            if child not in visited:
                stack.insert(0,child) 
    return None

def depth_limited_search(problem, depth):
    stack = [(problem, 0)] # start with depth 0
    visited = set() # to not visit the same state twice

    while stack:
        (state, current_depth) = stack.pop(0)
        visited.add(state)

        if state.is_palindrome():
            return state

        if current_depth < depth:
            for child in state.children():
                if child not in visited:
                    stack.insert(0,(child, current_depth+1)) # add depth
    return None

def iterative_deepening(problem):
    # solves game using iterative deepening

    for depth in range(100):
        result = depth_limited_search(problem, depth)
        if result != None: return result
    return None

def uniform_cost(problem):
    # TODO
    # Acho que é igual à bsf se o custo for 1
    return None


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

def greedy_search(problem, heuristic):
    # problem (GameState) - the initial state
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

def a_star_search(problem, heuristic):
    # problem (GameState) - the initial state
    # heuristic (function) - the heuristic function that takes a board (matrix), and returns an integer

    # this is very similar to greedy, the difference is that it takes into account the cost of the path so far
    return greedy_search(problem, lambda state: heuristic(state) + len(state.move_history))


def weighted_a_star_search(problem, heuristic):
    # TODO
    return None

# -------------------------------------------------
# SEARCH ALGORITHMS TEST
# -------------------------------------------------

# ------------------------------
# NOTE : working better now but for easier puzzles
# ------------------------------
# Test BFS
start_time = time.time()
solution = breadth_first_search(games()[6])
finish_time = time.time()
print("BFS --------------------")
solution.print_move_history()
print("TIME: " + str(finish_time-start_time))

# ------------------------------
# NOTE : not working (maybe it's suposed to not work?)
# ------------------------------
# Test DFS
# start_time = time.time()
# solution = depth_first_search(games()[6])
# finish_time = time.time()
# print("DFS --------------------")
# solution.print_move_history()
# print("TIME: " + str(finish_time-start_time))

# ------------------------------
# NOTE : not working (maybe it's suposed to not work?)
# ------------------------------
# Test iterative deepening
start_time = time.time()
solution = iterative_deepening(games()[6])
finish_time = time.time()
print("Iterative Deepening --------------------")
solution.print_move_history()
print("TIME: " + str(finish_time-start_time))

# ------------------------------
# NOTE : doesn't work well for game, game3 and game4
# ------------------------------
# Test Greedy Search
start_time = time.time()
solution = greedy_search(games()[6], h1)
finish_time = time.time()
print("Greedy --------------------")
solution.print_move_history()
print("TIME: " + str(finish_time-start_time))

# ------------------------------
# NOTE : tem de se mudar o custo não sei é para o que
# ------------------------------
# Test A* Search
start_time = time.time()
solution = a_star_search(games()[6], h1)
finish_time = time.time()
print("A* --------------------")
solution.print_move_history()
print("TIME: " + str(finish_time-start_time))