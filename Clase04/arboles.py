import csv
from collections import Counter

def leer_parque(nombre_archivo, parque):
    lista_parque = []
    ruta = rf'C:\Users\gonza\OneDrive\Escritorio\Programacion_1\Ejercicios\programacion1-unsam\data\{nombre_archivo}'
    f = open(ruta, encoding="utf-8")
    filas = csv.reader(f)
    headers = next(filas)
    indice_filtro = headers.index('espacio_ve')

    for i, fila in enumerate(filas, start=1):
        if(fila[indice_filtro] == parque):
            lista_parque.append(dict(zip(headers, fila)))
    return lista_parque

def especies(lista_arboles):
    especies = set()
    for l in lista_arboles:
        if l['nombre_com'] != 'No Determinado' and l['nombre_com'] != 'No Determinable':
            especies.add(l['nombre_com'])
    print(especies)

def contar_ejemplares(lista_arboles):
    lista = Counter()
    for l in lista_arboles:
        if l['nombre_com'] != 'No Determinado' and l['nombre_com'] != 'No Determinable':
            lista[l['nombre_com']] += 1
    return lista.most_common(5)





data = {
    "General Paz": contar_ejemplares(leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")),
    "Los Andes": contar_ejemplares(leer_parque("arbolado-en-espacios-verdes.csv", "ANDES, LOS")),
    "Centenario": contar_ejemplares(leer_parque("arbolado-en-espacios-verdes.csv", "CENTENARIO"))
}

print("=" * 90)
print(f"{'General Paz':<30s}{'Los Andes':<30s}{'Centenario':<30s}")
print("=" * 90)

# Imprimir filas
for i in range(5):
     dato_General_Paz = f'{data['General Paz'][i][0]} : {data['General Paz'][i][1]}'
     dato_Los_Andes = f'{data['Los Andes'][i][0]} : {data['Los Andes'][i][1]}'
     dato_Centenario = f'{data['Centenario'][i][0]} : {data['Centenario'][i][1]}'
     print(f'{dato_General_Paz:<30s} {dato_Los_Andes:<30s} {dato_Centenario:<30s}')

print("=" * 90)