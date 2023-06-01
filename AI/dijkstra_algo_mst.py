from heapq import *

def dijkstra(graph, start, visited, distance):
    distance[start] = 0
    bag = []
    heappush(bag, [0, start])

    while bag:
        d, n  = heappop(bag)
        visited[n] = 1
        for cd, cn in graph[n]:
            if not visited[cn] and distance[n]+cd < distance[cn]:
                distance[cn] = distance[n]+cd
                heappush(bag, [distance[n]+cd, cn])

    print(distance) 

edges = [[1,3,2], [1, 2, 1], [2, 3, 1], [2, 5, 1],[3, 4, 2], [5,4, 5]]
n = 5
graph    =  {}
distance = {}
visited = {}

for i in range(1, n+1):
    graph[i] = []
    distance[i]= 10**8+1
    visited[i] = 0

for u,v,d in edges:
    graph[u].append([d, v])
    graph[v].append([d, u])

start = 1
dijkstra(graph, start, visited, distance)

# Explanation:
# 1. The code implements Dijkstra's algorithm, a greedy search algorithm, for 
# the single source shortest path problem.

# 2. The `dijkstra` function takes four parameters: `graph` (the graph represented 
# as an adjacency list), `start` (the starting vertex), `visited` (a list to keep 
# track of visited vertices), and `distance` (a list to store the distances from the 
# starting vertex to each vertex).

# 3. The distance from the start vertex to itself is initialized as 0, and a priority 
# queue (heap) called `bag` is created to store vertices and their respective distances. 
# The starting vertex is added to the `bag` with a distance of 0.

# 4. The main loop runs as long as the `bag` is not empty. In each iteration, the vertex 
# with the minimum distance (`d`) is popped from the `bag`.

# 5. The popped vertex `n` is marked as visited by setting `visited[n] = 1`.

# 6. The code iterates over the neighbors (`cd`, `cn`) of the popped vertex `n` in 
# the graph. It checks if the neighbor `cn` is not visited and if the distance from the 
# start vertex to `n` plus the distance from `n` to `cn` is less than the current distance 
# from the start vertex to `cn`.

# 7. If the condition is true, it updates the distance to `cn` as `distance[n] + cd` and pushes 
# it into the `bag` with the new distance value.

# 8. Once the `bag` is empty and all vertices have been visited, the function prints the final 
# distances stored in the `distance` list.

# 9. The example usage section defines an example graph represented by the `edges` list, the number 
# of vertices `n`, an empty `graph` dictionary, an empty `distance` dictionary, and an empty `visited` dictionary.

# 10. The code initializes the graph, distance, and visited dictionaries with default values.

# 11. The `edges` list is iterated, and the graph is populated with the edges and their corresponding 
# weights.

# 12. The starting vertex is set to 1.

# 13. The `dijkstra` function is called with the graph, starting vertex, visited, and distance dictionaries.

# The Single-Source Shortest Path Problem is a graph problem that seeks to find the
# shortest paths from a single source vertex to all other vertices in a weighted graph. Dijkstra's 
# algorithm, which is a greedy search algorithm, is commonly used to solve this problem efficiently. 
# It iteratively selects the vertex with the minimum distance from the source and relaxes the distances 
# of its adjacent vertices until all vertices have been visited. The algorithm guarantees finding the 
# shortest path in graphs with non-negative edge weights.