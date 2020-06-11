import hashlib

project_input = 'yzbqklnj'
number_to_add = 0
match_found = False

while not match_found:
    secret_code = project_input + str(number_to_add)
    hash_result = hashlib.md5(secret_code.encode())
    hex_result = hash_result.hexdigest()
    for index, char in enumerate(hex_result):
        if char != '0' and index == 0:
            break
        elif char != '0' and index == 1:
            break
        elif char != '0' and index == 2:
            break
        elif char != '0' and index == 3:
            break
        elif char != '0' and index == 4:
            break
        elif char != '0' and index == 5:
            break
        elif index == 5:
            print(number_to_add)
            print(hex_result)
            match_found = True

    number_to_add += 1
