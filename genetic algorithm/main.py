import random
import math
import PMX_algorithm
import tournaments
import brute_force
import mutations
from datetime import datetime
# PERMUTACJA LISTY LICZB OD 1 DO RAN, BEZ POWTÓRZEŃ W WARRIORS
def permutation(population_count, num_of_cities):
    m = 0
    warrior_s = []
    while m < population_count:
        per = [0] + random.sample(range(1, num_of_cities), num_of_cities - 1)
        if not (per in warrior_s):
            warrior_s.append(per)
            m += 1
    return warrior_s

# FUNKCJA PRZYSTOSOWANIA
def fitness(genes, matrix):
    fit = 0
    for i in range(len(genes)-1):
        fit += matrix[genes[i]][genes[i + 1]]
    fit += matrix[genes[-1]][genes[0]]
    return 10000000/fit

def create_matrix(num_of_cities):
    mini = 100
    maxi = 100 * cities_count
    x_y_city = []
    new_matrix = [[0 for _ in range(cities_count)] for _ in range(cities_count)]
    while len(x_y_city) < num_of_cities:
        x = random.randint(mini, maxi)
        y = random.randint(mini, maxi)
        if [x, y] not in x_y_city:
            x_y_city.append([x, y])

    for i in range(cities_count):
        for j in range(cities_count):
            if j > i:
                x_dimension = x_y_city[i][0] - x_y_city[j][0]
                y_dimension = x_y_city[i][1] - x_y_city[j][1]
                new_matrix[i][j] = round(math.sqrt(pow(x_dimension, 2) + pow(y_dimension, 2)))
    return new_matrix

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# STARTER PACK
effectiveness = 0.7
cities_count = 10
population_count = 8
matrix = create_matrix(cities_count)
population = permutation(population_count, cities_count)
population_fitness = [fitness(population[i], matrix) for i in range(population_count)]             # distances of genotypes
old_max = 0
new_max = 0
winners = tournaments.tournament2(population_fitness, population)

# ----------- testowanie brute force ---------------
best_genes = brute_force.brute_force(matrix)
best_fitness = fitness(best_genes, matrix)
print("best: ", best_genes, best_fitness)
# --------------------------------------------------

## Może będziemy generować instancje wokół najpierw stworzonego rozwiązania? Nie trzeba będzie szukać brute forcem,
# ale trochę trudniejsze do napisania.

#for _ in range(40):
timer_start = datetime.now()
while new_max < effectiveness * best_fitness:

    # trzeba będzie za każdą iteracją tworzyć nową populację a nie tylko dodawać kolejnego osobnika
    #tournaments.tournament3(population_fitness, population)

    winners = tournaments.tournament3(population_fitness, population)
    #podaje tych samych winnersow po czasie
    # turniej powinnyśmy powtarzać tyle razy, ile ma wynosić nasza populacja i powinien on za każdym razem losować sobie
    #  część populacji z której potem wybiera najlepszych, czyli rodziców.

    # można zrobić tak, żeby funkcja turnament od razu zwracała nam listę par rodziców o zadanej długości (liczności populacji)
    # i potem przekazujemy to np do funkcji breed() (którą napiszemy), która za pomocą PMX tworzy z tych par nową populację

    # potem dla każdej populacji będziemy szukać najlepszego genomu i porównywać go z warunkiem stopu

    [genotype1, genotype2] = PMX_algorithm.PMX_algoritm_resolver(winners)
    fitness1 = fitness(genotype1, matrix)
    fitness2 = fitness(genotype2, matrix)
    chosen_gen = 0
    if fitness1 > fitness2:
        #print(fitness1)
        chosen_gen = genotype1
    else:
        #print(fitness2)
        chosen_gen = genotype2
    # population_fitness.append(fitness(population[population_count], matrix))

    random_choser = random.randint(0, 100)
    if random_choser <= 3:
        chosen_gen = mutations.mutation(chosen_gen)
    if 3 < random_choser <= 5:
        chosen_gen = mutations.mutation_seq(chosen_gen)
    if 5 < random_choser <= 7:
        chosen_gen = mutations.random_mutation(cities_count)

    if chosen_gen not in population:
        the_lowest_index = population_fitness.index(min(population_fitness))
        population[the_lowest_index] = chosen_gen
        population_fitness[the_lowest_index] = fitness(population[the_lowest_index], matrix)

    #population_count += 1
    new_max = max(population_fitness)
    if old_max < new_max:
        old_max = new_max
        #print("gotcha")
        #print(new_max, chosen_gen)
timer_end = datetime.now()
print("==============================================")
print("with ", round(old_max/best_fitness*100, 2), "% effectiveness", sep="")
print("best fitness:", old_max)
print("best route:", chosen_gen)
print("time:", timer_end.second-timer_start.second)
print("==============================================")