import random
"""
def add_to_map_list(chosen_pair, map_lists):
    for verse in range(len(map_lists)):
        if [chosen_pair[1], chosen_pair[0]] == map_lists[verse]:
            map_lists.pop(verse)
            break
        if (chosen_pair[0] in map_lists[verse]) and (chosen_pair[1] in map_lists[verse]):
            break
        if (chosen_pair[1] in map_lists[verse]) and (chosen_pair[0] in map_lists[verse]):
            break
        if (chosen_pair[0] in map_lists[verse]) and (chosen_pair[1] not in map_lists[verse]):
            map_lists[verse].append(chosen_pair[1])
            break
        if chosen_pair[1] in map_lists[verse] and (chosen_pair[0] not in map_lists[verse]):
            map_lists[verse].insert(0, chosen_pair[0])
            break
    else:
        map_lists.append(chosen_pair)
    return map_lists

def connect_sublists(sub1, sub2):
        return sub1 + sub2[1:]

def merge_map_sublists(map_lists):
    len_map_list = len(map_lists)   # length od map list will change thats why we use while loop
    verse = 0
    while verse < len_map_list-1:
        verse2 = verse+1
        while (verse != verse2) and (verse2 < len_map_list):
            if map_lists[verse][-1] == map_lists[verse2][0]:
                array = connect_sublists(map_lists[verse], map_lists[verse2])
                map_lists.pop(verse)
                map_lists.pop(verse2 - 1)
                map_lists.append(array)
                verse2 -= 1
                len_map_list -= 1
            elif map_lists[verse][0] == map_lists[verse2][-1]:
                array = connect_sublists(map_lists[verse2], map_lists[verse])
                map_lists.pop(verse)
                map_lists.pop(verse2 - 1)
                map_lists.append(array)     #you cant print map_list[verse] because in position verse there is another thing
                verse2 -= 1
                len_map_list -= 1
            verse2 += 1
        verse += 1
    return map_lists

def search_in_list(tab, elem):
    for i in range(len(tab)):
        if elem == tab[i]:
            return i
    return -1

def fix_numbers_in_two_genotypes(gen1, gen2, map_list, start, end):
    #fix all numbers that are repetitive in genotypes
    for verse in map_list:
        gen1_before_start = search_in_list(gen1[:start], verse[0])
        gen1_after_end = search_in_list(gen1[end + 1:], verse[0])

        gen2_before_start = search_in_list(gen2[:start], verse[-1])
        gen2_after_end = search_in_list(gen2[end + 1:], verse[-1])

        if gen1_before_start != -1:
            gen1[gen1_before_start] = verse[-1]

        if gen1_after_end != -1:
            update_this_element = search_in_list(gen1[end + 1:], verse[0]) + end + 1
            gen1[update_this_element] = verse[-1]

        if gen2_before_start != -1:
            gen2[gen2_before_start] = verse[0]

        if gen2_after_end != -1:
            update_this_element = search_in_list(gen2[end + 1:], verse[-1]) + end + 1
            gen2[update_this_element] = verse[0]
    return [gen1, gen2]
"""
def PMX_algoritm_resolver(genotypes):
    """
    PMX - cut fragment of one list and swap with another list, then fill mistakes
    :param genotypes: 2 sublists of routes
    :return: upgraded these 2 sublists
    """
    genotype1 = genotypes[0][2]
    genotype2 = genotypes[1][2]

    # choose position to swap
    pos_start = random.randint(1, len(genotype1) - 2)
    pos_end = random.randint(1, len(genotype2) - 1)
    while pos_end == pos_start:
        pos_end = random.randint(1, len(genotype2) - 1)
    if pos_start > pos_end:
        pos_start, pos_end = pos_end, pos_start

    #swap genotypes
    start_pairs = []
    new_genotype1 = genotype1[:pos_start] + genotype2[pos_start:pos_end] + genotype1[pos_end:]
    new_genotype2 = genotype2[:pos_start] + genotype1[pos_start:pos_end] + genotype2[pos_end:]
    """
    # create map list
    #print(pos_start, pos_end, "\nafter swap\n", genotype1, "\n", genotype2)
    map_lists = [[]]
    if len(start_pairs) > 0:
        # add first pair to map list if there is any pair to add
        map_lists = [start_pairs.pop()]
        # add pairs to map list with special logic
        while len(start_pairs) > 0:
            map_lists = add_to_map_list(start_pairs.pop(), map_lists)
        map_lists = merge_map_sublists(map_lists)
        #print("map list\n", map_lists)

        #fix repetitive numbers to non repetitive
        genotype1, genotype2 = (fix_numbers_in_two_genotypes(genotype1, genotype2, map_lists, pos_start, pos_end))
        #print("after fix repetitive numbers\n", genotype1, "\n", genotype2)
    """
    for x in range(len(genotype1)):

        if x in range(pos_start, pos_end):
            continue

        while new_genotype1[x] in new_genotype1[pos_start:pos_end]:
            new_genotype1[x] = new_genotype2[new_genotype1.index(new_genotype1[x], pos_start, pos_end)]

        while new_genotype2[x] in new_genotype2[pos_start:pos_end]:
            new_genotype2[x] = new_genotype1[new_genotype2.index(new_genotype2[x], pos_start, pos_end)]

    return [new_genotype1, new_genotype2]
