# Function to find the vertex with the minimum key value
def min_key(vertices, key, mst_set):
    min_value = float('inf')
    min_index = -1
    for v in range(vertices):
        if key[v] < min_value and mst_set[v] is False:
            min_value = key[v]
            min_index = v
    return min_index

# Function to construct and print the MST using Prim's algorithm
def prim_mst(graph):
    vertices = len(graph)

    # Initialize key values, parent array, and MST set
    key = [float('inf')] * vertices  # Key values represent the minimum edge weight to connect the vertex to the MST
    parent = [None] * vertices  # Parent array keeps track of the parent of each vertex in the MST
    mst_set = [False] * vertices  # MST set stores whether a vertex is included in the MST or not

    # Start with the first vertex as the root
    key[0] = 0  # Set the key value of the root vertex as 0
    parent[0] = -1  # Set the parent of the root vertex as -1 (no parent)

    for _ in range(vertices - 1):
        # Choose the vertex with the minimum key value from the set of vertices not yet included in the MST
        u = min_key(vertices, key, mst_set)

        # Add the selected vertex to the MST set
        mst_set[u] = True

        # Update key and parent values of the adjacent vertices
        for v in range(vertices):
            # Check if the edge between u and v exists, v is not in MST, and the weight is smaller than the current key value of v
            if graph[u][v] > 0 and mst_set[v] is False and graph[u][v] < key[v]:
                key[v] = graph[u][v]  # Update the key value of v with the new smaller weight
                parent[v] = u  # Set u as the parent of v in the MST

    # Print the constructed MST
    print("Edge \tWeight")
    for i in range(1, vertices):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Example usage
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim_mst(graph)

# Explanation:
# 1. The `min_key` function is used to find the vertex with the 
# minimum key value from the set of vertices not yet included in
#  the MST. It iterates over all the vertices, checks if the key
#  value is smaller than the current minimum value, and also verifies
#  that the vertex is not already in the MST.
# 2. The `prim_mst` function constructs and prints the Minimum Spanning
#  Tree (MST) using Prim's algorithm. It initializes the key values, parent
#  array, and MST set. The key values represent the minimum edge weight to
#  connect the vertex to the MST. The parent array keeps track of the parent 
# of each vertex in the MST, and the MST set stores whether a vertex is included in the MST or not.
# 3. The algorithm starts with the first vertex as the root and sets its key value as 0 and parent as -1

# .
# 4. It then iteratively selects the vertex with the minimum key 
# value using the `min_key` function, adds it to the MST set, and 
# updates the key and parent values of its adjacent vertices if necessary.
# 5. Finally, it prints the constructed MST by iterating over the 
# parent array and printing the edges and their weights.

# The Greedy search algorithm for finding the MST in Prim's algorithm 
# works by iteratively selecting the vertex with the minimum key value.
#  At each step, it expands the MST by adding the selected vertex and 
#updating the key values and parent pointers of its adjacent vertices. 
# This process continues until all vertices are included in the MST. 
# The algorithm ensures that the chosen edges have the minimum total weight,
#  resulting in the Minimum Spanning Tree.