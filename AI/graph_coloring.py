def bipartite(graph, node, visited, color, c):
    visited[node] = 1
    color[node] = c
    for child in graph[node]:
        if not visited[child]:
            tmp = bipartite(graph, child, visited, color, c^1)
            if tmp == False:
                return False
        else :
            if color[node] == color[child]:
                return False 
    return True

# canot be colored 
edges = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [4, 5]]
n = 5

# can be colored 
# edges = [[1, 2], [2, 3], [3, 6], [6, 5], [5, 4], [1, 4]]
# n = 6


graph = {}
visited  = {}
color = {}

for i in range(1, n+1):
    graph[i] = []
    visited[i] = 0
    color[i] = None

for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

temp  = bipartite(graph, 1, visited, color, 0)
print(temp)

# The given code is solving a graph coloring problem using the concept of
#  bipartite graphs. The goal is to determine if the given graph can be 
#  colored using only two colors such that no adjacent nodes have the same color.

# Here's a step-by-step explanation of the code:

# 1. The function `bipartite` takes the graph, a node, a visited dictionary,
#  a color dictionary, and a color `c` as input.

# 2. It marks the current node as visited by setting `visited[node] = 1` and assigns 
# the color `c` to the current node by setting `color[node] = c`.

# 3. It then iterates over each child node of the current node using `graph[node]`
#  to check if it can be colored in a valid way. 

# 4. If the child node has not been visited (`visited[child] = 0`), it recursively 
# calls the `bipartite` function on the child node, passing the same parameters and 
# flipping the color by using `c^1` (XOR operation with 1) to ensure alternate coloring.

# 5. If the recursive call returns `False`, indicating that the child node cannot be
#  colored properly, the function immediately returns `False` to propagate the failure upwards.

# 6. If the child node has already been visited (`visited[child] = 1`), it checks if
#  the current node and the child node have the same color (`color[node] == color[child]`). 
#  If they do, it means the graph cannot be colored in a valid way, and the function returns `False`.

# 7. If all child nodes have been visited and validated without any
#  conflicts, the function returns `True`, indicating that the graph can be colored properly.

# 8. The main code initializes the `graph`, `visited`, and `color` 
# dictionaries based on the given number of nodes `n`. It also defines the edges of the graph.

# 9. It then calls the `bipartite` function, starting with the first 
# node (node 1), passing the `graph`, `visited`, `color`, and initial color 0.

# 10. The result is stored in the `temp` variable, and it prints the value of 
# `temp`, which indicates whether the graph can be colored properly or not.

# The code checks if the given graph is bipartite, which means it can be colored 
# using only two colors such that no adjacent nodes have the same color. It is
#  based on the concept that a graph is bipartite if and only if it does not 
#  contain any odd-length cycles. If the graph is bipartite, it returns `True`; otherwise, it returns `False`.