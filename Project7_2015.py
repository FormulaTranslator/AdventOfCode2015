# For part 2, 1674 -> b was changed to 46065 -> b
import Bit16_FUNCS as b16

wire_dictionary = {'operators completed': 0}
file_name = 'Project7_2015'
operation_instructions = []
operations = {
    'NOT': lambda signal, place_holder: b16.BinNot(signal),
    'AND': lambda signal1, signal2: b16.BinAnd(signal1, signal2),
    'OR': lambda signal1, signal2: b16.BinOr(signal1, signal2),
    'RSHIFT': lambda signal1, signal2: b16.BinRshift(signal1, signal2),
    'LSHIFT': lambda signal1, signal2: b16.BinLshift(signal1, signal2)
}
with open(file_name) as file:
    for line in file:
        operation_instructions.append(line.rstrip('\n'))

number_lines = len(operation_instructions)

while wire_dictionary['operators completed'] < number_lines:
    for index, instruction in enumerate(operation_instructions):
        # Define initial variables
        variables = instruction.split()
        number_variables = len(variables)
        to_signal = variables[-1]
        from_signal_is_defined = False
        second_signal_is_defined = False

        # Assign dependant variables from input
        if number_variables == 3:  # No command has only 3 segments
            from_signal = variables[0]
            operation = None
            second_signal = None
        elif number_variables == 4:  # NOT command has only 4 segments
            from_signal = variables[1]
            operation = variables[0]
            second_signal = None
        else:  # All other commands have 5 segments
            from_signal = variables[0]
            operation = variables[1]
            second_signal = variables[2]

        # Define from signal if possible (None will be True to enable operation of NOT operations)
        if from_signal.isnumeric():
            from_signal = int(from_signal)
            from_signal_is_defined = True
        elif from_signal in wire_dictionary:
            from_signal = wire_dictionary[from_signal]
            from_signal_is_defined = True
        # Define second signal if possible (None will be True to enable operation of NOT operations)
        if second_signal is None:
            second_signal_is_defined = True
        elif second_signal.isnumeric():
            second_signal = int(second_signal)
            second_signal_is_defined = True
        elif second_signal in wire_dictionary:
            second_signal = wire_dictionary[second_signal]
            second_signal_is_defined = True

        if operation is None:
            # Simple assign if not operation is given
            if to_signal not in wire_dictionary:
                if from_signal_is_defined:
                    wire_dictionary[to_signal] = from_signal
                    wire_dictionary['operators completed'] += 1
        else:
            # call function based off of operation given
            if from_signal_is_defined and second_signal_is_defined and to_signal not in wire_dictionary:
                wire_dictionary[to_signal] = operations[operation](*[from_signal, second_signal])
                wire_dictionary['operators completed'] += 1

# print(wire_dictionary)
if 'a' in wire_dictionary:
    print(wire_dictionary['a'])
