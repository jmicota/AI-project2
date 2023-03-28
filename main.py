from data import extract_data, build_search_graph_dictionaries
import dfs, bfs
import time
# PYDEVD_CONTAINER_RANDOM_ACCESS_MAX_ITEMS = 1400

AGENCY_FILE = 'agency.txt'
CALENDAR_DATES_FILE = 'calendar_dates.txt'
ROUTES_FILE = 'routes.txt'
SHAPES_FILE = 'shapes.txt'
STOP_TIMES_FILE = 'stop_times.txt'
STOPS_FILE = 'stops.txt'
TRIPS_FILE = 'trips.txt'


print('---> Reading data..')
routes_data = extract_data(ROUTES_FILE, skip_keys=['route_long_name'])
stop_times_data = extract_data(STOP_TIMES_FILE, skip_keys=['pickup_type'])
stops_data = extract_data(STOPS_FILE, skip_keys=['stop_lat', 'stop_lon', 'location_type'])
trips_data = extract_data(TRIPS_FILE, skip_keys=['service_id', 'shape_id', 'block_id'])
print('---> Data saved successfully')


print('---> Building search environment..')
route_lines, stop_names, stop_ids, stop_neighbours, trips = \
    build_search_graph_dictionaries(routes_data, stop_times_data, stops_data, trips_data)
print('---> Success')
print(f'Stops: {len(stop_neighbours.keys())}; Trips: {len(trips)}, Lines: {len(route_lines)}')


stop_str_names = list(set([stop_names[key] for key in stop_names.keys()]))
if 'Hlidar' in stop_str_names:
    print('Hlidar!')
if 'Skeifan' in stop_str_names:
    print('Skeifan!')


while True:
    print()
    print('Example stop names: Hlidar, Skeifan, Sunnuhlid, Kopavogsskoli, Smaralind')
    print('SELECT TEST:')
    print('(1) DFS: Stop reachability')
    print('(2) BFS: Shortest distance')
    print('(3) BFS: Shortest path')
    print('(4) BFS: Shortest path and valid stop times')
    print('(5) BFS: Shortest path and optimal stop times')
    choice = input('---> ')
    # validate choice
    if not choice.isdigit():
        print('Selected value does not represent valid choice')
        continue

    # DFS for one stop pair
    if int(choice) == 1:
        stop1 = input('Stop 1: ')
        stop2 = input('Stop 2: ')
        result = dfs.dfs(stop_neighbours, stop1, stop2, [])
        if result == None:
            print('Stops unreachable')
        else:
            print('Stops reachable, list of visited stop IDs during execution of DFS:')
        print(result)

    # BFS for one stop pair
    elif int(choice) == 2:
        stop1 = input('Stop 1: ')
        stop2 = input('Stop 2: ')
        result = bfs.bfs(stop_neighbours, stop1, stop2)
        if result == -1:
            print('Stops unreachable')
        else:
            print(f'Shortest distance in nr of stops: {result}')

    # BFS for one stop pair with stop list
    elif int(choice) == 3:
        stop1 = input('Stop 1: ')
        stop2 = input('Stop 2: ')
        result = bfs.bfs_with_path(stop_neighbours, stop1, stop2)
        if result == None:
            print('Stops unreachable')
        else:
            for stop in result:
                print(stop)

    # BFS for one stop pair with stop list and time
    elif int(choice) == 4:
        stop1 = input('Stop 1: ')
        stop2 = input('Stop 2: ')
        start_time = input('Input start time in format \'%H:%M:%S\': ')
        result = bfs.bfs_with_path_and_time(stop_neighbours, stop1, stop2, start_time)
        if result == None:
            print('Stops unreachable')
        else:
            for stop in result:
                print(stop)

    # BFS for one stop pair with stop list and time
    elif int(choice) == 5:
        stop1 = input('Stop 1: ')
        stop2 = input('Stop 2: ')
        start_time = input('Input start time in format \'%H:%M:%S\': ')
        result = bfs.bfs_with_path_and_correct_time(stop_neighbours, stop1, stop2, start_time)
        if result == None:
            print('Stops unreachable')
        else:
            for stop in result:
                print(stop)
