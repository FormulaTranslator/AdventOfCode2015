from copy import deepcopy
# Initialize variables
steps = 100
off_on = 3
stay_on = (2, 3)
Project_file = 'Project18_2015'

# Create light grid based on file dimensions
with open(Project_file) as file:
    first_line = file.readline().rstrip('\n')
    number_columns = len(first_line)
    number_rows = len(file.readlines()) + 1  # plus 1 for the readline() above
    light_grid = [[0 for i in range(number_columns)] for j in range(number_rows)]

# Initialize the grid with starting positions
with open(Project_file) as file:
    for y in range(len(light_grid)):
        line = file.readline()
        line = line.rstrip('\n')
        for x, char in enumerate(line):
            if char == '#':
                light_grid[y][x] = 1
            else:
                light_grid[y][x] = 0


def get_surrounding_lights(x_pos, y_pos, grid):
    """Creates a 3x3 list around the specified point.
     It then sums up the list and subtracts the specified point to get the value of the 8 'neighbors' around it"""
    x_start = max(0, x_pos - 1)
    x_end = min(x_pos + 1, len(grid[y_pos])-1)
    y_start = max(0, y_pos - 1)
    y_end = min(y_pos + 1, len(grid)-1)

    neighbor_list = []
    for row in grid[y_start:y_end+1]:
        neighbor_list.append(row[x_start:x_end+1])

    lights_on = sum(sum(neighbor_list, [])) - grid[y_pos][x_pos]
    return lights_on


def corner_lights(l_grid):
    """Returns the given list, but with the corner indices set to 1"""
    l_grid[0][0] = 1
    l_grid[0][number_columns - 1] = 1
    l_grid[number_rows - 1][0] = 1
    l_grid[number_rows - 1][number_columns-1] = 1
    return l_grid


# Step through each step
step_grid = deepcopy(corner_lights(light_grid))  # deepcopy makes sure that the lists don't point to the same bits
for step in range(steps):
    for y_coord in range(len(light_grid)):
        for x_coord in range(len(light_grid[0])):
            number_surrounding_lights = get_surrounding_lights(x_coord, y_coord, light_grid)
            if light_grid[y_coord][x_coord]:
                if number_surrounding_lights not in stay_on:
                    step_grid[y_coord][x_coord] = 0
            else:
                if number_surrounding_lights == off_on:
                    step_grid[y_coord][x_coord] = 1

    light_grid = deepcopy(corner_lights(step_grid))

# Get the final answer (how many lights are on)
final_lights_on = sum(sum(light_grid, []))
print(final_lights_on)
