import matplotlib.pyplot as plt

def plot1(Y):
    X = [x for x in range(len(Y))]
    plt.plot(X, Y)
    plt.xlabel('Kolejne iteracje')
    plt.ylabel('Długość trasy')
    plt.show()

def plot2(effects, inter):
    Y = []
    x = 0
    while(True):
        avg = 0
        n = 0
        for i in range(len(effects)):
             if x < len(effects[i]):
                 avg += effects[i][x]
                 n += 1
        if avg == 0:
            break
        avg /= n
        Y.append(round(avg,2))
        n= 0
        x += 1

    print(Y)
    X = [x*inter for x in range(len(Y))]

    plt.plot(X, Y)
    plt.xlabel('Czas pracy algorytmu [s]')
    plt.ylabel('Dokładność rozwiązania [%]')
    plt.show()


