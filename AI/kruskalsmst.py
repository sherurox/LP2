# Function to find the root parent of a node using path compression
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])  # Recursively find the root parent and perform path compression
    return parent[node]

# Function to perform union of two sets based on rank
def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

# Function to find the Minimum Spanning Tree using Kruskal's algorithm
def kruskal_mst(graph):
    edges = []
    num_vertices = len(graph)

    # Create a list of edges from the graph
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    # Sort the edges based on their weights in ascending order
    edges.sort(key=lambda edge: edge[2])

    parent = [i for i in range(num_vertices)]  # Initialize the parent array
    rank = [0] * num_vertices  # Initialize the rank array

    mst = []  # List to store the edges in the MST

    for edge in edges:
        u, v, weight = edge
        u_parent = find(parent, u)
        v_parent = find(parent, v)

        # Check if adding the edge forms a cycle
        if u_parent != v_parent:
            mst.append(edge)
            union(parent, rank, u_parent, v_parent)

    return mst

# Example usage
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst = kruskal_mst(graph)

# Print the edges in the MST
print("Edge \tWeight")
for edge in mst:
    u, v, weight = edge
    print(u, "-", v, "\t", weight)

# Let's go through the code with added comments:

# The find function is used to find the root parent of a
#  node using path compression. It recursively traverses 
#  the parent array until it reaches the root parent, and
#   during the process, it performs path compression by 
#   updating the parent of each traversed node directly
#    to the root parent.

# The union function is used to perform the union operation
#  of two sets based on rank. It takes the parent and 
#   arrays, and two nodes x and y. It finds the root parents
#  of x and y and compares their ranks. If the ranks are different,
#   the set with the smaller rank is merged into the set with the 
#   larger rank. If the ranks are the same, one set is arbitrarily 
#   chosen as the parent, and its rank is increased by 1.

# The kruskal_mst function takes a graph represented as an adjacency 
# matrix and returns the Minimum Spanning Tree (MST) as a list of edges.
#  It starts by creating a list of edges from the graph.

# The edges are then sorted based on their weights in ascending order 
# using the sort method and a lambda function.

# The parent array is initialized with each node as its own parent, and 
# the rank array is initialized with zeros.

# The mst list is created to store the edges in the MST.

# Each edge is processed one by one from the sorted edges. The find function
#  is used to find the root parents of the nodes connected by the edge. If the 
#  root parents are different, adding the edge to the MST does not form a cycle, 
#  so the edge is added to the mst list, and the union function is called to merge
#   the sets represented by the root parents.

# Finally, the mst list is returned, and the edges in the MST are printed.
