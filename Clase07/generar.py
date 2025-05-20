import random
import matplotlib.pyplot as plt
import numpy as np

def busqueda_binaria_comps(lista, x):
    pos = -1
    izq = 0
    der = len(lista)-1
    comps = 0

    while izq <= der:
        comps += 1
        medio = (izq+der) // 2
        if lista[medio] == x:
            pos = medio
            break
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return (pos, comps)

def busqueda_secuencial_comps(lista, x):
    pos = 0
    comps = 0
    for i,z in enumerate(lista):
        comps += 1
        if z == x:
            pos = i
            break
        if z>x:
            pos = -1
            break
    return (pos, comps)

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)


#print(generar_lista(10, 100))
m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)
x = generar_elemento(m)
comps = busqueda_secuencial_comps(lista, x)[1]
comps_bin = busqueda_binaria_comps(lista, x)[1]

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom, comps_tot

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista, x)[1]
    comps_prom = comps_tot / k
    return comps_prom, comps_tot

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio_secuencial = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_promedio_binario = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)[0]
    comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k)[0]

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio_secuencial,label = 'Búsqueda Secuencial')
plt.plot(largos,comps_promedio_binario,label = 'Búsqueda Binario')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()