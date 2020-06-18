molecule_replacements = {}
Reverse_Engineer_Set = []

with open('Project19_2015') as file:
    for line in file:
        if '=>' in line:
            line_list = line.split()
            base = line_list[0]
            change = line_list[2]
            change.rstrip("\n")
            if base in molecule_replacements:
                new_list = molecule_replacements[base]
                new_list.append(change)
                molecule_replacements[base] = new_list
            else:
                molecule_replacements[base] = [change]
            Reverse_Engineer_Set.append((change, base))
        elif line != '\n':
            medicine_molecules = line
            molecule_length = len(medicine_molecules)

Reverse_Engineer_Set.sort(key=lambda x: (len(x[1]), x[0]), reverse=False)


def get_indices(current_molecules):
    """Returns every index where certain molecules exist in a string of molecules"""
    molecule_indices = {}
    for index, molecules in enumerate(current_molecules):
        if molecules.isupper() or molecules == 'e':
            if index == len(current_molecules)-1:
                next_char = 0
            else:
                next_char = 1
            if current_molecules[index+next_char].islower():
                molecule = current_molecules[index:index+2]
            else:
                molecule = molecules
            if molecule in molecule_indices:
                new_index = molecule_indices[molecule]
                new_index.append(index)
                molecule_indices[molecule] = new_index
            else:
                molecule_indices[molecule] = [index]
    return molecule_indices


# Find possible molecules after 1 replacement
def possible_replacements(current_molecules, molecule_characterization=True):
    """Returns every unique compound by making 1 change"""
    distinct_molecules = set()
    current_indicies = get_indices(current_molecules)
    for mol, indices in current_indicies.items():
        if mol in molecule_replacements:
            for replacement in molecule_replacements[mol]:
                for i in indices:
                    new_molecule = current_molecules[:i] + replacement + current_molecules[i+len(mol):]
                    if check_uncharacteristic_molecules(new_molecule) or not molecule_characterization:
                        distinct_molecules.add(new_molecule)
    return distinct_molecules


# Molecule Characterization (this is to reduce the number of iterations
Molecule_Characterization = {}
element_count = 0
for index, molecules in enumerate(medicine_molecules):
    if molecules.isupper() or molecules == 'e':
        if index == len(medicine_molecules)-1:
            next_char = 0
        else:
            next_char = 1
        if medicine_molecules[index+next_char].islower():
            molecule = medicine_molecules[index:index+2]
        else:
            molecule = molecules
        if molecule in Molecule_Characterization and molecule not in molecule_replacements:
            Molecule_Characterization[molecule] += 1
        elif molecule not in molecule_replacements:
            Molecule_Characterization[molecule] = 1
        element_count += 1


def check_uncharacteristic_molecules(molecule_string):
    for Molecules in Molecule_Characterization:
        if molecule_string.count(Molecules) > Molecule_Characterization[Molecules]:
            return False
        elif molecule_string.endswith(medicine_molecules[-1]):
            return False
    return True


print(len(possible_replacements(medicine_molecules, False)))
# See reddit explanation of this. I figured out the Rn, Ar, Y on my own, but not their connection
print(element_count-Molecule_Characterization['Rn']-Molecule_Characterization['Ar']-2*Molecule_Characterization['Y']-1)
# Find number of steps to make the molecule
# possible_molecules = {'e'}
# step = 0
# Reverse engineering the molecule seems to have worked for others, but not this code.
# next_molecule_sections = []
# masterloop = 0
# molecule_sections = []
# while True:
#     if molecule_sections:
#         medicine_molecules = "".join(molecule_sections)
#     r_split = medicine_molecules.split("r")
#     molecule_sections = []
#     for split in r_split:
#         if split.endswith('A'):
#             molecule_sections.append(split + 'r')
#         else:
#             molecule_sections[-1] = molecule_sections[-1] + split
#     test = len(molecule_sections)
#     if test < 4:
#         yay = True
#     next_molecule_sections = []
#     if masterloop % 2 == 0:
#         position = 0
#     else:
#         position = -1
#     current_section = molecule_sections[position]
#     for reverse_search, replacement in Reverse_Engineer_Set:
#         if reverse_search in current_section:
#             current_section = current_section.replace(reverse_search, replacement, 1)
#             step += 1
#             molecule_sections[position] = current_section
#             break
#
#     masterloop += 1
#     if masterloop == 1000:
#         break
#
# print(step)
# print(len(next_molecule_sections))
# print(next_molecule_sections)
# This runs out of memory ... too many combinations. It increases exponentially
# while True:
#     next_possible_molecules_set = set()
#     if medicine_molecules in possible_molecules:
#         print(step)
#         break
#     for molecule in possible_molecules:
#         next_molecule_set = possible_replacements(molecule)
#         next_possible_molecules_set |= next_molecule_set
#     possible_molecules = next_possible_molecules_set
#     step += 1
#     print(len(possible_molecules))
