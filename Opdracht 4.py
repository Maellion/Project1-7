# Create a list
my_list = [1, 2, 3, 4,5]
print(my_list)
# Elementen mogen van elk data type zijn
my_list = [1, 2, 3, "four"]
print(my_list)
# Elementen hebben een "index" nummer om hun locatie in de lijst aan te geven. Die index begint bij
print(my_list[-1])
# Elementen toevoegen achteraan een lijst
my_list.append(6)
# ...of op een specifieke locatie
my_list.insert(3, "three")
print(my_list)

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# Tuples zijn niet wijzigbaar
# my_tuple[0] = 6


# Dictionary - zorgt ervoor dat je een waarde geeft aan gene wat voor de : staat
dictionary = {"key": "value"}
print(dictionary)
print(dictionary["key"])
# Dit geeft een nieuwe waarde aan de eerdere dictionary
dictionary["key"] = "new value"
print(dictionary["key"])
# Voegt de nieuwe waarde toe aan de oude value, en print die achter elkaar
dictionary["new key"] = "new value"
print(dictionary)
