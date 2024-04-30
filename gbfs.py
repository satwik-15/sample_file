import heapq

def greedy_best_first_search(graph, start, goal):
    # Priority queue for storing nodes to be explored, ordered by heuristic value
    frontier = [(heuristic(start, goal), start, [start])]  # (heuristic value, node, path)
    explored = set()

    while frontier:
        _, node, path = heapq.heappop(frontier)

        # Goal reached
        if node == goal:
            return path, calculate_path_cost(path, graph)

        # Explore the node if not already explored
        if node not in explored:
            explored.add(node)

            # Add neighbors to the frontier
            for neighbor, _ in graph.get(node, []):
                if neighbor not in explored:
                    heapq.heappush(frontier, (heuristic(neighbor, goal), neighbor, path + [neighbor]))

    # Goal not reachable
    return None, float('inf')

def heuristic(node, goal):
    # Example heuristic function (here, it returns a simple distance between two nodes)
    return abs(ord(node) - ord(goal))

def calculate_path_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        for neighbor, edge_cost in graph[path[i]]:
            if neighbor == path[i+1]:
                cost += edge_cost
                break
    return cost

# Example usage:
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 10), ('E', 5)],
    'C': [('A', 2), ('F', 3), ('G', 7)],
    'D': [('B', 10)],
    'E': [('B', 5)],
    'F': [('C', 3)],
    'G': [('C', 7)]
}

start_node = 'A'
goal_node = 'G'

path, cost = greedy_best_first_search(graph, start_node, goal_node)
if path:
    print("Path:", "->".join(path))
    print("Cost:", cost)
else:
    print(f"No path exists between {start_node} and {goal_node}")
