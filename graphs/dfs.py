def dfs_iterative(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)



# Adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

if __name__ == '__main__':
    print(dfs_iterative(graph, 'A'))
    