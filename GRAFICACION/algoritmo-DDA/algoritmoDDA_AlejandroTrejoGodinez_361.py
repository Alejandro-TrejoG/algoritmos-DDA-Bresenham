import matplotlib.pyplot as plt


def algoritmo_DDA(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx > dy:
        steps = dx
        print("steps = dx = ", dx)
    else:
        steps = dy
        print("steps = dy = ", dy)

    xinc = float(dx / steps)
    yinc = float(dy / steps)

    xinc = round(xinc, 1)
    yinc = round(yinc, 1)
    i = 0
    for i in range(steps + 1):
        plt.plot(round(x1), round(y1), "bs")
        x1 += xinc
        y1 += yinc

        print("x => ", round(x1))
        print("y => ", round(y1))
    plt.show()


x1 = int(input("Ingresa el valor de x1: "))
y1 = int(input("Ingresa el valor de y1: "))
x2 = int(input("Ingresa el valor de x2: "))
y2 = int(input("Ingresa el valor de y2: "))
algoritmo_DDA(x1, y1, x2, y2)
