import matplotlib.pyplot as plt

def plot(Y):
    X = [x for x in range(len(Y))]

    plt.plot(X, Y)
    plt.xlabel('Kolejne iteracje')
    plt.ylabel('Długość trasy')
    plt.show()


