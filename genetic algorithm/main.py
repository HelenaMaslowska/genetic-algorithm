import matplotlib.pyplot as plt
import random
import math
import PMX_algorithm
import tournaments
import brute_force
import greedy
import mutations
import time
import draw_route

def plot(Y):
    X = [x for x in range(len(Y))]
    plt.plot(X, Y)
    plt.xlabel('Kolejne iteracje')
    plt.ylabel('Długość trasy')
    plt.show()

# PERMUTACJA BEZ POWTÓRZEŃ W WARRIORS
def permutation(population_count, num_of_cities):
    """
    Create list of sublists which have unique permutations
    :param population_count: number of permutations
    :param num_of_cities: number of cities as the name suggests
    :return: these unique permutations
    """
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
    """
    Calculate how long is the whole route
    :param genes: route
    :param matrix: input data distances between all cities
    :return: length of route
    """
    fit = 0
    for i in range(len(genes) - 1):
        fit += matrix[genes[i]][genes[i + 1]]
    fit += matrix[genes[-1]][genes[0]]
    return fit

def fitness(genes, matrix):
    fit = distance(genes, matrix)
    return 10000000/fit

def create_matrix(num_of_cities):
    """
    Creates new matrix[n][n], n - num_of_cities
    :param num_of_cities: number of cities
    :return: list: created matrix, cities coordinates, maximum place where is the city
    """
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

    return new_matrix, x_y_city, maxi

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# STARTER PACK
effectiveness = 0.95
cities_count = 100
population_count = 8
matrix, cities_coordinates, dim = create_matrix(cities_count)
population = permutation(population_count, cities_count)
population_fitness = [fitness(population[i], matrix) for i in range(population_count)]
old_max: float = 0.0
new_max: float = 0.0
winners = tournaments.tournament2(population_fitness, population)
#best_genes = brute_force.brute_force(matrix)
#best_fitness = fitness(best_genes, matrix)
best_genes = greedy.greedy_alg(matrix)
best_fitness = fitness(best_genes, matrix)
iterations = []

chosen_gen = 0
new_chosen = 0
the_lowest_index = 0
print("Loading...")

# --------- tests brute force and greedy ---------
'''for i in range(100):
    matrix = create_matrix(cities_count)
    best_genes = brute_force.brute_force(matrix)
    best_fitness = fitness(best_genes, matrix)
    good_genes = greedy.greedy_alg(matrix)
    good_fitness = fitness(good_genes, matrix)
    if good_fitness > best_fitness:
        print("--------------BŁĄD!---------------")
        print("best: ", best_genes, best_fitness)
        print("good: ", good_genes, good_fitness)
print("best: ", best_genes, best_fitness)
print("good: ", good_genes, good_fitness)'''
# --------------------------------------------------

timer_start = time.time()
temp_start_timer = time.time()
while new_max <= effectiveness * best_fitness:
    winners = tournaments.tournament3(population_fitness, population)

    [genotype1, genotype2] = PMX_algorithm.PMX_algoritm_resolver(winners)
    fitness1 = fitness(genotype1, matrix)
    fitness2 = fitness(genotype2, matrix)

    if fitness1 > fitness2:
        chosen_gen = genotype1
    else:
        chosen_gen = genotype2

    random_choser = random.randint(0, 100)
    #if random_choser <= 0:
    #    chosen_gen = mutations.mutation(chosen_gen)

    if 0 < random_choser <= 7:
        chosen_gen = mutations.mutation_seq(chosen_gen)

    if chosen_gen not in population:
        the_lowest_index = population_fitness.index(min(population_fitness))
        population[the_lowest_index] = chosen_gen
        population_fitness[the_lowest_index] = fitness(population[the_lowest_index], matrix)


    the_lowest_index = population_fitness.index(min(population_fitness))
    new_chosen = mutations.random_mutation(cities_count)
    new_chosen_fitness = fitness(new_chosen, matrix)
    if new_chosen not in population and new_chosen_fitness > population_fitness[the_lowest_index]:
        population[the_lowest_index] = new_chosen
        population_fitness[the_lowest_index] = new_chosen_fitness

    new_max = max(population_fitness)
    if old_max < new_max:
        old_max = new_max
        i = time.time()
        #print(round(old_max/best_fitness*100, 4), "\t",round(i - temp_start_timer, 4), "\t", round(i - timer_start, 4))
        iterations.append(distance(chosen_gen, matrix))
        #temp_start_timer = time.time()

timer_end = time.time()

#plot(iterations)
print("==============================================")
print("with ", round(old_max/best_fitness*100, 2), "% effectiveness", sep="")
print("best fitness:", old_max)
print("route length: ", distance(chosen_gen,matrix))
print("best route:", chosen_gen)
print("time:", timer_end - timer_start)
print("==============================================")

draw_route.draw(cities_coordinates, best_genes, dim, "Best route")
draw_route.draw(cities_coordinates, chosen_gen, dim, "Found route")