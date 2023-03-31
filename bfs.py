from collections import deque
import copy


def sort_graph_by_departure_times(graph_original):
    graph = copy.copy(graph_original)
    for key in graph:
        graph[key] = sorted(graph[key], key=lambda neighbour: neighbour['departure_time'])
    return graph


def bfs(graph, start, end):
    visited = set()
    queue = deque([(start, 0)])
    
    while queue:
        node, distance = queue.popleft()
        if node == end:
            return distance, len(visited)
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour['stop_name'] not in visited:
                    queue.append((neighbour['stop_name'], distance + 1))
    
    return -1, len(visited)


def bfs_with_path(graph, start, end):
    visited = set()
    queue = deque([(start, [])])
    
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path, len(visited)
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour['stop_name'] not in visited:
                    queue.append((neighbour['stop_name'],
                                  path + [f'{neighbour["departure_time"]}: {neighbour["stop_name"]} (line {neighbour["line"]})']))
    
    return None, len(visited)


def bfs_with_path_and_time(graph, start, end, time_start):
    visited = set()
    queue = deque([(start, [], time_start)])
    
    while queue:
        node, path, time = queue.popleft()
        if node == end:
            return path, len(visited)
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour['stop_name'] not in visited and time < neighbour['departure_time']:
                    queue.append((neighbour['stop_name'],
                                  path + [f'{neighbour["departure_time"]}: {neighbour["stop_name"]} (line {neighbour["line"]})'],
                                  neighbour['departure_time']))
    
    return None, len(visited)


def bfs_with_path_and_correct_time(graph, start, end, time_start):
    visited = set()
    queue = deque([(start, [], time_start)])

    # sort neighbours by departure times (ascending)
    graph = sort_graph_by_departure_times(graph)
    
    while queue:
        node, path, time = queue.popleft()
        if node == end:
            return path, len(visited)
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour['stop_name'] not in visited and time < neighbour['departure_time']:
                    queue.append((neighbour['stop_name'],
                                  path + [f'{neighbour["departure_time"]}: {neighbour["stop_name"]} (line {neighbour["line"]})'],
                                  neighbour['departure_time']))
    
    return None, len(visited)