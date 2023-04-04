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

    while states:
        # heapq.heappop(states) can be used to POP a state from the state list
        # heapq.heappush(states, new_state) can be used to APPEND a new state to the state list
        
        # state heap
        state, _ = heapq.heappop(states)
        
        # add to visited
        visited.add(state)

        # found solution
        if state.is_palindrome():
            return state

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
solution = None

def test_bfs_easy(game):
    global solution
    global time_
    # Test BFS
    # easy_games
    start_time = time.time()
    solution = breadth_first_search(easy_games()[game])
    finish_time = time.time()
    print("EASY BFS GAME:" + str(game+1) + " --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))

def test_iterative_easy(game):
    global solution
    global time_
    # Test iterative deepening
    # easy_games
    start_time = time.time()
    solution = iterative_deepening(easy_games()[game])
    finish_time = time.time()
    print("ITERATIVE DEEPENING GAME:" + str(game+1) + " --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))

def test_greedy_easy(game, heuristic):
    global solution
    global time_
    # Test Greedy Search with h1
    # easy_games
    start_time = time.time()
    solution = greedy_search(easy_games()[game], heuristic)
    finish_time = time.time()
    print("EASY GREEDY H1 GAME:" + str(game+1) + " --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))

def test_greedy_normal(game, heuristic):
    global solution
    global time_
    # Test Greedy Search with h1
    # normal_difficulty_games
    # Test Greedy Search with h3
    # normal_difficulty_games (0, 2, 3)
    start_time = time.time()
    solution = greedy_search(normal_difficulty_games()[game], heuristic)
    finish_time = time.time()
    print("NORMAL GREEDY H1 GAME:" + str(game+1) + " --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))

def test_greedy_hard(game, heuristic):
    global solution
    global time_
    # Test Greedy Search with h2
    # hard_games (just the 4th one)
    start_time = time.time()
    solution = greedy_search(hard_games()[game], heuristic)
    finish_time = time.time()
    print("HARD GREEDY H2 GAME:" + str(game+1) + " --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))

def test_a_star_easy(game, heuristic):
    global solution
    global time_
    # Test A* Search
    start_time = time.time()
    solution = a_star_search(easy_games()[game], heuristic)
    finish_time = time.time()
    print("A* H1 GAME:"  + str(game+1) + " --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))

def test_a_star_normal(game, heuristic):
    global solution
    global time_
    # Test A* Search
    # normal_difficulty_games (2, 3)
    start_time = time.time()
    solution = a_star_search(normal_difficulty_games()[game], heuristic)
    finish_time = time.time()
    print("A* H2 GAME: 3 --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))

def test_weighted_a_star_easy(game, heuristic, weight):
    global solution
    global time_
    # Test A* Search
    # hard_games (just the 4th one)
    start_time = time.time()
    solution = weighted_a_star_search(easy_games()[game], 8, heuristic)
    finish_time = time.time()
    print("A* H1 GAME: 0 --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))

def test_weighted_a_star_normal(game, heuristic, weight):
    global solution
    global time_
    # Test weighted A* Search
    # normal_difficulty_games
    normal_difficulty_games
    start_time = time.time()
    solution = weighted_a_star_search(normal_difficulty_games()[game], weight, heuristic)
    finish_time = time.time()
    print("WEIGHTED A* H1 GAME: 0 --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))


def test_weighted_a_star_hard(game, heuristic, weight):
    global solution
    global time_
    # Test weighted A* Search
    # hard_games (1, 2, 4, 5)
    start_time = time.time()
    solution = weighted_a_star_search(hard_games()[game], weight, heuristic)
    finish_time = time.time()
    print("WEIGHTED A* H3 GAME: 1 --------------------")
    # solution.print_move_history()
    time_ = finish_time-start_time
    print("TIME: " + str(finish_time-start_time))