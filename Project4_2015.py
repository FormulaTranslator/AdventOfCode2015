import hashlib

project_input = 'yzbqklnj'
number_to_add = 0
match_found = False

while not match_found:
    secret_code = project_input + str(number_to_add)
    hash_result = hashlib.md5(secret_code.encode())
    hex_result = hash_result.hexdigest()
    if hex_result.startswith('000000'):
        print(number_to_add)
        print(hex_result)
        match_found = True

    number_to_add += 1
