from itertools import permutations

people_dict = {'People': 'Relation'}
people_list = []
happiness_dict = {'DoubleName': 0}

# with open('Test_Input', 'r') as file:
with open('Project13_2015', 'r') as file:
    for line in file:
        name1 = line[:line.find(' ')]
        name2 = line[line.rfind(' ')+1:line.find('.')]
        if 'gain' in line:
            units = int(line[line.find('gain ') + 5: line.find(' happiness')])
        else:
            units = -int(line[line.find('lose ') + 5: line.find(' happiness')])
        if name1 in people_dict:
            people_dict[name1][name2] = units
        else:
            people_dict[name1] = {name2: units}
        if name1 not in people_list:
            people_list.append(name1)

for people in people_dict:
    if people != "People":
        for neighbor in people_dict[people]:
            names = people + '-' + neighbor
            inverse_names = neighbor + '-' + people
            if inverse_names not in happiness_dict:
                net_units = people_dict[people][neighbor] + people_dict[neighbor][people]
                happiness_dict[names] = net_units

sorted_happiness_list = sorted(happiness_dict.items(), key=lambda x: x[1], reverse=True)

seating_order = permutations(people_list, len(people_list))
seating_order_list = list(seating_order)
possible_orders = len(seating_order_list)
total_happiness = []
happiness_change = []

for order in seating_order_list:
    table_happiness_list = []
    for name_position in range(0, len(order)):
        if name_position == len(order)-1:
            position_adjustment = -(len(order)-1)
        else:
            position_adjustment = 1
        name_combo = order[name_position] + '-' + order[name_position + position_adjustment]
        inverse_name_combo = order[name_position + position_adjustment] + '-' + order[name_position]
        if name_combo in happiness_dict:
            net_happiness = happiness_dict[name_combo]
        else:
            net_happiness = happiness_dict[inverse_name_combo]
        table_happiness_list.append(net_happiness)
    happiness1 = sum(table_happiness_list)
    if happiness1 == 733:
        test = 'found'
    table_happiness_list.remove(min(table_happiness_list))
    happiness2 = sum(table_happiness_list)
    total_happiness.append(happiness2)
    happiness_change.append(happiness2-happiness1)

max_happiness = max(total_happiness)
max_change = happiness_change[total_happiness.index(max_happiness)]
# print(seating_order)
print(max_change)
# print(total_happiness)
print(max_happiness)
