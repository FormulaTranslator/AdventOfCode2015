array_length = 1000
array_width = 1000
Light_array = [[0 for length in range(array_length)] for width in range(array_width)]

with open('Project6_2015') as file:
    for line in file:
        first_comma = line.find(',')
        start_first_index = line.rfind(' ', 0, first_comma) + 1
        through_position = line.find('through')
        end_first_index = through_position - 1
        second_index_start = line.find(' ', through_position)
        second_comma = line.find(',', through_position)
        first_index_first_number = int(line[start_first_index:first_comma])
        first_index_second_number = int(line[first_comma+1:end_first_index])
        second_index_first_number = int(line[second_index_start+1:second_comma-len(line)])
        second_index_second_number = int(line[second_comma+1:])

        i = first_index_first_number

        while i <= second_index_first_number:
            j = first_index_second_number
            while j <= second_index_second_number:
                if 'turn on' in line:
                    Light_array[i][j] += 1
                elif 'turn off' in line:
                    if Light_array[i][j] > 0:
                        Light_array[i][j] -= 1
                elif 'toggle' in line:
                    Light_array[i][j] += 2
                j += 1
            i += 1

# Lights_on = sum(line.count(1) for line in Light_array)
Light_brightness = sum(sum(line) for line in Light_array)
print(Light_brightness)
