aunt_sue_dict ={}
MFCSAM_Key = {'children': 3,
              'cats': 7,
              'samoyeds': 2,
              'pomeranians': 3,
              'akitas': 0,
              'vizslas': 0,
              'goldfish': 5,
              'trees': 3,
              'cars': 2,
              'perfumes': 1}

with open('Project16_2015') as file:
    for line in file:
        if "\n" in line:
            end_line = -1
        else:
            end_line = None
        name = line[:line.find(':')]
        attribute1 = line[line.find(':')+2:line.find(':', line.find(':')+1)]
        attribute1_value = int(line[line.find(':', line.find(':')+1)+2: line.find(',')])
        attribute2 = line[line.find(',')+2:line.find(':', line.find(','))]
        attribute2_value = int(line[line.find(':', line.find(','))+2: line.rfind(',')])
        attribute3 = line[line.rfind(',')+2:line.rfind(':')]
        attribute3_value = int(line[line.rfind(':')+1: end_line])
        aunt_sue_dict[name] = {attribute1: attribute1_value,
                               attribute2: attribute2_value,
                               attribute3: attribute3_value,
                               }


def dict_remover(dict_var):
    for sues in dict_var:
        break_status = False
        for keys in MFCSAM_Key:
            if keys in dict_var[sues]:
                if keys == 'cats' or keys == 'trees':
                    if MFCSAM_Key[keys] >= dict_var[sues][keys]:
                        dict_var.pop(sues, None)
                        break_status = True
                        break
                elif keys == 'goldfish' or keys == 'pomeranians':
                    if MFCSAM_Key[keys] <= dict_var[sues][keys]:
                        dict_var.pop(sues, None)
                        break_status = True
                        break
                else:
                    if MFCSAM_Key[keys] != dict_var[sues][keys]:
                        dict_var.pop(sues, None)
                        break_status = True
                        break
        if break_status:
            dict_remover(dict_var)
            break
    return dict_var


print(dict_remover(aunt_sue_dict))
