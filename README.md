## Fastest path and time to travel

Given the length of roads between connected cities and the speed limits needed to obey for each of these roads, the project seeks to find a route from city A to B that takes the least amount of time to drive. 

For roads that have no speed limits, we will maintain the previous speed for such roads.

## Assumptions:

Each specified road is one-way.
The acceleration and deceleration happening at each city is instantaneous
The starting speed is 70km per hour
There is only one unique optimal solution

## Input File Format

The first line of the input file - "fastest.inp" contains 4 integers: N, M, S and Din this order. N is the number of cities, M is the number of roads connecting cities, S is the identifier of the source city and D is the identifier of the destination or target city. The cities are identified using numbers 0 to N-1. In subsequent lines of the file, each road can be described as a 4-tuple: (X,Y,V,L), specifying that the road rom city X to Y has the speed limit of V km per hour and a distance of L km. A road with an unspecified speed limit is given with V=0.

For instance, the data in my input file will result in a graph road network as seen in the image below:

road.png

## Source Code

The source code can be found in the python file - "fastest.py". 

## Running Project Files

Kindly ensure that the input and python file are in the same directory. Navigate to the directory and run the source file. You can use command such as -- "python fastest.py".
Upon successful execution, the program outputs all possible routes between city X and Y, the optimal route and the time taken to travel that route.

## Suggestions? Feedback?

I would love your feedback on this project. Kindly feel free to reach out at persiebrown285@gmail.com
