box_dimensions = [0, 0, 0]
box_dimensions_area = [0, 0, 0]
box_dimensions_perimeter = 0
box_surface_area = 0
box_wrapper_sq = 0
total_wrapper = 0
box_ribbon = 0
total_ribbon = 0
current_number = ''

with open('Project2_2015', 'r') as file:
    for index, lines in enumerate(file):
        current_line = lines
        side_tracker = 0
        for char_index, char in enumerate(current_line):
            if char == 'x':
                box_dimensions[side_tracker] = int(current_number)
                side_tracker += 1
                current_number = ''
            elif char_index + 1 == len(current_line):
                if current_number == '':
                    current_number += char
                box_dimensions[side_tracker] = int(current_number)
                current_number = ''
                box_dimensions_area[0] = box_dimensions[0] * box_dimensions[1]
                box_dimensions_area[1] = box_dimensions[1] * box_dimensions[2]
                box_dimensions_area[2] = box_dimensions[2] * box_dimensions[0]
                box_dimensions.sort()
                box_dimensions_perimeter = 2*(box_dimensions[0] + box_dimensions[1])
                box_ribbon = box_dimensions_perimeter + (box_dimensions[0]*box_dimensions[1]*box_dimensions[2])
                box_dimensions_area.sort()
                box_surface_area = 2 * (box_dimensions_area[0] + box_dimensions_area[1] + box_dimensions_area[2])
                box_wrapper_sq = box_surface_area + box_dimensions_area[0]
                total_wrapper += box_wrapper_sq
                total_ribbon += box_ribbon
            else:
                current_number += char

print(total_wrapper)
print(total_ribbon)
