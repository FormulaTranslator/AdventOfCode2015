def get_houses(directions_str, house=(0, 0)):
    houses = {house}
    for direction in directions_str:
        house = get_houses.move[direction](*house)
        houses.add(house)
    return houses


# This dictionary holds the equations for the various moves, like case conditions in VBA
get_houses.move = {
    '>': lambda x, y: (x + 1, y),
    '^': lambda x, y: (x, y + 1),
    '<': lambda x, y: (x - 1, y),
    'v': lambda x, y: (x, y - 1)
}

with open('Project3_2015', 'r') as file:
    directions = file.read()


houses_visited = get_houses(directions)
print(len(houses_visited))

# | unions the 2 sets
year2_houses_visited = get_houses(directions[::2]) | get_houses(directions[1::2])
print(len(year2_houses_visited))
