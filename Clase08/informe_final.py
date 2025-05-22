import csv
from collections import Counter

def leer_camion(ruta):
    camion = []
    rows = csv.reader(ruta)
    headers = next(rows)
    try:
        for row in rows:
            record = dict(zip(headers, row))
            camion.append(record)
        return camion
    except:
        print('Faltan datos en la linea', row, 'Del archivo.')

def leer_precios(ruta):
    rows = csv.reader(ruta)
    lista_precios = {}
    for row in rows:
        if len(row) != 0:
            lista_precios[row[0]] = row[1]
    return lista_precios

def hacer_informe(costos, precios):
    informe = [('Nombre', 'Cajones', 'Precio', 'Cambio'), ('----------','----------','----------','----------')]
    for c in costos:
        registro = (c['nombre'], int(c['cajones']), float(c['precio']), float(precios[c['nombre']])-float(c['precio']))
        informe.append(registro)
    return informe

def f_principal(parametros):
    with open(parametros[1], 'rt') as f:
        camion = leer_camion(f)
    with open(parametros[2], 'rt') as g:
        precios = leer_precios(g)
    informe = hacer_informe(camion, precios)
    
    for nombre, cajones, precio, ganancia in informe:
        precio_str = f'${str(precio)}'
        if isinstance(cajones, str) and isinstance(precio, str) and isinstance(ganancia, str) :
            print(f'{nombre:>10s} {cajones:>10s} {precio:>10s} {ganancia:>10s}')
        else:
            print(f'{nombre:>10s} {cajones:>10d} {precio_str:>10s} {ganancia:>10.2f}')



if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        f_principal(["tabla_informe.py", "../Data/camion.csv", "../Data/precios.csv"])
    elif len(sys.argv) == 2:
        f_principal(["tabla_informe.py", sys.argv[1], "../Data/precios.csv"])
    else:
        f_principal(["tabla_informe.py", sys.argv[1], sys.argv[2]])

