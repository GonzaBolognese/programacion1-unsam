import csv

def leer_camion(ruta):
    camion = []
    with open(ruta, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                lote = {
                    'nombre': row[0],
                    'cajones': int(row[1]),
                    'precio': float(row[2])
                }
                camion.append(lote)
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
    stock ={}
    balance = {
        'costos': 0.0,
        'ventas': 0.0
    }
    for c in costos:
        balance['costos'] += c['precio']*c['cajones']
        if c['nombre'] in stock:
            stock[c['nombre']] += c['cajones']
        else:
            stock[c['nombre']] = c['cajones']
    for s in stock:
        if s in precios:
            balance[f'precio_{s}'] = precios[s]
            balance['ventas'] += (int(stock[s])*float(precios[s]))


    print(f' Costo: ${balance["costos"]}\n Ventas: ${balance["ventas"]}\n -------------------------\n Ganancia neta: ${round(balance["ventas"]-balance["costos"],2)}')

balance(r"./Data/camion.csv", r"./Data/precios.csv")