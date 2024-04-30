import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue for storing nodes to be explored, ordered by path cost
    frontier = [(0, start, [])]  # (cost, node, path)
    explored = set()

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        # Goal reached
        if node == goal:
            return cost, path + [node]

        # Explore the node if not already explored
        if node not in explored:
            explored.add(node)

            # Expand the node and add its neighbors to the frontier
            for neighbor, edge_cost in graph.get(node, {}).items():
                if neighbor not in explored:
                    heapq.heappush(frontier, (cost + edge_cost, neighbor, path + [node]))

    # Goal not reachable
    return float('inf'), None

# Example usage:
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

start_node = 'A'
goal_node = 'D'

min_cost, path = uniform_cost_search(graph, start_node, goal_node)
if path:
    print(f"The minimum cost between {start_node} and {goal_node} is {min_cost}")
    print("Path:", "->".join(path))
else:
    print(f"There is no path between {start_node} and {goal_node}")
