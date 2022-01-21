from itertools import permutations

def brute_force(matrix):
    ran = len(matrix)
    starting_city = (0,)
    perm = permutations(range(1, ran))
    mini_genes = ()
    mini = 0
    for i in list(perm):
        new = list(starting_city + i)
        test = 0
        for i in range(len(new) - 1):
            test += matrix[new[i]][new[i + 1]]
        if mini == 0 or test < mini:
            mini = test
            mini_genes = new

    return list(mini_genes)
