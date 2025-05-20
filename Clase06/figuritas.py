import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(A):
    return 0 in A

def comprar_figu(figus_total):
    '''
        Simula comprar 1 figurita suelta
    '''
    return random.randint(1, figus_total)

def comprar_paquete(figus_total, figus_paquete):
    return random.choices(range(figus_total), k=figus_paquete)


def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    cantidad = 0
    while album_incompleto(album):
        cantidad += 1
        figu = comprar_figu(figus_total)
        album[figu-1] += 1
    return cantidad

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    cantidad = 0
    while album_incompleto(album):
        cantidad += 1
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            album[figu-1] += 1
    return cantidad


def album_6(n):
    return np.mean([cuantas_figus(6) for _ in range(n)])

def experimento_figus(n_repeticiones, figus_total):
    '''
        simule el llenado de n_repeticiones álbums de figus_total figuritas
        y devuelva el número estimado de figuritas que hay que comprar,
        en promedio, para completar el álbum.
    '''
    return round(np.mean([cuantas_figus(figus_total) for _ in range(n_repeticiones)]))

def paquete_5(n_repeticiones,figus_total, figus_paquete):
    return round(np.mean([cuantos_paquetes(670, 5) for _ in range(n_repeticiones)]))



#print(experimento_figus(100, 670)) #Simula el promedio de figus compradas para llenar 100 algunes de 670 figus
#print(comprar_paquete(670, 5))
#print(cuantos_paquetes(670, 5))
#print(paquete_5(1000,670,5))

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()