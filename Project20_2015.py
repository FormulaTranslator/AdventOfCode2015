# This script finds all houses that get the exact amount of presents (not what the problem asks)
# This script does not work on small numbers (less than 72 [which is 30 when regressed]
from math import log

End_value = 33100000/10  # 6400/10
prime_numbers = []
with open('Project20_2015') as file:
    for line in file:
        prime_numbers.append(int(line.rstrip('\n')))


def prime_sum(power_dict):
    """ Based on the formula (P^(k+1)-1)/(P-1)"""
    result = 1
    for prime, power in power_dict.items():
        result *= (prime**(power+1)-1)/(prime-1)
    return int(result)


def get_prime_factors(number):
    """ Reduces a number to prime numbers and counts each"""
    result = number
    powers_dict = {}
    while result not in prime_numbers:
        for prime_number in prime_numbers:
            if result % prime_number == 0:
                result //= prime_number
                if prime_number in powers_dict:
                    powers_dict[prime_number] += 1
                else:
                    powers_dict[prime_number] = 1
                break
        if prime_number == prime_numbers[-1]:
            break
    if result in powers_dict:
        powers_dict[result] += 1
    else:
        powers_dict[result] = 1
    return powers_dict


def get_value(prime_factors):
    """Returns the original number given the prime factors dictionary"""
    result = 1
    for prime, power in prime_factors.items():
        result *= prime**power
    return int(result)


def prime_regression(result):
    """ Returns the power number and the prime number.
    This was derived from (P^(k+1)-1)/(P-1) = result by
    solving for k. P is sequentially guessed"""
    return_list = None
    for prime in prime_numbers:
        intermediate1 = result * (prime-1) + 1
        regression = log(intermediate1) / log(prime) - 1
        if regression % 1 < 10**-10:
            if return_list is None:
                return_list = [[prime, int(regression)]]
            else:
                return_list.append([prime, int(regression)])
        elif prime > result:
            return return_list
    return return_list


def get_factors(number):
    """returns all factors of a given number"""
    start_value = int(number/2)
    divisors_set = set()
    for i in range(2, start_value+1):
        if number % i == 0:
            divisors_set.add(i)
            divisors_set.add(int(number/i))
    return divisors_set


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


all_factors = get_factors(End_value)
valid_factors = []
for factors in all_factors:
    if prime_regression(factors) is not None:
        valid_factors.append(factors)


perms_list = []
number_perms = 2**len(valid_factors)
bit_value = [0]*len(valid_factors)
for i in range(1, number_perms):
    bit_value = next_bit(bit_value)
    multiply_list = [a*b for a, b in zip(bit_value, valid_factors)]
    new_list = multiply_list.copy()
    for zeros in range(0, new_list.count(0)):
        new_list.remove(0)
    product = 1
    for value in new_list:
        product *= int(value)
    if product == End_value:
        perms_list.append(new_list)

answer_list = []
for numbers_list in perms_list:
    prime_factors_dict = {}
    for numbers in numbers_list:
        prime_factors_dict[numbers] = prime_regression(numbers)

    # This loop finds all permutations of the possible prime regressions
    # I.E. if a number (403) has factors 13 and 31, 13's prime regression is [3, 2] and 31's prime regression
    # is [2, 4] and [5,2]. Thus, there is 3 permutations ([3, 2], [2, 4]) and ([3, 2], [5,2])
    final_perms_list = [{}]
    for factor, prime_regressions in prime_factors_dict.items():
        if len(prime_regressions) == 1:
            for regression in prime_regressions:
                for i in range(len(final_perms_list)):
                    final_perms_list[i].update({prime_regressions[0][0]: prime_regressions[0][1]})
        elif len(prime_regressions) > 1:
            temp_perm_list = final_perms_list
            for index in range(len(prime_regressions)):
                for i in range(len(temp_perm_list)):
                    if index != len(prime_regressions)-1:
                        final_perms_list.insert(i, temp_perm_list[i+index].copy())
            for index, regression in enumerate(prime_regressions):
                for i in range(index, len(final_perms_list), len(prime_regressions)):
                    final_perms_list[i].update({regression[0]: regression[1]})

    # This loop goes through all permutations and keeps the ones that match the End_value
    for permutations in final_perms_list:
        permutation_check = prime_sum(permutations)
        if permutation_check == End_value:
            end_value = get_value(permutations)
            answer_list.append(end_value)

print(answer_list)
print('\n')
print(min(answer_list))
