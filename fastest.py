"""
@author: Percy Brown

Project Description: Finding the optimal route between two cities in a directed graph of cities with the distance and speed limit between them
The optimal route is one that takes a shorter time to travel, where time is the distance / speed
A starting speed of 70km per hour is assumed
If the speed of a route is unknown (indicated as 0), the previous speed is used
There is only one unique optimal solution
"""

from collections import defaultdict  # will use the dictionary to illustrate our road network like an adjacency list

"""
The class defines properties and methods to help identify the optimal route
The road network is represented as an adjacency list using a dictionary
"""
class OptimalRoute:
    # parameterized constructor
    def __init__(self, cities):
        self.cities = cities   # indicate number of cities
        graph_content = defaultdict
        self.road_network = graph_content(list)  # the dictionary will store a city as the key and a list of its neighbours as the values

    """
    Function below creates a connection between two cities if they are neighbours
    For instance if you can move from city 0 to 1 in a directed road network, then city 0 will have city 1 as part of a list of its neighbors
    """

    def connect_city(self, city, neighbor):
       self.road_network[city].append(neighbor)

    # Function below returns road network in the form of dictionary

    def display_graph(self):
        return self.road_network

    # function finds all possible paths between source and destination cities
    def find_all_routes(self, road_network, source, target, route=[]):
            
             # add source city to route to start with
            route = route + [source]

            # base case is when the source is the same as the target i.e we have exhausted the traversal, then we return the route
            if source == target:
                return [route] 
             
            if source not in road_network:  # if the source city is not found in the graph of road network then we return an empty list of no possible paths
                return []
            
            all_possible_routes = []  # list to store a list of all possible paths

            """
            Go through the other cities and check if they haven't been visited. 
            If any intermediary neighbor hasn't been visited then then it becomes the "temporary source" 
            Set it as visited and add it to the current set of routes
            """

            for temp_src in road_network[source]:
                if temp_src not in route:
                    newpaths = self.find_all_routes(road_network, temp_src, target, route)
                    for newpath in newpaths:
                        all_possible_routes.append(newpath)
            return all_possible_routes

    """
    Function below calculates time taken to travel from one city to another
    It returns the time and the previous speed
    """
    def time_btn_two_cities(self, tupl, starting_speed, previous_speed):
        time = 0.0

        # if both a city's speed and previous speed is 0 then the starting speed becomes the city's speed as well as the previous speed for the next road trip
        if tupl[2] == 0 and previous_speed == 0:
            previous_speed = starting_speed
            speed = tupl[2] + previous_speed # speed = previous speed
            time = tupl[3]/speed
        
        # if a city's speed is 0 but there exists a previous speed then that becomes the speed assigned to the city
        if tupl[2] == 0 and previous_speed !=0:
            speed = tupl[2] + previous_speed # speed = previous speed
            time = tupl[3]/speed

        # if the city speed is not zero then the previous speed for the next trip becomes the speed of the current city under consideration
        else:
            time = tupl[3]/tupl[2]
            previous_speed = tupl[2] # previous speed is current city's speed
        
        # return time and previous speed
        return time, previous_speed


"""
Main function to read the text file, obtain the various details to execute the class methods
"""
def main():

    # read text file
    with open('fastest.inp') as input_file:
        first_line = input_file.readline() # obtain the first line

        list_of_tuples = []  # list to contain all tuples from each line

        # go through subsequent M lines and generate tuples for each line. 
        for line in input_file:
            road_tuple = tuple(map(int, line.split()))  # split X,Y,V,L as a tuple of integers

            if(len(road_tuple)==0):  # ignore empty tuple which may be the last empty line in the text file
                continue
            list_of_tuples.append(road_tuple) # put all the tuples into a list
        
    first_line_details = tuple(map(int, first_line.split()))  # since the integers are space-delimited, split them by the space character into a tuple
    N, M, S, D = first_line_details  # get the values N, M and D from the first line
    
    fastest = OptimalRoute(N)  # create road network with N number of cities

    """
    Create connection (road) between two cities for the M number of roads
    The first element in the tuple is the source city (index 0) and the second is the destination city (index 1)
    """

    for i in range(M): 
        fastest.connect_city(list_of_tuples[i][0], list_of_tuples[i][1])

    # define source and destination cities


    road_network = fastest.display_graph()  # graph of road network as a dictionary in the form of an adjacency list
    all_possible_routes = fastest.find_all_routes(road_network, S, D) # all possible routes between from the source to destination city
 
    
    starting_speed = 70  # starting speed is 70km per hour
    previous_speed = 0   # no previous speed initially
   
    routeDict = {}   # dictionary to contain all possible_routes as keys (using their index) and corresponding time as the value

    """
    Go through the possible routes and check if a route just consists of 2 cities
    Calculate the distance and add the index of the route and the corresponding time to the dictionary
    """

    for i in all_possible_routes:
        for j in list_of_tuples:
            # when the route has just one road (2 cities involved) and the city identifiers are in the list of tuples
            if len(i)== 2 and i[0] == j[0] and i[1] == j[1]:
                time, previous_speed = fastest.time_btn_two_cities(j, starting_speed, previous_speed)
                routeDict[all_possible_routes.index(i)] = time

 
    consec = []  # list to store list of consecutive pairs of route with more than two cities
    """
    If there are more than 2 cities for a route, generate a list of consecutive pairs for that route
    Put all consecutive pairs in a list
    """

    for i in all_possible_routes:
        if len(i) > 2:
            consecutive_city_pairs = list(zip(i, i[1:]))
            consec.append(consecutive_city_pairs)
    
    """
    Go through the list of consecutive pairs for each route with more than 2 cities
    For each pair in the list of consecutive pairs of a particular route, calculate the distance between the two cities of each pair
    Add all the time taken to travel the consecutive pairs of the route
    Add the index of the route and its corresponding time to the dictionary
    """

    for i in consec:
        total = 0.0
        previous_speed = 0.0
        for k in i:
            for j in list_of_tuples:
               if len(k)== 2 and k[0] == j[0] and k[1] == j[1]: 
                    time, previous_speed = fastest.time_btn_two_cities(j, starting_speed, previous_speed)
                    total+=time

        # the lines below concatenates the consecutive pairs of cities for a route back into a list of all cities involved in the route
        original_route = []
        for x in i:
            original_route = original_route + list(x)
        original_route = list( dict.fromkeys(original_route) )  # remove duplicates while concatenating city identifiers
        routeDict[all_possible_routes.index(original_route)] = round(total, 4)  # add route index and time calculated to dictionary

    # get key of the route with the minimum time as its value
    optimal_route_key = min(routeDict, key=routeDict.get)
    min_time = routeDict.get(optimal_route_key)
    # get the optimal route from the possible routes using the key as identifier
    optimal_route = all_possible_routes[optimal_route_key]

    # the optimal route is a list with the cities so it's converted to arrow-delimited city identifiers
    optimal_route = '->'.join(map(str, optimal_route))

    # print all possible routes
    print("These are the possible routes from city " + str(S) + " city " + str(D) + "\n")
    print(all_possible_routes)
    print("\n")

    # print optimal route into output file - fastest.out
    print("Of all the possible routes, the fastest is " + optimal_route + " and the time taken to travel this route is " + str(min_time) + " hours")


main()

