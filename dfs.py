graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Recursive implementation of DFS algorithm
def dfs(graph, node_id, target_stop_id, visited_ids):
    if node_id == target_stop_id:
        visited_ids.append(node_id)
        return visited_ids
    if node_id not in visited_ids:
        visited_ids.append(node_id)
        for neighbour in graph[node_id]:
            result = dfs(graph, neighbour['stop_id'], target_stop_id, visited_ids)
            if result is not None:
                return result
    return None


def check_all(id_list, graph, names):
    for id1 in id_list:
        for id2 in id_list:
            if dfs(graph, id1, id2, []) == None:
                print(f'({names[id1]}) -> ({names[id2]}): UNREACHABLE')
            else:
                print(f'({names[id1]}) -> ({names[id2]}): OK')
