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

def balance(ruta_camion, ruta_venta):
    costos = leer_camion(ruta_camion)
    precios = leer_precios(ruta_venta)
    stock = Counter()
    balance = {}
    for c in costos:
        stock[c['nombre']] += int(c['cajones'])
    for s in stock:
        if s in precios:
            balance[f'precio_{s}'] = precios[s]
    
    balance = {
        'costos': sum([int(s['cajones'])*float(s['precio']) for s in costos]),
        'ventas': sum([int(stock[c])*float(precios[c]) for c in stock ])
    }
    
    print(f' Costo: ${balance["costos"]}\n Ventas: ${balance["ventas"]}\n -------------------------\n Ganancia neta: ${round(balance["ventas"]-balance["costos"],2)}')
    return costos

camion = balance(r"C:\Users\gbolognese\Documents\Prs\programcion\programacion1-unsam\Data\camion.csv", r"C:\Users\gbolognese\Documents\Prs\programcion\programacion1-unsam\Data\precios.csv")