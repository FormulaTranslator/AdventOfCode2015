x_coordinate1 = 0
y_coordinate1 = 0
x_coordinate2 = 0
y_coordinate2 = 0
coordinate_list = [(0, 0)]

with open('Project3_2015', 'r') as file:
    direction_file = file.read()

for index, char in enumerate(direction_file):
    if index % 2 == 0:
        if char == '>':
            x_coordinate1 += 1
        elif char == '^':
            y_coordinate1 += 1
        elif char == '<':
            x_coordinate1 -= 1
        elif char == 'v':
            y_coordinate1 -= 1
        if coordinate_list.count((x_coordinate1, y_coordinate1)) == 0:
            coordinate_list.append((x_coordinate1, y_coordinate1))
    else:
        if char == '>':
            x_coordinate2 += 1
        elif char == '^':
            y_coordinate2 += 1
        elif char == '<':
            x_coordinate2 -= 1
        elif char == 'v':
            y_coordinate2 -= 1
        if coordinate_list.count((x_coordinate2, y_coordinate2)) == 0:
            coordinate_list.append((x_coordinate2, y_coordinate2))

print(len(coordinate_list))
