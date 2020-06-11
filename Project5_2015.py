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
