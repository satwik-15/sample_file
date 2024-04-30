import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def ucs(graph, start, goal):
    queue = PriorityQueue()
    queue.put(start, 0)
    visited = set()
    cost_so_far = {start: 0}
    while not queue.is_empty():
        current_node = queue.get()
        if current_node == goal:
            break
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, cost in graph[current_node].items():
                new_cost = cost_so_far[current_node] + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    queue.put(neighbor, new_cost)
    return cost_so_far
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3, 'G': 6},
    'D': {'B': 2},
    'E': {'B': 5, 'H': 8},
    'F': {'C': 3},
    'G': {'C': 6},
    'H': {'E': 8}
}
start_node = 'A'
goal_node = 'H'
result = ucs(graph, start_node, goal_node)
print("Cost to reach node '{}' from node '{}': {}".format(goal_node, start_node, result[goal_node]))
