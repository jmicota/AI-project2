from collections import deque

def bfs(graph, start_id, end_id):
    visited_ids = set()
    queue = deque([(start_id, 0)])
    
    while queue:
        node_id, distance = queue.popleft()
        if node_id == end_id:
            return distance
        if node_id not in visited_ids:
            visited_ids.add(node_id)
            for neighbour in graph[node_id]:
                if neighbour['stop_id'] not in visited_ids:
                    queue.append((neighbour['stop_id'], distance + 1))
    
    return -1


def bfs_with_path(graph, start_id, end_id):
    visited_ids = set()
    queue = deque([(start_id, 0)])
    
    while queue:
        node_id, distance = queue.popleft()
        if node_id == end_id:
            return distance
        if node_id not in visited_ids:
            visited_ids.add(node_id)
            for neighbour in graph[node_id]:
                if neighbour['stop_id'] not in visited_ids:
                    queue.append((neighbour['stop_id'], distance + 1))
    
    return -1
