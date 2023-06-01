from queue import PriorityQueue

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # 0 represents the empty space

# Define the possible moves
moves = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

# Calculate the Manhattan distance heuristic
def calculate_manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

# A* search algorithm
def solve_puzzle(start_state):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_state))
    
    while not queue.empty():
        _, current_state = queue.get()
        
        if current_state == goal_state:
            return current_state  # Puzzle solved
        
        visited.add(tuple(map(tuple, current_state)))  # Convert to tuple for hashing
        
        empty_row, empty_col = find_empty_space(current_state)
        
        for move in moves:
            new_row = empty_row + move[0]
            new_col = empty_col + move[1]
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(row) for row in current_state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
                
                if tuple(map(tuple, new_state)) not in visited:
                    priority = calculate_manhattan_distance(new_state)
                    queue.put((priority, new_state))
                    visited.add(tuple(map(tuple, new_state)))
    
    return None  # No solution found

# Find the coordinates of the empty space (0)
def find_empty_space(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Example usage
start_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]  # Initial state
solution = solve_puzzle(start_state)

if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution found.")


#     The given code solves the 8-puzzle problem using the A* search 
#     algorithm with the Manhattan distance heuristic. Let's go through the
#     code with comments to understand it better:

# 1. The code imports the `PriorityQueue` class from the `queue` module. This 
# data structure is used to store the states of the puzzle based on their priority.

# 2. The `goal_state` variable represents the desired configuration of the puzzle,
#  where the numbers 1 to 8 are arranged in order, and 0 represents the empty space.

# 3. The `moves` list contains the possible moves in the puzzle. Each move is 
# represented as a tuple `(row_change, col_change)`.

# 4. The `calculate_manhattan_distance` function calculates the Manhattan distance 
# heuristic for a given state. The Manhattan distance is the sum of the horizontal 
# and vertical distances between the current position of each number and its target 
# position in the goal state.

# 5. The `solve_puzzle` function implements the A* search algorithm to solve the puzzle. 
# It takes the `start_state` as input and returns the solution state if found, or `None`
# if no solution is found.

# 6. The `visited` set keeps track of the visited states to avoid revisiting them.

# 7. The `queue` is a priority queue that stores states along with their priority. 
# The priority is calculated based on the Manhattan distance heuristic.

# 8. The algorithm enters a loop that continues until the queue is empty.

# 9. In each iteration, the state with the lowest priority is removed from the queue.

# 10. If the current state is the goal state, the function returns the solution state, 
# indicating that the puzzle is solved.

# 11. The current state is added to the `visited` set for future reference. To hash the
#  state, it is converted to a tuple of tuples.

# 12. The empty space coordinates in the current state are found using the `find_empty_space` function.

# 13. The algorithm generates new states by moving the empty space in all possible directions.

# 14. Each new state is checked for validity (within the puzzle boundaries) and whether 
# it has been visited before.

# 15. If the new state is valid and not visited, it is assigned a priority based on the 
# Manhattan distance heuristic and added to the queue along with its priority.

# 16. The new state is also added to the `visited` set.

# 17. If the loop ends without finding a solution, the function returns `None`.

# 18. The `find_empty_space` function finds the coordinates of the empty space (0) in a
#  given state.

# 19. In the example usage, an initial `start_state` is defined.

# 20. The `solve_puzzle` function is called with the `start_state` as input, and the returned 
# solution is stored in the `solution` variable.

# 21. If a solution is found, it is printed row by row.

# 22. If no solution is found, a message indicating that no solution was found is printed.