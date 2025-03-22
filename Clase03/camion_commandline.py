import csv
import sys


def costo_camion(nombre_archivo):
    ruta = nombre_archivo
    try:
        f = open(ruta)
        rows = csv.reader(f)
        next(rows)
        suma = 0
        for r in rows:
            if len(r[1]) != 0:
                suma += float(r[1])*float(r[2])
        f.close()
        return round(suma,2)
    except:
        print("El archivo seleccionado no es compatible")    

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'


costo = costo_camion(rf'{nombre_archivo}')
print('Costo total:', costo)
