import random
import matplotlib.pyplot as plt
import numpy as np
 

def busqueda_secuencial_comps(lista, x):
    comps = 0
    pos = -1
    for i, z in enumerate(lista):
        comps += 1
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria_comps(lista, x):
    comps = 0
    pos = -1
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        comps += 1 

        if lista[medio] == x:
            pos = medio
            break
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1

    return pos, comps


def generar_lista(n, m):
    l = random.sample(range(m), k=n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m - 1)


def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista, x)[1]
    return comps_tot / k

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista, x)[1]
    return comps_tot / k

def graficar_bbin_vs_bseq(m, k):
    largos = np.arange(1, 257)
    comps_seq = np.zeros(len(largos))
    comps_bin = np.zeros(len(largos))

    for i, n in enumerate(largos):
        lista = generar_lista(n, m)
        comps_seq[i] = experimento_secuencial_promedio(lista, m, k)
        comps_bin[i] = experimento_binario_promedio(lista, m, k)

    plt.plot(largos, comps_seq, label='Búsqueda Secuencial')
    plt.plot(largos, comps_bin, label='Búsqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Comparaciones promedio")
    plt.title("Comparación de complejidad: Búsqueda Secuencial vs Binaria")
    plt.legend()
    plt.xlim(0, 256)
    plt.ylim(0, max(comps_seq) * 1.1)
    plt.grid(True)
    plt.show()


#graficar_bbin_vs_bseq(10000, 1000)
