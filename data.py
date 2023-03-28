import pandas as pd
import csv


# Put data from a file into a local list of dictionaries
def extract_data(file, skip_keys=[]):
    result = []
    with open(f'./data/{file}', 'r') as f:
        reader = csv.reader(f, delimiter=',', quoting = csv.QUOTE_NONE)
        rows = []
        for row in reader:
            rows.append(row)

        keys = []
        for i in range(len(rows)):
            if i == 0:
                for key in rows[i]:
                    keys.append(key)
            else:
                entry = {}
                for entry_i in range(len(rows[i])):
                    entry[keys[entry_i]] = rows[i][entry_i]
                result.append(entry)

    for entry in result:
        for skip_key in skip_keys:
            del entry[skip_key]

    return result


def build_search_graph_dictionaries(routes_data, stop_times_data, stops_data, trips_data):
    # extract stop_names, and initialize stop_neighbours with empty neighbours array
    stop_names = {}
    stop_ids = {}
    stop_neighbours = {}
    route_lines = {}
    trips = {}

    # extract stop names
    for stop in stops_data:
        stop_neighbours[stop['stop_name']] = []
        stop_names[stop['stop_id']] = stop['stop_name']
        stop_ids[stop['stop_name']] = stop['stop_id']

    # extract line numbers
    for route in routes_data:
        route_lines[route['route_id']] = route['route_short_name']

    # initialize trip info
    for trip in trips_data:
        trip_id = trip['trip_id']
        line = route_lines[trip['route_id']]
        direction = trip['direction_id']
        entry = {
            'line': line,
            'direction': direction,
            'stops': []
        }
        trips[trip_id] = entry

    # extract stops for trips
    for stop in stop_times_data:
        trip_id = stop['trip_id']
        stop_entry = {}
        stop_entry['stop_id'] = stop['stop_id']
        stop_entry['stop_name'] = stop_names[stop['stop_id']]
        stop_entry['stop_sequence'] = stop['stop_sequence']
        stop_entry['arrival_time'] = stop['arrival_time']
        stop_entry['departure_time'] = stop['departure_time']
        trips[trip_id]['stops'].append(stop_entry)

    # extract end stop for trips
    for key in trips.keys():
        trip_stops = trips[key]['stops']
        trips[key]['direction'] = trip_stops[len(trip_stops) - 1]['stop_name']

    # extract neighbour stops for graph
    for key in trips.keys():
        trip = trips[key]
        trip_stops = trip['stops']
        for i in range(len(trip_stops)):
            if i < len(trip_stops) - 1:
                next_stop = trip_stops[i + 1]
                neighbour_entry = {}
                neighbour_entry['stop_name'] = next_stop['stop_name']
                neighbour_entry['departure_time'] = next_stop['departure_time']
                # neighbour_entry['arrival_time'] = next_stop['arrival_time']
                neighbour_entry['line'] = trip['line']
                neighbour_entry['direction'] = trip['direction']
                stop_neighbours[trip_stops[i]['stop_name']].append(neighbour_entry)


    # delete Hamraborg from stop list, since it doesnt appear in any trip
    del stop_names['10000802']
    del stop_ids['Hamraborg']
    
    return route_lines, stop_names, stop_ids, stop_neighbours, trips