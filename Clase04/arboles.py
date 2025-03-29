import csv
from collections import Counter

RUTA_ARCHIVO = r"C:\Users\gonza\OneDrive\Escritorio\Programacion_1\Ejercicios\programacion1-unsam\data\arbolado-en-espacios-verdes.csv"


def leer_parque(nombre_archivo, parque):
    lista_parque = []
    try:
        ruta = f'{nombre_archivo}'
        f = open(ruta, encoding="utf-8")
        filas = csv.reader(f)
        headers = next(filas)
        indice_filtro = headers.index('espacio_ve')

        for i, fila in enumerate(filas, start=1):
            if(fila[indice_filtro] == parque):
                lista_parque.append(dict(zip(headers, fila)))
    except:
        print('Faltan valores en el archivo ingresado')
    return lista_parque

def especies(lista_arboles):
    especies = set()
    try:
        for l in lista_arboles:
            if l['nombre_com'] != 'No Determinado' and l['nombre_com'] != 'No Determinable':
                especies.add(l['nombre_com'])
        return especies
    except:
        print('Faltan valores en el archivo ingresado')

def contar_ejemplares(lista_arboles):
    lista = Counter()
    try:
        for l in lista_arboles:
            if l['nombre_com'] != 'No Determinado' and l['nombre_com'] != 'No Determinable':
                lista[l['nombre_com']] += 1
        return lista.most_common(5)
    except:
        print('Faltan valores en el archivo ingresado')

def obtener_alturas(lista_arboles, especie):
    max = 0
    lista_Alturas = []
    try:
        for l in lista_arboles:
            if l['nombre_com'] == especie:
                if int(l['altura_tot']) > max:
                    max = int(l['altura_tot'])
                lista_Alturas.append(int(l['altura_tot']))
        promedio = sum(lista_Alturas)/len(lista_Alturas)

        return(max, promedio)
    except:
        print('Faltan valores en el archivo ingresado')

def obtener_inclinaciones(lista_arboles, especie):
    lista_Inclinacion = set()
    try:
        for l in lista_arboles:
            if l['nombre_com'] == especie:
                lista_Inclinacion.add(int(l['inclinacio']))
        return(lista_Inclinacion)
    except:
        print('Faltan valores en el archivo ingresado')

def especimen_mas_inclinado(lista_arboles):
    max_incli = dict()
    especies_unicas = especies(lista_arboles)
    mas_inclinado={'especie': '', 'inclinacion': 0}
    try:
        for e in especies_unicas:
            incli = obtener_inclinaciones(lista_arboles, e)
            max = 0
            for i in incli:
                if i>max:
                    max = i
            max_incli[e] = max
        for k in max_incli:
            if max_incli[k] > mas_inclinado['inclinacion']:
                mas_inclinado['especie'] = k
                mas_inclinado['inclinacion'] = max_incli[k]
        return (mas_inclinado['especie'], f'{mas_inclinado['inclinacion']}')
    except:
        print('Faltan valores en el archivo ingresado')

def especie_promedio_mas_inclinada(lista_arboles):
    prom_incli = dict()
    especies_unicas = especies(lista_arboles)
    especie_mas_inclinada = {'especie': '', 'inclinacion': 0}
    try:
        for e in especies_unicas:
            incli = obtener_inclinaciones(lista_arboles, e)
            prom = round(sum(incli)/len(incli), 2)
            prom_incli[e] = prom
        for k in prom_incli:
            if prom_incli[k] > especie_mas_inclinada['inclinacion']:
                especie_mas_inclinada['especie'] = k
                especie_mas_inclinada['inclinacion'] = prom_incli[k]
        return f'Los {especie_mas_inclinada["especie"]} del Parque {lista_arboles[0]['espacio_ve'].lower()} tiene un promedio de inclinación de {especie_mas_inclinada["inclinacion"]} grados.'
    except:
        print('Faltan valores en el archivo ingresado')


data = {
    "General Paz": obtener_alturas(leer_parque(RUTA_ARCHIVO, "GENERAL PAZ"), 'Jacarandá'),
    "Los Andes": obtener_alturas(leer_parque(RUTA_ARCHIVO, "ANDES, LOS"), 'Jacarandá'),
    "Centenario": obtener_alturas(leer_parque(RUTA_ARCHIVO, "CENTENARIO"), 'Jacarandá')
}

"""
print("=" * 120)
print(f"{'Descripcion':<30s}{'General Paz':<30s}{'Los Andes':<30s}{'Centenario':<30s}")
print("=" * 120)
"""


# Imprimir filas
"""
for i in range(5):
     dato_General_Paz = f'{data['General Paz'][i][0]} : {data['General Paz'][i][1]}'
     dato_Los_Andes = f'{data['Los Andes'][i][0]} : {data['Los Andes'][i][1]}'
     dato_Centenario = f'{data['Centenario'][i][0]} : {data['Centenario'][i][1]}'
     print(f'{dato_General_Paz:<30s} {dato_Los_Andes:<30s} {dato_Centenario:<30s}')

print("=" * 90)
"""
"""
print(f'{'max':<30s}{data["General Paz"][0]:<30d} {data["Los Andes"][0]:<30d} {data["Centenario"][0]:<30d}')
print(f'{'prom':<30s}{data["General Paz"][1]:<30.2f} {data["Los Andes"][1]:<30.2f} {data["Centenario"][1]:<30.2f}')
print("=" * 120)
"""

#print(obtener_inclinaciones(leer_parque(RUTA_ARCHIVO, "GENERAL PAZ"), 'Jacarandá'))
#print (especimen_mas_inclinado(leer_parque(RUTA_ARCHIVO, "GENERAL PAZ")))
#print (especimen_mas_inclinado(leer_parque(RUTA_ARCHIVO, "ANDES, LOS")))
#print (especimen_mas_inclinado(leer_parque(RUTA_ARCHIVO, "CENTENARIO")))

print (especie_promedio_mas_inclinada(leer_parque(RUTA_ARCHIVO, "GENERAL PAZ")))
print (especie_promedio_mas_inclinada(leer_parque(RUTA_ARCHIVO, "ANDES, LOS")))
print (especie_promedio_mas_inclinada(leer_parque(RUTA_ARCHIVO, "CENTENARIO")))