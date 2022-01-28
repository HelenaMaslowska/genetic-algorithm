import random

def tournament(num_of_cities, genes, n, leng):
    """
    TOURNAMENT 1
    Started with this method but it's useless for the rest of program
    :param num_of_cities: number of cities
    :param genes: fitness list
    :param n: idk
    :param leng: idk
    :return: max of list
    """
    winners = []
    while len(winners) < n:
        tmp = []
        indices = random.sample(range(num_of_cities), leng)
        for i in indices:
            tmp.append(genes[i])
        maxi = max(tmp)
        if maxi not in winners:
            winners.append(maxi)
    return winners


def tournament2(genes, genes_path):
    """
    TOURNAMENT 2
    Choose the best of two genes - fitnesses
    :param genes: input list of fitness
    :param genes_path: input list of routes
    :return: two vectors in one list
    """
    tab = [random.randint(0, 1) for _ in range(len(genes_path))]
    while not (len(genes_path) // 3 < sum(tab) < len(genes_path) //3 * 2):
        tab = [random.randint(0, 1) for _ in range(len(genes_path))]

    max1 = max2 = -1
    for i in range(len(genes_path)):
        if tab[i] == 1:
            max1 = max(max1, genes[i])
        else:
            max2 = max(max2, genes[i])

    return [ [genes.index(max1), max1, genes_path[genes.index(max1)]],
             [genes.index(max2),max2,genes_path[genes.index(max2)]]  ]


def tournament3(population_fitness, population):
    """
    TOURNAMENT 3
    Cut one list into half choosing indexes randomly
    :param population_fitness: input list of fitness
    :param population: input list of routes
    :return: two vectors in one list
    """

    random_i_list = random.sample(population_fitness, len(population)//2)
    reverso_random_i_list = [x for x in population_fitness if x not in random_i_list]
    max1 = max(random_i_list)

    max2 = population_fitness[0]
    i=0
    if reverso_random_i_list:
        max2 = max(reverso_random_i_list)
    else:
        while i < len(population_fitness) and population_fitness[i] == max1:
            max2 = population_fitness[i]
            i += 1

    id = population_fitness.index(max1)
    reverso_id = population_fitness.index(max2)

    return [  [id, max1, population[id]],  [reverso_id, max2, population[reverso_id]]  ]
