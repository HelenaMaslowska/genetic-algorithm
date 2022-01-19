import random

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
        temp = sub2[1:]
        return sub1 + temp

def merge_map_sublists(map_lists):
    len_map_list = len(map_lists)   # length od map list will change thats why we use while loop
    verse = 0
    while verse < len_map_list-1:
        verse2 = verse+1
        while verse2 < len_map_list:
            if map_lists[verse][-1] == map_lists[verse2][0]:
                array = connect_sublists(map_lists[verse], map_lists[verse2])
                map_lists.pop(verse)
                map_lists.pop(verse2 - 1)
                map_lists.append(array)
                verse -= 1
                verse2 -= 1
                len_map_list -= 1
            elif map_lists[verse][0] == map_lists[verse2][-1]:
                array = connect_sublists(map_lists[verse2], map_lists[verse])
                map_lists.pop(verse)
                map_lists.pop(verse2 - 1)
                map_lists.append(array)     #you cant print map_list[verse] because in position verse there is another thing
                verse -= 1
                verse2 -= 1
                len_map_list -= 1
            verse2 += 1
        verse += 1
    return map_lists


def PMX_algoritm_resolver(genes):
    genom1 = genes[0][2]    #first genom
    genom2 = genes[1][2]    #second genom to reform

    pos_start = min(random.randint(0, len(genom1) - 1), random.randint(0, len(genom1) - 1))
    pos_end = max(random.randint(0, len(genom2) - 1), random.randint(0, len(genom2) - 1))
    if pos_start > pos_end:
        pos_start, pos_end = pos_end, pos_start

    start_pairs = []
    for i in range(pos_start, pos_end+1):
        genom1[i], genom2[i] = genom2[i], genom1[i]
        if genom1[i] != genom2[i]:
            start_pairs.append([genom1[i], genom2[i]])

    print("\n", genom1, "\n", genom2, "\n", pos_start, pos_end)
    #print("start_pairs", start_pairs)
    map_lists = [[]]
    if len(start_pairs) > 0:
        map_lists = [start_pairs.pop()]     #add first pair if there is any pair

        while len(start_pairs) > 0:
            map_lists = add_to_map_list(start_pairs.pop(), map_lists)
        map_lists = merge_map_sublists(map_lists)
    return map_lists
