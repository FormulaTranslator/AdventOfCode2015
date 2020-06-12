# example_list = [20, 15, 10, 5, 5]
# containers_list = example_list
containers_list = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
total_volume = 150

containers_list.sort(reverse=True)


def rerun_list(list_var, index, limit_var, start_position=0):
    permutations = []
    permutation = [list_var[index]]
    list_sum = list_var[index]
    # list_var.remove(list_sum)
    next_position = None
    for k in range(start_position, len(list_var)):
        if index == k:
            pass
        elif list_sum + list_var[k] <= limit_var:
            if next_position is None:
                next_position = k + 1
            list_sum += list_var[k]
            permutation.append(list_var[k])
    if sum(permutation) == limit_var:
        permutation.sort(reverse=True)
        permutations.append(permutation)
    if next_position is not None and next_position != len(list_var):
        permutations.extend(rerun_list(list_var, index, limit_var, next_position))
    return permutations


containers_dict = {}
for indx in containers_list:
    containers_dict[indx] = containers_list.count(indx)

permutations_list = []
for i in range(0, len(containers_list)):
    permutations_list.extend(rerun_list(containers_list, i, total_volume))

permutations_list.sort(key=lambda y: (y[0], y[1], y[2]), reverse=True)

for lists in permutations_list:
    max_counts = 1
    for item in lists:
        max_item = containers_dict[item] - lists.count(item) + 1
        max_counts *= containers_dict[item]
    counts = permutations_list.count(lists)
    while permutations_list.count(lists) > max_counts:
        permutations_list.remove(lists)
        counts = permutations_list.count(lists)

print(permutations_list)
print(len(permutations_list))
