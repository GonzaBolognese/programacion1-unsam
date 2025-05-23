import numpy as np
import matplotlib.pyplot as plt

def generar_datos(n):
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    return X, Y1, Y2

def graficar_barras(X, Y1, Y2):
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    # Etiquetas para barras positivas (azules)
    for x, y in zip(X, Y1):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='right', va='bottom')

    # Etiquetas para barras negativas (rojas)
    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='right', va='top')

    plt.ylim(-1.25, 1.25)
    plt.show()

def f_principal():
    n = 12
    X, Y1, Y2 = generar_datos(n)
    graficar_barras(X, Y1, Y2)

if __name__ == '__main__':
    f_principal()
