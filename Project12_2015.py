import json


def redundant_lists(list_var):
    str_lists = str(list_var)
    number_lists = 0
    for char in str_lists:
        if char == '[':
            number_lists += 1
        else:
            break

    if number_lists == 1:
        new_list = list_var
    elif number_lists == 0:
        return None
    else:
        for items in list_var:
            new_list = redundant_lists(items)
    return new_list


def nest_finder(item, number_var):
    for items in item:
        skip = False
        if isinstance(item, dict):
            next_item = item[items]
            for keys in item:
                if item[keys] == 'red':
                    skip = True
        else:
            str_items = str(items)
            if str_items[:2] == '[[[' and str_items[-2:] == ']]]':
                next_item = redundant_lists(items)
            else:
                next_item = None
        if not skip:
            if isinstance(items, int):
                number_var += items
                # print(number_var)
            elif isinstance(item, dict) and isinstance(next_item, int):
                number_var += next_item
                # print(number_var)

            if isinstance(next_item, dict) or isinstance(next_item, list):
                number_var = nest_finder(next_item, number_var)
            if isinstance(items, dict) or isinstance(items, list):
                number_var = nest_finder(items, number_var)

    return number_var


with open('JSON') as json_file:
    json_dict = json.load(json_file)

total = 0
total = nest_finder(json_dict, total)

print(total)
