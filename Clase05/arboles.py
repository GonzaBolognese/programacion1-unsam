import csv
from collections import Counter
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

RUTA_ARCHIVO = r"C:\Users\gonza\OneDrive\Escritorio\Programacion_1\Ejercicios\programacion1-unsam\data\arbolado-en-espacios-verdes.csv"

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

def medidas_de_especies(especies,arboleda):
    medidas = dict()
    # longitudes = dict() # Para controlar cuantos pares de numero por especie hay
    for e in especies:
        H=[(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == e]
        medidas[e] = H 
        # longitudes[e] = len(H) Agrega cuantos pares de numeros hay para la especie e
    
    return medidas

arboleda = leer_parque(RUTA_ARCHIVO)

medidas = medidas_de_especies(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'], arboleda)


print(medidas)