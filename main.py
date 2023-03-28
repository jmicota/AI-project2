from data import extract_data, build_search_graph_dictionaries
import dfs, bfs
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


stop_str_names = [stop_names[key] for key in stop_names.keys()]
if 'Hlidar' in stop_str_names:
    print('Hlidar!')
if 'Skeifan' in stop_str_names:
    print('Skeifan!')


while True:
    print()
    print('Select test:')
    print('(0) Check if stop exists in database')
    print('(1) Check reachability of all stop pairs with DFS')
    print('(2) Check reachability between two stops with DFS')
    print('(3) Calculate shortest distance between two stops with BFS')
    choice = input('---> ')
    # validate choice
    if not choice.isdigit():
        print('Selected value does not represent valid choice')
        continue

    if int(choice) == 0:
        stop_name = input('Input stop name: ')
        if stop_name in stop_str_names:
            print('Stop exists')
        else:
            print('Stop not found')

    elif int(choice) == 1:
        all_stop_ids = [key for key in stop_names.keys()]
        dfs.check_all(all_stop_ids, stop_neighbours, stop_names)

    elif int(choice) == 2:
        print('Example stops existing: Hlidar, Skeifan, Sunnuhlid, Kopavogsskoli, Smaralind')
        stop1 = input('Stop 1: ')
        stop2 = input('Stop 2: ')
        result = dfs.dfs(stop_neighbours, stop_ids[stop1], stop_ids[stop2], [])
        if result == None:
            print('Stops unreachable')
        else:
            print('Stops reachable, list of visited stop IDs during execution of DFS:')
        print(result)

    elif int(choice) == 3:
        print('Example stops existing: Hlidar, Skeifan, Sunnuhlid, Kopavogsskoli, Smaralind')
        stop1 = input('Stop 1: ')
        stop2 = input('Stop 2: ')
        result = bfs.bfs(stop_neighbours, stop_ids[stop1], stop_ids[stop2])
        if result == -1:
            print('Stops unreachable')
        else:
            print(f'Shortest distance in nr of stops: {result}')


# dfs_result = dfs.dfs(stop_neighbours, stop_ids['Hlidar'], stop_ids['Skeifan'], [])


# print('yo')