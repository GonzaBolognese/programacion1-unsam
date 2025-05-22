import csv
def costo_camion(nombre_archivo):
    ruta = rf'{nombre_archivo[1]}'
    f = open(ruta)
    filas = csv.reader(f)
    headers = next(filas)
    suma = 0
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(headers, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            suma += ncajones*precio
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    print(f'El costo total fue de: {suma}')

def f_principal(nombre_archivo):
    costo_camion(nombre_archivo)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        costo_camion(["Costo_camion.py", "../Data/camion.csv"])
    else:
        costo_camion(sys.argv)

#costo = costo_camion("missing.csv")
#costo = costo_camion("camion.csv")
#costo = costo_camion("../Data/fecha_camion.csv")
