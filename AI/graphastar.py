tree = { 'S': [['A', 1], ['B', 5], ['C', 8]],
        'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
        'B': [['S', 5], ['G', 4],],
        'C': [['S', 8], ['G',5]],
        'D': [['A', 3]],
        'E': [['A', 7]]
}

heuristic = {'S':8, 'A':8, 'B':4, 'C':3, 'D':5000, 'E':5000, 'G':0}

cost = {'S':0}              #total cost for nodes visited

def AStarSearch():
    global tree, heuristic
    closed = []
    opened = [['S',8]]
    '''find the visited nodes //closed'''
    while True:
        fn = [i[1] for i in opened]
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == 'G':
            break
        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]:cost[node]+item[1]})
            fn_node = cost[node] + heuristic[item[0]] + item[1]
            temp  = [item[0], fn_node]
            opened.append(temp)

    '''find optimal sequence'''
    trace_node = 'G'
    optimal_sequence = ['G'] 
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]
        if trace_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]     

            if cost[check_node]+children_costs[children_nodes.index(trace_node)] == cost[trace_node]: 
                optimal_sequence.append(check_node)
                trace_node = check_node
    print(opened)
    optimal_sequence.reverse()
    return closed, optimal_sequence

if __name__ == '__main__':
    visited_nodes, optimal_node  = AStarSearch()
    print("visited nodes :"+str(visited_nodes))
    print("optimal nodes sequence : "+str(optimal_node))


#     The tree variable represents the graph structure as an adjacency 
#     list. Each key in the dictionary represents a node, and its corresponding 
#     value is a list of neighbors with their associated costs.

# The heuristic dictionary represents the heuristic values for each node. In this 
# example, it represents the estimated distance from each node to the goal node ('G').

# The cost dictionary keeps track of the total cost of reaching each node during 
# the search process. It is initialized with the start node ('S') having a cost of 0.

# The AStarSearch function implements the A* search algorithm.

# It starts by initializing an empty closed list to keep track of visited nodes and 
# an opened list that stores nodes yet to be explored. The 'S' node is initially 
# added to the opened list with its heuristic value as the priority.

# The algorithm enters a loop that continues until the goal node ('G') is reached.

# Inside the loop, the algorithm selects the node with the lowest cost (fn) from the 
# opened list and adds it to the closed list. If the selected node is the goal node, 
# the loop breaks.

# The algorithm then expands the selected node by considering its neighbors. If a
#  neighbor is already in the closed list, it is skipped to avoid revisiting nodes.

# The cost to reach each neighbor is updated in the cost dictionary, and the evaluation 
# function (fn_node) is calculated as the sum of the cost to reach the neighbor, the 
# heuristic value, and the cost of the edge connecting them.

# The neighbor and its evaluation function are added to the opened list.

# After the loop ends, the algorithm has visited all nodes necessary to reach the goal node.

# The next step is to find the optimal sequence of nodes by backtracking from the goal
#  node to the start node.

# The algorithm starts with the goal node ('G') and traces back through the closed list. It
#  checks if the current node's cost plus the cost of the edge to the goal node matches 
#  the cost of the goal node. If it does, it adds the current node to the optimal sequence.

# Finally, the opened list is printed (optional), the optimal sequence is reversed, and 
# the closed list and the optimal node sequence are returned.

# In the if __name__ == '__main__': block, the AStarSearch function is called, and the 
# visited nodes and optimal node sequence are printed.