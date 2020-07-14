# Original solution (part1 was deleted to make room for part 2)
with open('Project5_2015') as file:
    nice_counter = 0
    for line in file:
        match_found1 = False
        match_found2 = False
        for index, char in enumerate(line):
            if index == len(line) - 2:
                break
            if char == line[index+2]:
                match_found1 = True
            var = char + line[index+1]
            if line.count(var) > 1:
                match_found2 = True
        if match_found1 and match_found2:
            nice_counter += 1

print(nice_counter)

# Help from Mark's input:
import re

# Part 1
repeated_letter = re.compile(r'(.)*\1')
vowels = lambda input_string: sum([*map(input_string.lower().count, "aeiou")]) >= 3
naughty_strings = lambda input_string: sum([*map(input_string.lower().count, ['ab', 'cd', 'pq', 'xy'])]) == 0


def first_nice_tester(input_string):
    return repeated_letter.search(input_string) and vowels(input_string) and naughty_strings(input_string)


# Part 2
repeated_letter_pair = re.compile(r'(..).*\1')
split_repeated_letter = re.compile(r'(.).\1')


def second_nice_tester(input_string):
    return repeated_letter_pair.search(input_string) and split_repeated_letter.search(input_string)


with open('Project5_2015') as file:
    nice_counter1 = sum(1 for line in file if first_nice_tester(line))
    file.seek(0, 0)
    nice_counter2 = sum(1 for line in file if second_nice_tester(line))

print('Part 1 answer is: {} nice strings'.format(nice_counter1))
print('Part 2 answer is: {} nice strings'.format(nice_counter2))
