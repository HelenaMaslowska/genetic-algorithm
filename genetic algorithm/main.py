import random


def form(per):
    form = []
    mini = min(per)
    ind = per.index(mini)
    for i in range(ind, len(per)):
        form.append(per[i])
    for i in range(ind):
        form.append(per[i])
    return form


def good(per, permutations):
    pers = []
    for i in permutations.values():
        pers.append(form(i))
    per = form(per)
    if per in pers or per.reverse() in pers:
        return False
    return True


# PERMUTACJA LISTY LICZB OD 0 DO RAN, BEZ POWTÓRZEŃ W PERS
def permutation(ran, pers):
    while True:
        per = random.sample(range(ran),ran)
        if good(per, pers):
            return per


# FUNKCJA PRZYSTOSOWANIA
def fitness(genes, matrix):
    fit = 0
    for i in range(len(genes)):
        if i == len(genes) - 1:
            fit += matrix[genes[i]][genes[0]]
            break
        fit += matrix[genes[i]][genes[i + 1]]
    return 1000000/fit


# TURNIEJ
def tournament(v, p, n, leng):
    winners = []
    while len(winners) < n:
        tmp = []
        indices = random.sample(range(v), leng)
        for i in indices:
            tmp.append(p[i])
        maxi = max(tmp)
        if maxi not in winners:
            winners.append(maxi)
    return winners


# TWORZENIE MACIERZY
v = 6
mini = 100
maxi = 600
matrix = []
for i in range(v):
    matrix.append([])
    for j in range(v):
        if i == j:
            matrix[i].append(0)
        elif j > i:
            matrix[i].append(random.randint(mini, maxi))
        else:
            matrix[i].append(matrix[j][i])
    print(matrix[i])

# TWORZENIE POCZĄTKOWEJ POPULACJI
n = 8
p = {}
p_f = {}
for i in range(n):
    p[i] = permutation(v, p)
    p_f[i] = fitness(p[i], matrix)
print(p.values())
print(p_f.values())

# TURNIEJ chyba szuka najmniejszego
print(tournament(v, p, 2, 3))






