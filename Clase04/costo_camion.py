import csv
def costo_camion(nombre_archivo):
    ruta = rf'C:\Users\gonza\OneDrive\Escritorio\Programacion_1\Ejercicios\programacion1-unsam\data\{nombre_archivo}'
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
#costo = costo_camion("missing.csv")
#costo = costo_camion("camion.csv")
costo = costo_camion("fecha_camion.csv")