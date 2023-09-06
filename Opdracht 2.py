line_character = "-"
line = line_character * 20
# Display large numbers in a readable format
people = 7861304740
print(people)
# Je mag underscores gebruiken om getallen leesbaar te maken
people = 7_861_304_740
print(people)

print(line)

people = 7_861_304_740
# Calculations with big numbers
meals = 3
people_eat = people * meals
print(people_eat)

# What is the data type?
days = 365
meals_per_year = people_eat * days
print(type(meals_per_year))
print(meals_per_year)

print(line)

ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(maximum_capacity)

print(line)

ethernet_speed_mbps = 1000
download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(usage)

print(line)

# Speed of light in m/s
speed_of_light = 299_792_458

# Distance Rotterdam / New York in km
distance_Rotterdam_NewYork = 5_862.03
# Distance Rotterdam to New York in meters divided by the speed of light
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(f"Time to reach New York is: {time_to_reach_NYC} seconds => {time_to_reach_NYC * 1000.0} milliseconds.")







