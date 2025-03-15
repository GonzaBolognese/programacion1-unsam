import csv
def costo_camion(nombre_archivo):
    ruta = rf'C:\Users\gonza\OneDrive\Escritorio\Programacion_1\Ejercicios\programacion1-unsam\data\{nombre_archivo}'
    try:
        f = open(ruta)
        rows = csv.reader(f)
        next(rows)
        suma = 0
        for r in rows:
            suma += float(r[2])
        f.close()
        print(suma)
    except:
        print("El archivo seleccionado no es compatible")    
costo_camion("camion.csv")