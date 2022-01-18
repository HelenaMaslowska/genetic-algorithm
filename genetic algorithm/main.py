import random
import math

def form(per):
    form = []
    mini = min(per)
    ind = per.index(mini)
    for i in range(ind, len(per)):
        form.append(per[i])
    for i in range(ind):
        form.append(per[i])
    return form


def good(per, permutations):
    pers = []
    for i in permutations.values():
        pers.append(form(i))
    per = form(per)
    if per in pers or per.reverse() in pers:
        return False
    return True


# PERMUTACJA LISTY LICZB OD 0 DO RAN, BEZ POWTÓRZEŃ W PERS
def permutation(ran, pers):
    while True:
        per = random.sample(range(ran), ran)
        if good(per, pers):
            return per


# FUNKCJA PRZYSTOSOWANIA
def fitness(genes, matrix):
    fit = 0
    for i in range(len(genes)):
        if i == len(genes) - 1:
            fit += matrix[genes[i]][genes[0]]
            break
        fit += matrix[genes[i]][genes[i + 1]]
    return 1000000/fit

"""
def fitness(genes, matrix):
    fit = 0
    for i in range(len(genes)-1):
        fit += matrix[genes[i]][genes[i + 1]]
    fit += matrix[genes[-1]][genes[0]]
    return 1000000/fit
"""

# TURNIEJ
def tournament(cities_counter, genes, n, leng):
    # wersja 1 algorytmu
    winners = []
    while len(winners) < n:
        tmp = []
        indices = random.sample(range(cities_counter), leng)
        for i in indices:
            tmp.append(genes[i])
        maxi = max(tmp)
        if maxi not in winners:
            winners.append(maxi)
    return winners

def tournament2(genes, genes_path): # zwraca ścieżkę o największej wartości [index, funkcja przystosowania, ścieżka]
    #wersja 2 algorytmu
    winners = []
    cp_genes = genes
    cp_genes_path = genes_path
    while len(winners) < 2:
        tab_values = list(cp_genes.values())

        max_value = max(tab_values)
        max_key = list(cp_genes.keys())[tab_values.index(max_value)]
        max_path = list(cp_genes_path.values())[tab_values.index(max_value)]

        max_gene = [max_key, max_value, max_path]
        winners.append(max_gene)
        cp_genes.pop(max_key)
        cp_genes_path.pop(max_key)
        # print(cp_genes, "hm")
    return winners


def add_to_map_list(chosen_pair, map_lists):
    for verse in range(len(map_lists)):
        print("sprawdzam ", map_lists[verse], chosen_pair)
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
    print()
    print("map list", map_lists, "\n")
    return map_lists

def connect_sublists(sub1, sub2):           # sprawdzić czy działa
    for i in (1, sub2):
        sub1.append(sub2[i])
    return sub1

def merge_map_sublists(map_lists):          #do poprawy
    array = 0
    for verse in range(len(map_lists)-1):
        for verse2 in range(verse+1, len(map_lists)-1):
            if map_lists[verse][-1] == map_lists[verse2][0]:
                array = connect_sublists(map_lists[verse], map_lists[verse2])
            elif map_lists[verse][0] == map_lists[verse2][-1]:
                array = connect_sublists(map_lists[verse2], map_lists[verse])
            map_lists.pop(verse)
            map_lists.pop(verse2-1)
            map_lists.append(array)
    return map_lists


def PMX_algoritm(genes):
    path1 = genes[0][2]
    path2 = genes[1][2]
    pos_start = min(random.randint(0, len(path1)-1), random.randint(0, len(path1)-1))
    pos_end = max(random.randint(0, len(path2) - 1), random.randint(0, len(path2) - 1))
    if pos_start > pos_end:
        pos_start, pos_end = pos_end, pos_start
    start_pairs = []

    for i in range(pos_start, pos_end+1):
        path1[i], path2[i] = path2[i], path1[i]
        if path1[i] != path2[i]:
            start_pairs.append([path1[i], path2[i]])

    print("after \n", path1, "\n", path2, pos_start, pos_end)
    print("start_pairs", start_pairs)
    if len(start_pairs) > 0:
        map_lists = [start_pairs.pop()]
        while len(start_pairs) > 0:
            chosen_pair = start_pairs.pop()
            map_lists = add_to_map_list(chosen_pair, map_lists)
        map_lists = merge_map_sublists(map_lists)
    print("map list", map_lists)


### --------------------------------------- dane wejściowe do zadania --------------------------------------- ####


# generowanie punktów na płaszczyźnie kartezjańskiej
cities_count = 6                        # liczba miast
mini = 100                              # odległość minimalna
maxi = 100 * cities_count               # odległość maksymalna
cities = []
x_y_city = []
while len(x_y_city) < cities_count:
    # dodanie nowego miasta do listy jeśli jeszcze takiego nie ma
    x = random.randint(mini, maxi)
    y = random.randint(mini, maxi)
    if [x, y] not in x_y_city:
        x_y_city.append([x, y])
    print("cities dimensions: ", [x, y])


# TWORZENIE MACIERZY odległości miast
cities_count = 6
maxi = cities_count * 100
matrix = [[0 for _ in range(cities_count)] for _ in range(cities_count)]

for i in range(cities_count):
    for j in range(cities_count):
        if j > i:
            # oblicza odległość miasta na podstawie x_y miast
            x_dimension = x_y_city[i][0] - x_y_city[j][0]
            y_dimension = x_y_city[i][1] - x_y_city[j][1]
            matrix[i][j] = round( math.sqrt(pow(x_dimension, 2) + pow(y_dimension, 2)) )
    print(matrix[i])

# TWORZENIE POCZĄTKOWEJ POPULACJI
n = 8
warriors = {}           # wygeneruje się tutaj 8 genomów do walki
warriors_distances = {} # obliczone długości
for i in range(n):
    warriors[i] = permutation(cities_count, warriors)       # generuje geny, z których wybierze się najkrótszą
    warriors_distances[i] = fitness(warriors[i], matrix)    #generuje odległości na podstawie genów
print("\n", warriors)
print("distances: ", warriors_distances)

# TURNIEJ chyba szuka najmniejszego
print(tournament(cities_count, warriors, 2, 3))

# TURNIEJ 2 szuka 2 najkrótszych
winners = tournament2(warriors_distances, warriors)
print("genes", winners)
PMX_algoritm(winners)





