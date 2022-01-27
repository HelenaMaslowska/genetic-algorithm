import random
import math
import PMX_algorithm
import tournaments
import brute_force
import greedy
import mutations
import time
import plot


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
def distance(genes, matrix):
    fit = 0
    for i in range(len(genes) - 1):
        fit += matrix[genes[i]][genes[i + 1]]
    fit += matrix[genes[-1]][genes[0]]
    return fit

def fitness(genes, matrix):
    fit = distance(genes, matrix)
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
                new_matrix[j][i] = new_matrix[i][j] = round(math.sqrt(pow(x_dimension, 2) + pow(y_dimension, 2)))
    return new_matrix

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# STARTER PACK
effectiveness = 0.8
cities_count = 100
population_count = 10
matrix = create_matrix(cities_count)
population = permutation(population_count, cities_count)
population_fitness = [fitness(population[i], matrix) for i in range(population_count)]             # distances of genotypes
old_max = 0
new_max = 0
winners = tournaments.tournament2(population_fitness, population)
#best_genes = brute_force.brute_force(matrix)
#best_fitness = fitness(best_genes, matrix)
best_genes = greedy.greedy_alg(matrix)
best_fitness = fitness(best_genes, matrix)
iterations = []

# ----------- testowanie brute force i greedy ---------------
'''for i in range(100):
    matrix = create_matrix(cities_count)
    best_genes = brute_force.brute_force(matrix)
    best_fitness = fitness(best_genes, matrix)
    good_genes = greedy.greedy_alg(matrix)
    good_fitness = fitness(good_genes, matrix)
    if good_fitness > best_fitness:
        print("-----------------BŁĄD!------------------")
        print("best: ", best_genes, best_fitness)
        print("good: ", good_genes, good_fitness)
print("best: ", best_genes, best_fitness)
print("good: ", good_genes, good_fitness)'''
# --------------------------------------------------

#for _ in range(40):
timer_start = time.time()
while new_max < effectiveness * best_fitness:

    winners = tournaments.tournament3(population_fitness, population)
    #podaje tych samych winnersow po czasie

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
        print(new_max, chosen_gen)
        iterations.append(distance(chosen_gen, matrix))

timer_end = time.time()

plot.plot(iterations)
print("==============================================")
print("with ", round(old_max/best_fitness*100, 2), "% effectiveness", sep="")
print("best fitness:", old_max)
print("best route:", chosen_gen)
print("time:", timer_end - timer_start)
print("==============================================")
