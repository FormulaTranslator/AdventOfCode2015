from time import time
from itertools import combinations
start = time()
presents = []
with open('Project24_2015') as file:
    for line in file:
        presents.append(int(line.rstrip('\n')))
presents.sort(reverse=True)
group_size = int(sum(presents)/4)  # Part 1 had 3 groups


def quantum_entanglement_calculator(group):
    result = 1
    for present in group:
        result *= present
    return result


def get_minimum_presents(presents_list, current_list=[]):
    presents_list_copy = presents_list.copy()
    for present in presents_list:
        test = sum(current_list) + present
        if sum(current_list) + present < group_size:
            current_list.append(present)
            presents_list_copy.remove(present)
            get_minimum_presents(presents_list_copy, current_list)
        elif sum(current_list) + present == group_size:
            return len(current_list) + 1


smallest_group_size = get_minimum_presents(presents)
possible_groups = list(combinations(presents, smallest_group_size))
balanced_groups = []
for group in possible_groups:
    if sum(group) == group_size:
        balanced_groups.append(group)
smallest_group_entanglement = quantum_entanglement_calculator(presents)
for present_group in balanced_groups:
    current_group_size = len(present_group)
    current_group_entanglement = quantum_entanglement_calculator(present_group)
    if current_group_size == smallest_group_size and current_group_entanglement < smallest_group_entanglement:
        smallest_group_entanglement = current_group_entanglement

print(smallest_group_entanglement)
print(time()-start)
