# attempt 1 fail
# example_list = [20, 15, 10, 5, 5]
# containers_list = example_list
# total_volume = 25
# containers_list = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
# total_volume = 150
#
# containers_list.sort(reverse=True)
#
#
# def rerun_list(list_var, index, limit_var, start_position=0):
#     list_length = len(list_var)
#     permutations = []
#     permutation = [list_var[index]]
#     list_sum = list_var[index]
#     next_position = None
#
#     for k in range(0, list_length):
#         circular_variable = k + start_position
#         if circular_variable >= list_length:
#             circular_variable -= list_length
#         if index == circular_variable:
#             pass
#         elif list_sum + list_var[circular_variable] <= limit_var:
#             if next_position is None:
#                 next_position = circular_variable + 1
#             list_sum += list_var[circular_variable]
#             permutation.append(list_var[circular_variable])
#
#     if sum(permutation) == limit_var:
#         permutation.sort(reverse=True)
#         permutations.append(permutation)
#
#     if next_position != list_length and index != list_length - 1 != next_position:
#         permutations.extend(rerun_list(list_var, index, limit_var, next_position))
#
#     return permutations
#
#
# containers_dict = {}
# for indx in containers_list:
#     containers_dict[indx] = containers_list.count(indx)
#
# permutations_list = []
# for i in range(0, len(containers_list)):
#     permutations_list.extend(rerun_list(containers_list, i, total_volume))
#
# for sortlist in range(0, len(permutations_list)):
#     permutations_list[sortlist].sort(reverse=True)
#
# final_list = []
#
# for lists in permutations_list:
#     max_counts = 1
#
#     for item in lists:
#         max_item = containers_dict[item] - lists.count(item) + 1
#         max_counts *= max_item
#     while final_list.count(lists) < max_counts:
#         final_list.append(lists)
#         counts = final_list.count(lists)
#
# print(final_list)
# print(len(final_list))
from numpy import vectorize

containers_list = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]

x = vectorize(int)(containers_list)
c = 0
for i in range(1 << len(x)):
    t = i
    s = 0
    for j in x:
        if t % 2 == 1:
            s += j
        t //= 2
    if s == 150:
        c += 1
print(c)
