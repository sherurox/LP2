from queue import Queue

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()  # Set to keep track of visited vertices
    queue = Queue()  # Queue to store vertices to visit
    queue.put(start)  # Enqueue the start vertex
    visited.add(start)  # Mark the start vertex as visited

    while not queue.empty():
        vertex = queue.get()  # Dequeue a vertex from the queue
        print(vertex)  # Process the vertex (in this case, print it)

        for neighbor in graph[vertex]:  # Iterate over the neighbors of the current vertex
            if neighbor not in visited:  # Check if the neighbor has not been visited
                queue.put(neighbor)  # Enqueue the unvisited neighbor
                visited.add(neighbor)  # Mark the neighbor as visited

# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited vertices

    visited.add(start)  # Mark the current vertex as visited
    print(start)  # Process the vertex (in this case, print it)

    for neighbor in graph[start]:  # Iterate over the neighbors of the current vertex
        if neighbor not in visited:  # Check if the neighbor has not been visited
            dfs(graph, neighbor, visited)  # Recursively call DFS on the unvisited neighbor

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS traversal:")
bfs(graph, 'A')  # Perform BFS traversal starting from vertex 'A'

print("\nDFS traversal:")
dfs(graph, 'A')  # Perform DFS traversal starting from vertex 'A'


# This code implements two graph traversal algorithms: Breadth-First Search (BFS) 
# and Depth-First Search (DFS). Here's an explanation of the code:

# The code starts by importing the Queue class from the queue module, which will
#  be used in the BFS algorithm.

# The bfs function performs a Breadth-First Search on the given graph starting 
# from the start vertex. It uses a visited set to keep track of the visited 
# vertices and a queue to store the vertices to visit.

# In the BFS algorithm, we start by enqueueing the start vertex, marking it as 
# visited, and entering the main loop.

# Inside the loop, we dequeue a vertex from the queue and process it (in this case,
# simply print it). Then, we iterate over the neighbors of the current vertex.

# For each neighbor, if it has not been visited yet, we enqueue it, mark it as 
# visited, and continue the loop.

# The BFS algorithm continues until the queue becomes empty, meaning all reachable 
# vertices have been visited.

# The dfs function performs a Depth-First Search on the given graph starting from 
# the start vertex. It uses a visited set to keep track of the visited vertices.

# In the DFS algorithm, we start by marking the start vertex as visited and processing
#  it (printing it).

# Then, for each unvisited neighbor of the current vertex, we recursively call the dfs 
# function to explore that neighbor and its descendants.

# The DFS algorithm explores vertices as deeply as possible before backtracking.

# Finally, an example usage of the functions is provided. The graph is defined as a 
# dictionary, where each vertex is mapped to a list of its neighboring vertices.

# The BFS traversal is performed starting from vertex 'A', and the vertices are printed
#  in the order they are visited.

# Similarly, the DFS traversal is performed starting from vertex 'A', and the vertices
#  are printed in the order they are visited.