total_wrapper = 0
total_ribbon = 0

with open('Project2_2015', 'r') as file:
    for lines in file:
        length, width, height = sorted(int(i) for i in lines.split('x'))
        area = 2 * (length * width + width * height + height * length)
        smallest_side = length * width
        total_wrapper += area + smallest_side

        box_volume = length * width * height
        smallest_perimeter = 2 * (length + width)
        total_ribbon += box_volume + smallest_perimeter

print(total_wrapper)
print(total_ribbon)
