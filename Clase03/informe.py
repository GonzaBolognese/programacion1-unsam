import csv

def leer_camion(ruta):
    camion = []
    with open(rf'U:\Gonzalo\Documentos\Prs\programacion\programacion1-unsam{ruta}', 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                lote = (row[0], int(row[1]), float(row[2]))
                camion.append(lote)
            return camion
        except:
            print('Faltan datos en la linea', row, 'Del archivo.')
    

leer_camion("/Data/camion.csv")