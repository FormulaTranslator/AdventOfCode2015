from hashlib import md5
project_input = 'yzbqklnj'
number_to_add = 0
match_found = False

while True:
    secret_code = project_input + str(number_to_add)
    hash_result = md5(secret_code.encode())
    hex_result = hash_result.hexdigest()
    if hex_result.startswith('00000'):
        print(number_to_add)
        print(hex_result)
        break

    number_to_add += 1


# Mark's scalable alternative way:
from itertools import count


def solve(password, prefix='00000', numbers_to_add=count()):
    for number_to_add in numbers_to_add:
        secret_code = password + str(number_to_add)
        hash_result = md5(secret_code.encode())
        hex_result = hash_result.hexdigest()
        if hex_result.startswith(prefix):
            return number_to_add, hex_result


password_vars = solve('yzbqklnj')
print(*password_vars, sep='\n')

password_vars = solve('yzbqklnj', '000000')
print(*password_vars, sep='\n')

