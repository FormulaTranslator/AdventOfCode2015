# Puzzle Input
# Hit Points: 100
# Damage: 8
# Armor: 2

weapons = {}
armor = {'None': [0, 0, 0]}
rings = {'None': [0, 0, 0]}

with open("Project21_2015") as file:
    for line in file:
        parts = line.split()
        if 'Weapons' in parts[0]:
            weapon = True
            armr = False
            ring = False
        if 'Armor' in parts[0]:
            weapon = False
            armr = True
            ring = False
        if 'Rings' in parts[0]:
            weapon = False
            armr = False
            ring = True
        if weapon and 'Weapons' not in line:
            weapons[parts[0]] = [int(parts[1]), int(parts[2]), int(parts[3])]
        if armr and 'Armor' not in line:
            armor[parts[0]] = [int(parts[1]), int(parts[2]), int(parts[3])]
        if ring and 'Rings' not in line:
            rings[parts[0]+parts[1]] = [int(parts[2]), int(parts[3]), int(parts[4])]


def game_match(player1, opponent):
    match_round = 1
    while True:
        if match_round % 2 == 1:
            attack = max(player1[damage_i] - opponent[armor_i], 1)
            opponent[hp_i] -= attack
        else:
            attack = max(opponent[damage_i] - player1[armor_i], 1)
            player1[hp_i] -= attack
        if player1[hp_i] <= 0:
            return False
        if opponent[hp_i] <= 0:
            return True
        match_round += 1


cost_i = 0
hp_i = 0
damage_i = 1
armor_i = 2

boss = [100, 8, 2]
ready_player_1 = [100, 0, 0]

minimum_gold_spent = None
most_gold_spent = 0
for i in weapons.keys():
    for j in armor.keys():
        for k in rings.keys():
            for l in rings.keys():

                if k == l:
                    ring_gold = rings[k][cost_i]
                    ring_damage = rings[k][damage_i]
                    ring_armor = rings[k][armor_i]
                else:
                    ring_gold = rings[k][cost_i] + rings[l][cost_i]
                    ring_damage = rings[k][damage_i] + rings[l][damage_i]
                    ring_armor = rings[k][armor_i] + rings[l][armor_i]

                spent_gold = weapons[i][cost_i] + armor[j][cost_i] + ring_gold
                ready_player_1[damage_i] = weapons[i][damage_i] + armor[j][damage_i] + ring_damage
                ready_player_1[armor_i] = weapons[i][armor_i] + armor[j][armor_i] + ring_armor
                player_wins = game_match(ready_player_1.copy(), boss.copy())

                if minimum_gold_spent is None and player_wins:
                    minimum_gold_spent = spent_gold
                elif minimum_gold_spent:
                    if minimum_gold_spent > spent_gold and player_wins:
                        minimum_gold_spent = spent_gold
                if not player_wins and most_gold_spent < spent_gold:
                    most_gold_spent = spent_gold

print(minimum_gold_spent)
print(most_gold_spent)
