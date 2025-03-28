import csv
from collections import Counter

def leer_camion(ruta):
    camion = []
    with open(ruta, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                record = dict(zip(headers, row))
                camion.append(record)
            return camion
        except:
            print('Faltan datos en la linea', row, 'Del archivo.')

def leer_precios(ruta):
    f = open(ruta, 'r')
    rows = csv.reader(f)
    lista_precios = {}
    for row in rows:
            if len(row) != 0:
                lista_precios[row[0]] = row[1]
    f.close()
    return lista_precios

def hacer_informe(costos, precios):
    informe = [('Nombre', 'Cajones', 'Precio', 'Cambio'), ('----------','----------','----------','----------')]
    for c in costos:
        registro = (c['nombre'], int(c['cajones']), float(c['precio']), float(precios[c['nombre']])-float(c['precio']))
        informe.append(registro)
    return informe

camion = leer_camion(r"./Data/camion.csv")
precios = leer_precios(r"./Data/precios.csv")
informe = hacer_informe(camion, precios)

"""
for r in informe:
    print(r)
"""

"""
for r in informe:
    print('%10s %10d %10.2f %10.2f'%r)
"""

for nombre, cajones, precio, ganancia in informe:
    precio_str = f'${str(precio)}'
    if isinstance(cajones, str) and isinstance(precio, str) and isinstance(ganancia, str) :
        print(f'{nombre:>10s} {cajones:>10s} {precio:>10s} {ganancia:>10s}')
    else:
        print(f'{nombre:>10s} {cajones:>10d} {precio_str:>10s} {ganancia:>10.2f}')