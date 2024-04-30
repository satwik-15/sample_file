# Define the graph as a nested dictionary where keys are nodes and values are dictionaries of neighboring nodes and their edge costs
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

# Function to add an edge to the graph with a specified cost
def add_edge(graph, u, v, cost):
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = cost
    graph[v][u] = cost

# Function to print the graph
def print_graph(graph):
    for node in graph:
        print(node + " -> ", end="")
        neighbors = graph[node]
        print(", ".join([f"{neighbor}({neighbors[neighbor]})" for neighbor in neighbors]))

# Example usage:
add_edge(graph, 'A', 'D', 8)
print_graph(graph)
