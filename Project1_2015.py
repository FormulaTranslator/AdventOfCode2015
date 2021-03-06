with open('Project1_2015', 'r') as file:
    current_file = file.read()
floor_counter = 0
basement_position = None

for index, char in enumerate(current_file):
    if char == '(':
        floor_counter += 1
    else:
        floor_counter -= 1

    if basement_position is None and floor_counter == -1:
        basement_position = index + 1

print(floor_counter)
print(basement_position)
