input_string = '1113222113'
# input_string = '1'
new_string = input_string
for numbers in range(1, 51):
    char_counter = 0
    input_string = new_string
    new_string = ''
    # print(input_string)
    for index, char in enumerate(input_string):
        if len(input_string) > 1 and index != len(input_string)-1:
            next_char = input_string[index+1:index+2]
        else:
            next_char = ''
        char_counter += 1
        if char != next_char or index == len(input_string)-1:
            new_string += str(char_counter) + char
            char_counter = 0

# print(new_string)
print(len(new_string))
