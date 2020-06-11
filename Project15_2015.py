ingredients_dict = {}

with open('Project15_2015') as file:
    for line in file:
        if "\n" in line:
            end_line = -1
        else:
            end_line = None
        name = line[:line.find(':')]
        capacity = int(line[line.find('capacity')+9: line.find(',', line.find('capacity'))])
        durability = int(line[line.find('durability')+11: line.find(',', line.find('durability'))])
        flavor = int(line[line.find('flavor')+7: line.find(',', line.find('flavor'))])
        texture = int(line[line.find('texture')+8: line.find(',', line.find('texture'))])
        calories = int(line[line.find('calories')+9:end_line])
        ingredients_dict[name] = {'capacity': capacity,
                                  'durability': durability,
                                  'flavor': flavor,
                                  'texture': texture,
                                  'calories': calories
                                  }

remaining_teaspoons = 100


def cookie_score(ingredient_dict, measurement_dict):
    score_dict = {}
    for ingredient in measurement_dict:
        score_dict[ingredient] = {}
        for properties in ingredient_dict[ingredient]:
            score_dict[ingredient][properties] = ingredients_dict[ingredient][properties] * measurement_dict[ingredient]
    capacity_score = 0
    durability_score = 0
    flavor_score = 0
    texture_score = 0
    calories_score = 0
    for item in score_dict:
        capacity_score += score_dict[item]['capacity']
        durability_score += score_dict[item]['durability']
        flavor_score += score_dict[item]['flavor']
        texture_score += score_dict[item]['texture']
        calories_score += score_dict[item]['calories']
    if capacity_score < 0 or durability_score < 0 or flavor_score < 0 or texture_score < 0 or calories_score != 500:
        total_score = 0
    else:
        total_score = capacity_score * durability_score * flavor_score * texture_score

    return total_score


def permutations_iter(iter_dict, min_val, max_val, counter=0, sums=0, iter_values_dict={}):
    counter += 1
    max_counter = len(iter_dict)
    max_score = 0
    for index, items in enumerate(iter_dict):
        if index == counter - 1:
            ingredient = items
            break
    if counter < max_counter:
        for perms in range(min_val, max_val):
            iter_values_dict[ingredient] = perms
            sum_value = sums + perms
            score = permutations_iter(iter_dict, min_val, max_val, counter, sum_value, iter_values_dict)
            if score > max_score:
                max_score = score
    else:
        iter_values_dict[ingredient] = max_val - sums
        score = cookie_score(iter_dict, iter_values_dict)
        if score > max_score:
            max_score = score

    return max_score


print(permutations_iter(ingredients_dict, 0, remaining_teaspoons))
