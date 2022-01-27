from graphics import *

def draw(cities, genes, dim, title):
    ratio = round(700/dim, 3)
    print(ratio)
    win = GraphWin(title, 700, 700)
    win.setCoords(0,0,700,700)

    for i in range(len(cities)):
        x = ratio*cities[i][0]
        y = ratio*cities[i][1]
        cir = Circle(Point(x, y), 5)
        cir.setFill('green')
        cir.draw(win)

    for i in range(len(genes) - 1):
        x1 = ratio * cities[genes[i]][0]
        y1 = ratio * cities[genes[i]][1]
        x2 = ratio * cities[genes[i+1]][0]
        y2 = ratio * cities[genes[i+1]][1]
        route = Line(Point(x1, y1), Point(x2, y2))
        route.draw(win)
    x1 = ratio * cities[genes[len(genes) - 1]][0]
    y1 = ratio * cities[genes[len(genes) - 1]][1]
    x2 = ratio * cities[genes[0]][0]
    y2 = ratio * cities[genes[0]][1]
    route = Line(Point(x1, y1), Point(x2, y2))
    route.draw(win)

    win.getMouse()
    win.close()
