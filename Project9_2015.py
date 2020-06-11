import itertools


def total_distance(cities_array, city_list_array):
    distance_traveled = 0
    for number in range(len(city_list_array)-1):
        for index, lst in enumerate(cities_array):
            if city_list_array[number] in lst and city_list_array[number+1] in lst:
                distance_traveled += lst[2]
    return distance_traveled


citys_array = [('City1', 'City2', 'Distance Apart')]
city_array = ['Each City Once']
distance_array = ['distance only']


with open('Project9_2015', 'r') as file:
    for line in file:
        if '\n' in line:
            endofline_factor = -1
        else:
            endofline_factor = None
        city1 = line[:line.find(' ')]
        city2 = line[line.find(' ')+4:line.find('=')-1]
        distance = line[line.find('=')+2:endofline_factor]
        citys_array.append((city1, city2, int(distance)))
        distance_array.append(int(distance))
        if city1 not in city_array:
            city_array.append(city1)
        if city2 not in city_array:
            city_array.append(city2)

# max_distance = max(distance_array[1:])
# max_city1 = citys_array[distance_array.index(max_distance)][0]
# max_city2 = citys_array[distance_array.index(max_distance)][1]
# city_array.insert(1, city_array.pop(city_array.index(max_city1)))
# city_array.insert(len(city_array)-1, city_array.pop(city_array.index(max_city2)))
perm_array = city_array[1:]
route_array = itertools.permutations(perm_array, len(perm_array))
route_array2 = list(route_array)
Route_Distance_array = [500]
for route in route_array2:
    route_distance = total_distance(citys_array, route)
    Route_Distance_array.append(route_distance)
# print(min(Route_Distance_array))
print(max(Route_Distance_array))
