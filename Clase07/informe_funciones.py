import csv
from collections import Counter
import fileparse

def leer_camion(ruta):
    try:     
        return fileparse.parse_csv(ruta)
    except:
        print('Faltan datos en la linea del archivo.')

def leer_precios(ruta):
    try:
        headers = ('nombre', 'precio')
        return dict(fileparse.parse_csv(ruta,has_headers=False))
    except:
        print('Faltan datos en la linea del archivo.')

def hacer_informe(costos, precios):
    informe = [('Nombre', 'Cajones', 'Precio', 'Cambio'), ('----------','----------','----------','----------')]
    for c in costos:
        registro = (c['nombre'], int(c['cajones']), float(c['precio']), float(precios[c['nombre']])-float(c['precio']))
        informe.append(registro)
    return informe

def imprimir_informe(informe):
    for nombre, cajones, precio, ganancia in informe:
        precio_str = f'${str(precio)}'
        if isinstance(cajones, str) and isinstance(precio, str) and isinstance(ganancia, str) :
            print(f'{nombre:>10s} {cajones:>10s} {precio:>10s} {ganancia:>10s}')
        else:
            print(f'{nombre:>10s} {cajones:>10d} {precio_str:>10s} {ganancia:>10.2f}')

def informe_camion(data_camion, data_precios):
    camion = leer_camion(rf'{data_camion}') #./Data/camion.csv
    precios = leer_precios(rf'{data_precios}')#./Data/precios.csv
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

informe_camion('./Data/camion.csv','./Data/precios.csv')