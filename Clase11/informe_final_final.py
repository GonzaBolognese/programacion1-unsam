import csv
from collections import Counter
from lote import Lote
import formato_tabla

def leer_camion(nombre_archivo):
    camion = []
    try:
        with open(nombre_archivo, 'rt', encoding='utf-8') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for n_linea, row in enumerate(rows, 2):
                try:
                    record = Lote(*row)
                    camion.append(record)
                except ValueError:
                    print(f'Faltan datos o son incorrectos en la linea {n_linea} del archivo {nombre_archivo}.')
    except FileNotFoundError:
        print(f'No se encontró el archivo: {nombre_archivo}')

    return camion

def leer_precios(nombre_archivo):
    lista_precios = {}
    try:
        with open(nombre_archivo, 'rt', encoding='utf-8') as f:
            rows = csv.reader(f)
            for row in rows:
                # Asegurarse que la fila no está vacía y tiene 2 elementos
                if row and len(row) == 2:
                    try:
                        lista_precios[row[0]] = float(row[1])
                    except ValueError:
                        print(f'No se pudo convertir el precio en la fila: {row}')
                else:
                    print(f'Se ignoró una línea con formato incorrecto: {row}')
    except FileNotFoundError:
        print(f'No se encontró el archivo: {nombre_archivo}')
        
    return lista_precios

def hacer_informe(costos, precios):
    # Devuelve una lista de tuplas con los datos del informe
    informe = []
    for c in costos:
        # Calculamos el cambio (ganancia o pérdida)
        cambio = precios.get(c.nombre, 0) - c.precio
        registro = (c.nombre, c.cajones, c.precio, cambio)
        informe.append(registro)
    return informe

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas.
    '''
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        # Formateamos los datos antes de pasarlos a la fila
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt='txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt.
    Alternativas: csv o html.
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # -------- MODIFICACIÓN PRINCIPAL --------
    # Delega la creación del formateador a la función fábrica.
    formateador = formato_tabla.crear_formateador(fmt)
    
    # Imprime el informe usando el formateador elegido.
    imprimir_informe(data_informe, formateador)


def f_principal(parametros):
    camion = leer_camion(parametros[1])
    precios = leer_precios(parametros[2])
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
        f_principal(["tabla_informe.py", "./Data/camion.csv", "./Data/precios.csv"])
    elif len(sys.argv) == 2:
        f_principal(["tabla_informe.py", sys.argv[1], "../Data/precios.csv"])
    else:
        f_principal(["tabla_informe.py", sys.argv[1], sys.argv[2]])

