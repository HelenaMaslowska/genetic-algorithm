import random
import math
import PMX_algorithm
import tournaments
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
    #print("cities dimensions: ", [x, y])


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
    #print(matrix[i])

# TWORZENIE POCZĄTKOWEJ POPULACJI
n = 8
warriors = {}           # wygeneruje się tutaj 8 genomów do walki
warriors_distances = {} # obliczone długości
for i in range(n):
    warriors[i] = permutation(cities_count, warriors)       # generuje geny, z których wybierze się najkrótszą
    warriors_distances[i] = fitness(warriors[i], matrix)    #generuje odległości na podstawie genów

# TURNIEJ chyba szuka najmniejszego
#print(tournaments.tournament(cities_count, warriors, 2, 3))

# TURNIEJ 2 szuka 2 najkrótszych
winners = tournaments.tournament2(warriors_distances, warriors)
print("genes", winners)
print("map_lists:", PMX_algorithm.PMX_algoritm_resolver(winners))
#PMX_algoritm([[4, 26.9, [0, 4, 3, 2, 5, 1]], [1, 7.54, [2, 3, 5, 1, 0, 4]]])
#connect_sublists([[2,4]], [[3,9,6,3]])




