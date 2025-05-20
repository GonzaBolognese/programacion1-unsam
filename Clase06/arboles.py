import os
import csv
import matplotlib.pyplot as plt
import numpy as np

def leer_parque(nombre_archivo):
    arboleda = []
    try:
        ruta = f'{nombre_archivo}'
        f = open(ruta, encoding="utf-8")
        filas = csv.reader(f)
        headers = next(filas)
        indice_filtro = headers.index('espacio_ve')
        types = [float, float, int, int, int, int, int, str, str, str, str, str, str, str, str, float, float]
        

        for i, fila in enumerate(filas, start=1):
            lista_parque = [func(val) for func, val in zip(types, fila)]
            arboleda.append(dict(zip(headers, lista_parque)))
    except:
        print('Faltan valores en el archivo ingresado')
    return arboleda


ruta = os.path.join('.', 'Data', 'arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies,arboleda):
    arboleda = leer_parque(arboleda)
    medidas_especies = {}
    for especie in especies:
        altos = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == especie]
        diametro = [arbol['diametro'] for arbol in arboleda if arbol['nombre_com'] == especie]
        info_arbol = tuple(zip(altos, diametro))
        medidas_especies[especie] = info_arbol
    return medidas_especies

def scatter_hd(lista_de_pares, nombre):
    d = [arbol[1] for arbol in lista_de_pares]
    h = [arbol[0] for arbol in lista_de_pares]
    plt.scatter(d,h,alpha=0.2)
    plt.xlabel("Diametro (cm)")
    plt.ylabel("Alto (m)")
    plt.title(f'Relación diámetro-alto para {nombre}')
    plt.xlim(0,max(d)) 
    plt.ylim(0,max(h)) 
    plt.show()




# plt.hist(altos,bins=np.linspace(0,max(altos),25))
# plt.xlabel('Tamaño [Metros]')
# plt.ylabel('Cantidad de Jacarandas')
# plt.title('Distribución de alturas de Jacarandás')
# plt.show()
medidas_final = medidas_de_especies(especies, ruta)
for especie in especies:
    scatter_hd(medidas_final[especie], especie)