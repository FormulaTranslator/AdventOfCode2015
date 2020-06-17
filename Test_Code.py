from time import time
start = time()
containers_list = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
# containers_list = [20, 10, 15, 5, 5]
total_volume = 150


def next_bit(binary_arr):
    bits = len(binary_arr)
    if binary_arr[bits-1] == 0:
        binary_arr[bits-1] = 1
    else:
        index = bits-1
        while binary_arr[index] == 1:
            binary_arr[index] = 0
            index -= 1
        binary_arr[index] = 1
    return binary_arr


perms_list = []
number_perms = 2**len(containers_list)
bit_value = [0]*len(containers_list)
for i in range(1, number_perms):
    bit_value = next_bit(bit_value)
    multiply_list = [a*b for a, b in zip(bit_value, containers_list)]
    if sum(multiply_list) == total_volume:
        new_list = bit_value.copy()
        for zeros in range(0, new_list.count(0)):
            new_list.remove(0)
        perms_list.append(new_list)

min_size = len(containers_list)
size_count = 0
for items in perms_list:
    length = len(items)
    if length == min_size:
        size_count += 1
    elif length < min_size:
        min_size = length
        size_count = 1


print(len(perms_list))
print(min_size)
print(size_count)
print(time()-start)
