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

def comprar_paquete_sin_repetir(figus_total, figus_paquete):
    return random.sample(range(figus_total), k=figus_paquete)


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

def calcular_historia_figus_pegadas(figus_total, figus_paquete, repetidas_paquete=True):
    album = crear_album(figus_total)
    historia_figus_pegadas = []
    while album_incompleto(album):
        if repetidas_paquete:
            paquete = comprar_paquete(figus_total, figus_paquete)
        else:
            paquete = comprar_paquete_sin_repetir(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas


def calcular__historia_figus_pegadas_amigos(figus_total, figus_paquete, repetidas_paquete=True, cant_amigos=5):
    album = crear_album(figus_total)
    completo = False
    historia_figus_pegadas = []
    while completo:
        if repetidas_paquete:
            paquete = comprar_paquete(figus_total, figus_paquete)
        else:
            paquete = comprar_paquete_sin_repetir(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] += 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas) 
        if min(album) == 5:
            completo = True
    return historia_figus_pegadas

            

    
    


def probabilidad_de_llenar (n_paquetes, figus_total, figus_paquete, repetidas_paquete=True, num_simulaciones=1000):
    '''
    Esta funcion completa num_simulaciones albumnes y compara cuantos de esos num_simulaciones albumnes
    se completaron con menos de los paquetes indicados.
    '''
    informe = np.zeros(num_simulaciones)
    for i in range(num_simulaciones):
        paquetes_abiertos = len(calcular_historia_figus_pegadas(figus_total,figus_paquete,repetidas_paquete=repetidas_paquete))
        if paquetes_abiertos <= n_paquetes:
            informe[i] = 1
    probabilidad = np.sum(informe)/num_simulaciones
    return f'La probabilidad de completar el album con {n_paquetes} es de: %{probabilidad*100}'

def paquetes_para_probabilidad_deseada(porcentaje_deseado, figus_total, figus_paquete, repetidas_paquete=True, num_simulaciones=1000):
    '''
    Estima cuántos paquetes habría que comprar para tener una probabilidad
    del 'porcentaje_deseado'% de completar el álbum.
    '''
    resultados_simulaciones = np.zeros(num_simulaciones)
    for i in range(num_simulaciones):
        paquetes_abiertos = len(calcular_historia_figus_pegadas(figus_total, figus_paquete, repetidas_paquete=repetidas_paquete))
        resultados_simulaciones[i] = paquetes_abiertos
    
    np.sort(resultados_simulaciones)
    indice_percentil = int(num_simulaciones*(porcentaje_deseado/100) - 1)
    if indice_percentil < 0:
        indice_percentil = 0
    paquetes_necesarios = resultados_simulaciones[indice_percentil]

    return paquetes_necesarios





figus_total = 670
figus_paquete = 5
n_paquetes = 850

#Ejercicio 6.22:
#Curva de llenado
#plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
#plt.xlabel("Cantidad de paquetes comprados.")
#plt.ylabel("Cantidad de figuritas pegadas.")
#plt.title("La curva de llenado se desacelera al final")
#plt.show()

#Probabilidades de completar con n paquetes
#print(probabilidad_de_llenar(n_paquetes, figus_total, figus_paquete))

#Ejercicio 6.26:
#Probabilidades de completar con n paquetes sin figus repetidas en los paquetes
#print(probabilidad_de_llenar(n_paquetes, figus_total, figus_paquete, repetidas_paquete=False))

#Ejercicio 6.24: Plotear el histograma
#Histograma de paquetes
# cuantos_paquetes = [len(calcular_historia_figus_pegadas(figus_total, figus_paquete)) for _ in range(1000)]
# plt.hist(cuantos_paquetes, bins=50)
# plt.xlabel('Cantidad de paquetes comprados')
# plt.ylabel('Cantidad cantidad de álbumes')
# plt.title('Cantidad de álbumes completados x Cantidad de Paquetes')
# plt.show()

#Ejercicio 6.25:
#Cantidad de paquetes necesarios para completar el album con un 90% de seguridad
#print(paquetes_para_probabilidad_deseada(90, figus_total, figus_paquete))

#Ejercicio 6.26:
#Cantidad de paquetes necesarios para completar el album con un 90% de seguridad sin figus repetidas en los paquetes
#print(paquetes_para_probabilidad_deseada(90, figus_total, figus_paquete, repetidas_paquete=False))