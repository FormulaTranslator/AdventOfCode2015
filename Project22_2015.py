class Character:
    def __init__(self, name, Hp, damage=0, armor=0, mana=0):
        self.name = name
        self.Hp = Hp
        self.initial_Hp = Hp
        self.damage = damage
        self.initial_damage = damage
        self.armor = armor
        self.initial_armor = armor
        self.mana = mana
        self.initial_mana = mana

    def __str__(self):
        return "{} has the following stats:\nHp = {}\nDamage = {}\nArmor = {}\nMana = {}".format(
            self.name, self.Hp, self.damage, self.armor, self.mana)

    def __repr__(self):
        return self.name

    def adjust_Hp(self, amount):
        self.Hp += amount

    def adjust_damage(self, amount):
        self.damage = amount

    def adjust_armor(self, amount):
        self.armor = amount

    def adjust_mana(self, amount):
        self.mana += amount

    def attack(self, defender):  # Character 1 is the attacking player
        attack_damage = self.damage + defender.armor
        if attack_damage > 0:
            attack_damage = 0
        return attack_damage

    def reset_stats(self):
        self.Hp = self.initial_Hp
        self.damage = self.initial_damage
        self.armor = self.initial_armor
        self.mana = self.initial_mana


class Move:
    def __init__(self, name, Hp, damage, armor, mana, duration, mana_cost, number):
        self.name = name
        self.Hp = Hp
        self.damage = damage
        self.armor = armor
        self.duration = duration
        self.active_duration = 0
        self.mana = mana
        self.mana_cost = mana_cost
        self.cast = False
        self.number = number

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# Initialize characters
ready_player_1 = Character('Parzival', 50, 0, 0, 500)
boss = Character('Anorak', 51, -9)


def current_turn(current_active_moves,  current_turn_moves):
    total_attack = 0
    total_armor = 0
    total_mana = 0
    swap_list = []
    for move in current_active_moves:
        if move.active_duration > 0:
            move.active_duration -= 1
            total_attack += move.damage
            total_armor += move.armor
            total_mana += move.mana
        if move.active_duration <= 0:
            swap_list.append(move)
    ready_player_1.adjust_damage(total_attack)
    ready_player_1.adjust_armor(total_armor)
    for i in swap_list:
        current_active_moves.remove(i)
        current_turn_moves.insert(i.number, i)
    return total_mana


def game_match(available_moves, active_moves, mana_spent=0,
               hp=ready_player_1.Hp, mana=ready_player_1.mana, boss_hp=boss.Hp, tracker=[]):
    """This function is recursive. It loops through the possible
    options until the player or the boss dies."""
    global minimum_mana_spent

    # Start Player Turn
    # Evaluate current spells
    hp -= 1  # Part 2 addition
    result_mana = current_turn(active_moves, available_moves)
    mana += result_mana
    boss_hp += ready_player_1.attack(boss)
    active_timers = [x.active_duration for x in active_moves]
    for moves in available_moves:
        # Reset turn variables
        turn_moves = available_moves.copy()
        turn_active_effects = active_moves.copy()
        temp_Hp = hp
        temp_mana = mana
        temp_boss_Hp = boss_hp
        temp_mana_spent = mana_spent
        move_tracker = tracker.copy()
        if move_tracker == [Shield, Recharge, Poison, Drain, Magic_Missile]:
                test = True
        for i, effect in enumerate(turn_active_effects):
            effect.active_duration = active_timers[i]

        if temp_boss_Hp < 1:
            if temp_mana_spent < minimum_mana_spent:
                minimum_mana_spent = temp_mana_spent
        elif temp_Hp > 0:
            # if temp_mana_spent == 0:
            #     test = True
            # cast a spell
            if temp_mana >= -moves.mana_cost:
                temp_mana_spent -= moves.mana_cost
                temp_mana += moves.mana_cost
                if moves.duration == 1:
                    temp_boss_Hp += moves.damage
                    temp_Hp += moves.Hp
                else:
                    turn_active_effects.append(moves)
                    turn_moves.remove(moves)
                    moves.active_duration = moves.duration
                if temp_boss_Hp < 1:
                    if temp_mana_spent < minimum_mana_spent:
                        minimum_mana_spent = temp_mana_spent
                else:
                    # Start Boss's turn
                    result_mana = current_turn(turn_active_effects, turn_moves)
                    temp_mana += result_mana
                    temp_boss_Hp += ready_player_1.attack(boss)
                    if temp_boss_Hp < 1:
                        if temp_mana_spent < minimum_mana_spent:
                            minimum_mana_spent = temp_mana_spent
                    else:
                        temp_Hp += boss.attack(ready_player_1)
                        if temp_Hp > 0 and temp_mana >= Magic_Missile.mana_cost and temp_mana_spent < minimum_mana_spent:
                            # This recursive call starts another round of turns
                            move_tracker.append(moves)
                            game_match(turn_moves,
                                       turn_active_effects,
                                       temp_mana_spent,
                                       temp_Hp, temp_mana,
                                       temp_boss_Hp,
                                       move_tracker)


# Initialize moves
Magic_Missile = Move('Magic Missle', 0, -4, 0, 0, 1, -53, 3)
Drain = Move('Drain', 2, -2, 0, 0, 1, -73, 4)
Shield = Move('Shield', 0, 0, 7, 0, 6, -113, 0)
Poison = Move('Poison', 0, -3, 0, 0, 6, -173, 1)
Recharge = Move('Recharge', 0, 0, 0, 101, 5, -229, 2)

Moves = [
    Shield,
    Poison,
    Recharge,
    Magic_Missile,
    Drain
]

# The minimum_mana_spent is set sufficiently high enough
# to ensure that the correct low value can be found.
minimum_mana_spent = int(-Recharge.mana_cost * ready_player_1.Hp/2)
# Get the minimum amount of mana to win
Active_moves = []
game_match(Moves, Active_moves)

print(minimum_mana_spent)
