import random
import math
import PMX_algorithm
import tournaments
import brute_force


def good(per, pers):
    if per in pers or per.copy().reverse() in pers:
        return False
    return True


# PERMUTACJA LISTY LICZB OD 0 DO RAN, BEZ POWTÓRZEŃ W PERS
def permutation(ran, pers):
    while True:
        per = [0]
        samp = random.sample(range(1, ran), ran - 1)
        for i in samp:
            per.append(i)
        if good(per, pers):
            pers.append(per)
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
cities_count = 6                   # how many cities
mini = 100
maxi = 100 * cities_count
x_y_city = generate_x_y_city(cities_count, mini, maxi)

# CREATE DISTANCES MATRIX
matrix = get_distances([[0 for _ in range(cities_count)] for _ in range(cities_count)])

# ----------- testowanie brute force ---------------
#best_genes = brute_force.brute_force(matrix)
#best_fitness = fitness(best_genes, matrix)
#print("najlepszy genom: ", best_genes, best_fitness)
# --------------------------------------------------

# CREATE NEW POPULATION - PATHS OF ALL THE CITIES
n = 8

warriors_distances = []     # distances of genotypes    #-----PRZEROBIC SLOWNIK NA LISTE W CALYM PROGRAMIE

#-----PRZEROBIC SLOWNIK NA LISTE W CALYM PROGRAMIE
#'''
warriors = []
for _ in range(n):
    permutation(cities_count, warriors)
#'''

#warriors = [random.sample(range(cities_count), cities_count) for i in range(n)] # genotypes
print("warriors: ", warriors)

for i in range(n):
    warriors_distances.append(fitness(warriors[i], matrix))

# TURNIEJ chyba szuka najmniejszego
#print(tournaments.tournament(cities_count, warriors, 2, 3))
winners = tournaments.tournament2(warriors_distances, warriors)
#print(winners[0][1])
#print(winners[1][1])
# TOURNAMENT 2 SEARCH THE SHORTEST PATHS
old_max = 0


new_max = 0
for _ in range(5):
#while new_max < 0.6 * best_fitness:
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
    print(len(warriors), warriors)
    print(len(warriors_distances), warriors_distances)
    n += 1
    new_max = max(warriors_distances)
    if old_max < new_max:
        old_max = new_max
        print("gotcha", old_max)
        print(warriors[warriors_distances.index(old_max)])
