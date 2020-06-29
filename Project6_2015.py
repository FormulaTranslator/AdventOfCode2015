array_length = 1000
array_width = 1000
Light_array = [[0 for length in range(array_length)] for width in range(array_width)]

with open('Project6_2015') as file:
    for line in file:
        instructions = line.rstrip('\n').split()
        index = instructions.index('through')
        first_index_first_number, first_index_second_number = [int(i) for i in instructions[index-1].split(',')]
        second_index_first_number, second_index_second_number = [int(i) for i in instructions[index+1].split(',')]

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
