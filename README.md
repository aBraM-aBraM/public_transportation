# Public Transportation

## Setup

> clone the repository

> cd GSDB && npm install

## Requirements

* simplicity (accessibility)
    * maximal amount of walking time from
        every private house / business
    * minimal amount of changes per route (by type)
        * inner city routes
        * external city routes
        * minimal amount of routes intersections (also increases converage)
* hot spots
    * business areas
    * leisure areas
    * private houses
* limited resources
    * prioritized funding
        * popular routes occur more frequently
        * popular routes get better vehicles
        * route hierarchy (popular main routes, sub-main routes etc.)


* data assumptions
    * bus stations
        * location
        * frequency
        * population per hour

People use public transport for a few main purposes:
* Getting to work and back home
* Getting to leisure/business centers and back home
* Getting between leisure/business
* Traveling around the state

Instead of trying to categorize each purposes manually routes
should be separated by popularity.

## Route Categorization


```py

def get_paths(bus_stops: List[BusStop]) -> List[Path]:
    paths: List[Path]
    for bus_stop in bus_stops:
        if bus_stop.previous == None:
            end_stop = bus_stop
            end_stop = end_stop.next while end_stop.next != None
            paths.append(Path(start: bus_stop, end: end_stop))
    return paths

def get_close_paths(paths: List[Path]) -> List[List[Path]]:
    close_paths_list: List[List[Path]]

    for path in paths:        
        close_paths: List[Path]
        close_paths.append(path.start)

        for other_path in paths:
            if path != other_path:
                close_start = path.start.distance(other_path.start) < distance_threshold
                close_end = path.end.distance(other_path.end) < distance_threshold
                if close_start and close_end:
                    close_start_paths.append(other_path.start)


        close_paths_list.append(close_paths)
    return close_paths_list

def get_distant_paths(path_lists: List[List[Path]]) -> List[List[path]]:
    different_paths_list: List[List[path]]

    for close_path in path_lists:
        sort(path, )
        distant_paths: List[Path]

def get_popular_location_paths(paths: List[Path]) -> List[Path]:
    distance_threshold # radius for area assumed to be same
    # tuning this parameter is an important task

    hot_spots: List[List[path]] = get_close_paths(paths)

    for paths in hot_spots:
        sort(paths, by: population)
        for path in paths:
            for other_path in paths:


    similar_start_paths: List[Path] = 

def get_popular_paths(paths: List[Path]):
    distance_threshold # radius for area assumed to be same
    # tuning this parameter is an important task


    
```