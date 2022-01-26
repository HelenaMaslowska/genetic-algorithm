import random

def mutation(genotype):
    a = random.randint(1, len(genotype) - 2)
    b = random.randint(a, len(genotype) - 1)
    genotype[a], genotype[b] = genotype[b], genotype[a]
    return genotype

def mutation_seq(genotype):
    a = random.randint(1, len(genotype) - 2)
    b = random.randint(a, len(genotype) - 1)
    genotype[a:b] = reversed(genotype[a:b])
    return genotype

def random_mutation(num_of_cities):
    return [0] + random.sample(range(1, num_of_cities), num_of_cities - 1)
