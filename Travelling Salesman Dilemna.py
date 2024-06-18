from itertools import permutations

# setting distance and time in km
distance_matrix = {
    "Nairobi": {"Nyeri": 153.8, "Nakuru": 162.1, "Laikipia": 160.5, "Nandi": 89.3, "Meru": 228.9},
    "Nyeri": {"Nairobi": 143.3, "Nakuru": 166.8, "Laikipia": 130.0, "Nandi": 214.0, "Meru": 136.5},
    "Nakuru": {"Nairobi": 159.3, "Nyeri": 166.8, "Laikipia": 249.4, "Nandi": 156.3, "Meru": 256.0},
    "Laikipia": {"Nairobi": 265.8, "Nyeri": 130.0, "Nakuru": 249.5, "Nandi": 186.0, "Meru": 103.2},
    "Nandi": {"Nairobi": 89.3, "Nyeri": 214.0, "Nakuru": 154.0, "Laikipia": 186.0, "Meru": 281.0},
    "Meru": {"Nairobi": 225.9, "Nyeri": 136.5, "Nakuru": 256.0, "Laikipia": 143.4, "Nandi": 281.0},
}

# setting average speed and fuel consumption
average_speed = 80  #  speed in km/h
fuel_consumption = 12.6  # consumption in km/l
petrol_price = 199.15  # price in shillings/liter

def calculate_travel_time(distance):
    """Calculates travel time based on distance and average speed"""
    return distance / average_speed

def calculate_total_distance(route):
    """Calculates total distance for a given route"""
    distance = 0
    for i in range(len(route) - 1):
        origin = route[i]
        destination = route[i + 1]
        distance += distance_matrix[origin][destination]
         #return to Nairobi
    distance += distance_matrix[route[-1]][route[0]] 
    return distance

def calculate_total_time(route):
    """Calculates total travel time for a given route"""
    total_distance = calculate_total_distance(route)
    return calculate_travel_time(total_distance)

def calculate_fuel_amount(distance):
    """Calculates the amount of fuel needed based on distance and fuel consumption"""
    # rounding to four decimal places
    return round(distance / fuel_consumption, 4)  

def calculate_fuel_cost(distance):
    """Calculates the cost of fuel based on distance, fuel consumption, and petrol price"""
    fuel_amount = calculate_fuel_amount(distance)
    # rounding to two decimal places
    return round(fuel_amount * petrol_price, 2)  

def find_shortest_route(cities):
    """Finds the shortest route using nearest neighbor heuristic"""
    shortest_distance = float("inf")
    shortest_route = None
    shortest_time = None
    for permutation in permutations(cities):
        route_distance = calculate_total_distance(permutation)
        route_time = calculate_total_time(permutation)
        if route_distance < shortest_distance:
            shortest_distance = route_distance
            shortest_route = permutation
            shortest_time = route_time
    return shortest_route, shortest_distance, shortest_time

# listing countries
counties = ["Nyeri", "Nakuru", "Laikipia", "Nandi", "Meru"]

# find shortest route and distance
shortest_route, shortest_distance, shortest_time = find_shortest_route(counties)

# calculate fuel amount and cost
fuel_amount = calculate_fuel_amount(shortest_distance)
fuel_cost = calculate_fuel_cost(shortest_distance)

# print the results with formatting for decimal places
print("Shortest Route:", shortest_route)
print("Total Distance:", "{:.1f}".format(shortest_distance), "km")
print("Total Travel Time:", shortest_time, "hours")
print("Fuel Amount Needed:", "{:.4f}".format(fuel_amount), "liters")
print("Fuel Cost:", "{:.2f}".format(fuel_cost), "shillings")