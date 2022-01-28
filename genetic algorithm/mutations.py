import random

def mutation(genotype):
    """
    Swap 2 numbers in input list
    :param genotype: this list
    :return: swapped list
    """
    a = random.randint(1, len(genotype) - 2)
    b = random.randint(a, len(genotype) - 1)
    genotype[a], genotype[b] = genotype[b], genotype[a]
    return genotype

def mutation_seq(genotype):
    """
    Swap fragment of list
    :param genotype: list which be swapped
    :return: swapped list
    """
    a = random.randint(1, len(genotype) - 2)
    b = random.randint(a, len(genotype) - 1)
    genotype[a:b] = reversed(genotype[a:b])
    return genotype

def random_mutation(num_of_cities):
    """
    Gets random list started with 0
    :param num_of_cities:
    :return: new random list started with 0
    """
    return [0] + random.sample(range(1, num_of_cities), num_of_cities - 1)
