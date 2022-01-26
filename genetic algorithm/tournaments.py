import random

# TURNIEJ
def tournament(num_of_cities, genes, n, leng):
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


# TURNIEJ 2
# zwraca 2 wektory o największej wartości [index genu, funkcja przystosowania, ścieżka]
def tournament2(genes, genes_path):
    #wersja 2 algorytmu
    #length = len(genes_path) ---------- można obliczyć raz i zastąpić
    cp_genes_path = genes_path
    tab = [random.randint(0, 1) for _ in range(len(genes_path))]
    while not (len(genes_path) // 3 < sum(tab) < len(genes_path) //3 * 2):
        tab = [random.randint(0, 1) for _ in range(len(genes_path))]

    max1 = max2 = -1
    for i in range(len(genes_path)):
        if tab[i] == 1:
            max1 = max(max1, genes[i])
        else:
            max2 = max(max2, genes[i])

    winners = [[0,0,0], [0,0,0]]
    winners[0][0] = genes.index(max1)
    winners[0][1] = max1
    winners[0][2] = genes_path[genes.index(max1)]
    winners[1][0] = genes.index(max2)
    winners[1][1] = max2
    winners[1][2] = genes_path[genes.index(max2)]
    return winners

def tournament3(population_fitness, population):
    # losuje polowe zbioru do jednej listy, reszta do drugiej, wybiera max z obu
    # zwraca w postaci takiej jak tournament 2
    # wersja 3 algorytmu
    # naprawić błąd - po wielu iteracjach znacznie
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
            # w tym miejscu jest po czasie coraz czesciej, najpewniej przez to że wartości zaczynają się powtarzać


    id = population_fitness.index(max1)
    reverso_id = population_fitness.index(max2)

    return [    [id,            max1, population[id]            ],
                [reverso_id,    max2, population[reverso_id]    ]   ]
