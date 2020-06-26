instructions = {
                'hlf': lambda register: register/2,
                'tpl': lambda register: register*3,
                'inc': lambda register: register+1,
                'jmp': lambda jump, ind: ind + jump,
                'jie': lambda register, jump, ind: instructions['jmp'](*[jump, ind]) if register % 2 == 0 else ind+1,
                'jio': lambda register, jump, ind: instructions['jmp'](*[jump, ind]) if register == 1 else ind+1
}

instructions_list = []
with open('Project23_2015') as file:
                for line in file:
                    split_line = line.split()
                    split_line = [x.rstrip(',') for x in split_line]
                    split_line = [x.rstrip('\n') for x in split_line]
                    instructions_list.append(split_line)

registers = {'a': 1, 'b': 0}
index = 0

while True:
    instruction = instructions_list[index]
    command = instruction[0]

    if command != 'jmp':
                    register = instruction[1]
                    if 'j' not in command:
                        index += 1
                        registers[register] = instructions[command](registers[register])
                    else:
                        jump_value = int(instruction[2])
                        index = instructions[command](*[registers[register], jump_value, index])
    else:
        jump_value = int(instruction[1])
        index = instructions[command](*[jump_value, index])

    if index >= len(instructions_list):
        break

print(registers['a'])
print(registers['b'])

