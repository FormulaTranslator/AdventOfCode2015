end_time = 2503
reindeer_stats = {'name': 0}
reindeers = []

with open('Project14_2015') as file:
    for line in file:
        reindeer = line[:line.find(' ')]
        reindeers.append(reindeer)
        speed = int(line[line.find('fly ')+4: line.find(' km')])
        endurance = int(line[line.find('s for ')+6: line.find(' seconds,')])
        rest = int(line[line.find('rest for ')+9: line.find(' seconds.')])
        average_pace = (speed * endurance) / (endurance + rest)
        cycle_time = endurance + rest
        reindeer_stats[reindeer] = {'speed': speed,
                                    'endurance': endurance,
                                    'rest': rest,
                                    'average pace': average_pace,
                                    'cycle time': cycle_time,
                                    'traveled distance': 0
                                    }

race_results = {'Reindeer': 0}
# part 1 of puzzle
# for deer in reindeer_stats:
#     if deer != 'name':
#         total_distance = reindeer_stats[deer]['average pace'] * end_time
#         if total_distance % int(total_distance) == 0:
#             race_results[deer] = total_distance
#         else:
#             extra_time = end_time % reindeer_stats[deer]['cycle time']
#             partial_distance = reindeer_stats[deer]['average pace'] * (end_time - extra_time)
#             if extra_time < reindeer_stats[deer]['endurance']:
#                 makeup_distance = reindeer_stats[deer]['speed'] * extra_time
#             else:
#                 makeup_distance = reindeer_stats[deer]['speed'] * reindeer_stats[deer]['endurance']
#             total_distance = partial_distance + makeup_distance
#             race_results[deer] = total_distance
for reindeer in reindeer_stats:
    race_results[reindeer] = 0


for seconds in range(1, end_time):
    temp_results = []
    for deer in reindeer_stats:
        if deer != 'name':
            cycle_second = seconds % reindeer_stats[deer]['cycle time']
            if cycle_second == 0:
                pass
            elif cycle_second <= reindeer_stats[deer]['endurance']:
                reindeer_stats[deer]['traveled distance'] += reindeer_stats[deer]['speed']
            temp_results.append(reindeer_stats[deer]['traveled distance'])
    winning_distance = max(temp_results)
    for deer in reindeer_stats:
        if deer != 'name':
            if reindeer_stats[deer]['traveled distance'] == winning_distance:
                race_results[deer] += 1

print(race_results)
results_list = []
for deers in race_results:
    results_list.append(race_results[deers])
print(max(results_list))
