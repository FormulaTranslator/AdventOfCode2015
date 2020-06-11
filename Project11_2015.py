
letter_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']


def next_password(old_password):
    new_password = list(old_password)
    char_index = len(new_password)-1
    if letter_array.index(new_password[char_index]) < 25:
        new_password[char_index] = letter_array[letter_array.index(new_password[char_index]) + 1]
    else:
        new_password[char_index] = letter_array[0]
        char_index -= 1
        while new_password[char_index] == 'z':
            if letter_array.index(new_password[char_index]) < 25:
                new_password[char_index] = letter_array[letter_array.index(new_password[char_index]) + 1]
            else:
                new_password[char_index] = letter_array[0]
            char_index -= 1
        new_password[char_index] = letter_array[letter_array.index(new_password[char_index]) + 1]

    new_password = ''.join(new_password)
    return new_password


input_string = 'hepxxyzz'
password = next_password(input_string)
match_found = False

while not match_found:
    numeric_password = [None]
    for char in password:
        numeric_password.append(letter_array.index(char))
    numeric_password.remove(None)
    sequence_check_array = [None]
    for number in range(0, len(numeric_password)-1):
        sequence_check_array.append(numeric_password[number + 1] - numeric_password[number])
    sequence_check_array.remove(None)
    if 'i' in password or 'l' in password or 'o' in password:
        pass
    elif sequence_check_array.count(1) < 2:
        pass
    elif sequence_check_array.count(0) < 2:
        pass
    else:
        sequence1 = False
        sequence2 = False
        sequence_length = len(sequence_check_array) - 1
        for number in range(0, sequence_length):
            if sequence_check_array[number] == 1 and sequence_check_array[number + 1] == 1:
                sequence1 = True
            if sequence_check_array[number] == 0 and sequence_check_array[number + 1] == 0:
                sequence2 = False
                break
            else:
                sequence2 = True
        if sequence1 and sequence2:
            match_found = True
    if not match_found:
        password = next_password(password)

print(password)
