import matplotlib.pyplot as plt


def algoritmo_Besenham(x1, y1, x2, y2):
    x = x1
    y = y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx

    while x <= x2:
        plt.plot(x, y, "bs")
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + 2 * dy - 2 * dx
            y += 1
    plt.show()


x1 = int(input("Ingresa el valor de x1: "))
y1 = int(input("Ingresa el valor de y1: "))
x2 = int(input("Ingresa el valor de x2: "))
y2 = int(input("Ingresa el valor de y2: "))
algoritmo_Besenham(x1, y1, x2, y2)