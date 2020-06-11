import Bit16_FUNCS as b16

max_value = 65535
wire_dictionary = {'operators completed': 0}
file_name = 'Project7_2015'


with open(file_name) as file:
    number_lines = file.read().count('\n')

while wire_dictionary['operators completed'] < number_lines+1:
    # operators_complete = 0
    with open(file_name) as file:
        for index, line in enumerate(file):
            if line[len(line)-1] == '\n':
                end_of_line = -1
            else:
                end_of_line = None

            if 'NOT' in line:
                from_signal = line[line.find(' ')+1:line.find('->')-1]
                to_signal = line[line.find('->') + 3:end_of_line]
                if from_signal in wire_dictionary and to_signal not in wire_dictionary:
                    wire_dictionary[to_signal] = b16.BinNot(wire_dictionary[from_signal])
                    wire_dictionary['operators completed'] += 1
                    if wire_dictionary[to_signal] > max_value:
                        wire_dictionary[to_signal] = max_value

            elif ' OR ' in line:
                from_signal1 = line[:line.find(' ')]
                from_signal2 = line[line.find('OR') + 3:line.find('->') - 1]
                to_signal = line[line.find('->') + 3:end_of_line]
                if from_signal1.isalpha() and from_signal2.isalpha() and to_signal not in wire_dictionary:
                    if from_signal1 in wire_dictionary and from_signal2 in wire_dictionary and to_signal not in wire_dictionary:
                        wire_dictionary[to_signal] = b16.BinOr(wire_dictionary[from_signal1], wire_dictionary[from_signal2])
                        wire_dictionary['operators completed'] += 1
                        if wire_dictionary[to_signal] > max_value:
                            wire_dictionary[to_signal] = max_value
                elif from_signal1.isalpha():
                    if from_signal1 in wire_dictionary and to_signal not in wire_dictionary:
                        wire_dictionary[to_signal] = b16.BinOr(wire_dictionary[from_signal1], int(from_signal2))
                        wire_dictionary['operators completed'] += 1
                        if wire_dictionary[to_signal] > max_value:
                            wire_dictionary[to_signal] = max_value
                elif from_signal2.isalpha():
                    if from_signal2 in wire_dictionary and to_signal not in wire_dictionary:
                        wire_dictionary[to_signal] = b16.BinOr(int(from_signal1), wire_dictionary[from_signal2])
                        wire_dictionary['operators completed'] += 1
                        if wire_dictionary[to_signal] > max_value:
                            wire_dictionary[to_signal] = max_value

            elif 'AND' in line:
                from_signal1 = line[:line.find(' ')]
                from_signal2 = line[line.find('AND') + 4:line.find('->') - 1]
                to_signal = line[line.find('->') + 3:end_of_line]
                if from_signal1.isalpha() and from_signal2.isalpha() and to_signal not in wire_dictionary:
                    if from_signal1 in wire_dictionary and from_signal2 in wire_dictionary and to_signal not in wire_dictionary:
                        wire_dictionary[to_signal] = b16.BinAnd(wire_dictionary[from_signal1], wire_dictionary[from_signal2])
                        wire_dictionary['operators completed'] += 1
                        if wire_dictionary[to_signal] > max_value:
                            wire_dictionary[to_signal] = max_value
                elif from_signal1.isalpha() and to_signal not in wire_dictionary:
                    if from_signal1 in wire_dictionary and to_signal not in wire_dictionary:
                        wire_dictionary[to_signal] = b16.BinAnd(wire_dictionary[from_signal1], int(from_signal2))
                        wire_dictionary['operators completed'] += 1
                        if wire_dictionary[to_signal] > max_value:
                            wire_dictionary[to_signal] = max_value
                elif from_signal2.isalpha() and to_signal not in wire_dictionary:
                    if from_signal2 in wire_dictionary and to_signal not in wire_dictionary:
                        wire_dictionary[to_signal] = b16.BinAnd(int(from_signal1), wire_dictionary[from_signal2])
                        wire_dictionary['operators completed'] += 1
                        if wire_dictionary[to_signal] > max_value:
                            wire_dictionary[to_signal] = max_value

            elif 'LSHIFT' in line:
                from_signal = line[:line.find(' ')]
                shift_number = int(line[line.find('LSHIFT') + 7:line.find('->') - 1])
                to_signal = line[line.find('->') + 3:end_of_line]
                if to_signal == 'w':
                    test = 1
                if from_signal in wire_dictionary and to_signal not in wire_dictionary:
                    wire_dictionary[to_signal] = b16.BinLshift(wire_dictionary[from_signal], shift_number)
                    wire_dictionary['operators completed'] += 1
                    if wire_dictionary[to_signal] > max_value:
                        wire_dictionary[to_signal] = max_value

            elif 'RSHIFT' in line:
                from_signal = line[:line.find(' ')]
                shift_number = int(line[line.find('RSHIFT')+7:line.find('->') - 1])
                to_signal = line[line.find('->') + 3:-1]
                if from_signal in wire_dictionary and to_signal not in wire_dictionary:
                    wire_dictionary[to_signal] = b16.BinRshift(wire_dictionary[from_signal], shift_number)
                    wire_dictionary['operators completed'] += 1
                    if wire_dictionary[to_signal] > max_value:
                        wire_dictionary[to_signal] = max_value

            elif line[0].isalpha():
                from_signal = line[:line.find(' ')]
                to_signal = line[line.find('->') + 3:end_of_line]
                if from_signal in wire_dictionary and to_signal not in wire_dictionary:
                    wire_dictionary[to_signal] = wire_dictionary[from_signal]
                    wire_dictionary['operators completed'] += 1
                    if wire_dictionary[to_signal] > max_value:
                        wire_dictionary[to_signal] = max_value

            else:
                value = int(line[:line.find(' ')])
                to_signal = line[line.find('->') + 3:end_of_line]
                if to_signal not in wire_dictionary:
                    wire_dictionary[to_signal] = value
                    wire_dictionary['operators completed'] += 1
                    if wire_dictionary[to_signal] > max_value:
                        wire_dictionary[to_signal] = max_value
print(wire_dictionary)
if 'a' in wire_dictionary:
    print(wire_dictionary['a'])
if 'or' in wire_dictionary:
    print(wire_dictionary['or'])
