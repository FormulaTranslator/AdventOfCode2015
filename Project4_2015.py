from hashlib import md5
project_input = 'yzbqklnj'
number_to_add = 0

while True:
    secret_code = project_input + str(number_to_add)
    hash_result = md5(secret_code.encode())
    hex_result = hash_result.hexdigest()
    if hex_result.startswith('00000'):
        print(number_to_add)
        print(hex_result)
        break

    number_to_add += 1


# A scalable alternative way:
from itertools import count


def solve(password, prefixes):
    numbers_to_add = count()
    for prefix in prefixes:
        for number_to_add in numbers_to_add:
            secret_code = password + str(number_to_add)
            hash_result = md5(secret_code.encode())
            hex_result = hash_result.hexdigest()
            if hex_result.startswith(prefix):
                yield number_to_add, hex_result
                break


password_requirements = ['00000', '000000']
password_vars = solve(project_input, password_requirements)
print(*password_vars, sep='\n')

