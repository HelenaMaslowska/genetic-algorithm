import random
import math
import PMX_algorithm
import tournaments
from itertools import permutations
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
    for i in range(len(genes)-1):
        fit += matrix[genes[i]][genes[i + 1]]
    fit += matrix[genes[-1]][genes[0]]
    return 10000000/fit

#CREATE CITIES
def generate_x_y_city(cities_count, mini, maxi):
    x_y_city = []
    while len(x_y_city) < cities_count:
        x = random.randint(mini, maxi)
        y = random.randint(mini, maxi)
        if [x, y] not in x_y_city:
            x_y_city.append([x, y])
    return x_y_city

#GET DISTANCES FROM CITY TO CITY
def get_distances(matrix):
    for i in range(cities_count):
        for j in range(cities_count):
            if j > i:
                x_dimension = x_y_city[i][0] - x_y_city[j][0]
                y_dimension = x_y_city[i][1] - x_y_city[j][1]
                matrix[i][j] = round(math.sqrt(pow(x_dimension, 2) + pow(y_dimension, 2)))
    return matrix



### --------------------------------------- dane wejściowe do zadania --------------------------------------- ####


# GENERATE POINTS ON THE CARTESIAN PLANE
cities_count = 2000                      # how many cities
mini = 100
maxi = 100 * cities_count
x_y_city = generate_x_y_city(cities_count, mini, maxi)

# CREATE DISTANCES MATRIX
matrix = get_distances([[0 for _ in range(cities_count)] for _ in range(cities_count)])

# CREATE NEW POPULATION - PATHS OF ALL THE CITIES
n = 8

warriors_distances = []     # distances of genotypes    #-----PRZEROBIC SLOWNIK NA LISTE W CALYM PROGRAMIE

#-----PRZEROBIC SLOWNIK NA LISTE W CALYM PROGRAMIE
warriors = [random.sample(range(cities_count), cities_count) for i in range(n)] # genotypes

for i in range(n):
    warriors_distances.append(fitness(warriors[i], matrix))

# TURNIEJ chyba szuka najmniejszego
#print(tournaments.tournament(cities_count, warriors, 2, 3))
winners = tournaments.tournament2(warriors_distances, warriors)
print(winners[0][1])
print(winners[1][1])
# TOURNAMENT 2 SEARCH THE SHORTEST PATHS
old_max = 0
for _ in range(1000):
    winners = tournaments.tournament2(warriors_distances, warriors)
    genotype1, genotype2 = PMX_algorithm.PMX_algoritm_resolver(winners)
    fitness1 = fitness(genotype1, matrix)
    fitness2 = fitness(genotype2, matrix)
    #print("po")
    if fitness1 > fitness2:
        #print(fitness1)
        warriors.append(genotype1)
    else:
        #print(fitness2)
        warriors.append(genotype2)
    warriors_distances.append(fitness(warriors[n], matrix))
    n += 1

    if old_max < max(warriors_distances):
        old_max = max(warriors_distances)
        print("gotcha", old_max)

