import random

# TURNIEJ
def tournament(cities_counter, genes, n, leng):
    # losuje polowe zbioru do jednej listy, reszta do drugiej, wybiera max z obu
    # zwraca w postaci takiej jak tournament 2
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


# TURNIEJ 2
# zwraca 2 wektory o największej wartości [index, funkcja przystosowania, ścieżka]
def tournament2(genes, genes_path):
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
    return winners