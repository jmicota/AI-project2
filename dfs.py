graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Recursive implementation of DFS algorithm
def dfs(graph, node, target, visited):
    if node == target:
        visited.append(node)
        return visited
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            result = dfs(graph, neighbour['stop_name'], target, visited)
            if result is not None:
                return result
    return None


def check_all(name_list, graph):
    for name1 in name_list:
        for name2 in name_list:
            if dfs(graph, name1, name2, []) == None:
                print(f'({name1}) -> ({name2}): UNREACHABLE')
            else:
                print(f'({name1}) -> ({name2}): OK')
