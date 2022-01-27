from itertools import permutations

import main


def brute_force(matrix):
    ran = len(matrix)
    starting_city = (0,)
    perm = permutations(range(1, ran))
    mini_genes = ()
    mini = 0
    for i in list(perm):
        new = list(starting_city + i)
        test = main.distance(new, matrix)
        if mini == 0 or test < mini:
            mini = test
            mini_genes = new

    return list(mini_genes)

