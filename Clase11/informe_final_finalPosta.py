import sys
import csv
from lote import Lote  # Suponiendo que lote.py está en el mismo directorio
import formato_tabla  # Suponiendo que formato_tabla.py está en el mismo directorio

def leer_camion(nombre_archivo):
    '''Lee un archivo de lotes en un camión 
    y lo devuelve como una lista de objetos Lote.
    '''
    camion = []
    try:
        with open(nombre_archivo, 'rt', encoding='utf-8') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for n_linea, row in enumerate(rows, 2):
                try:
                    record = Lote(row[0], int(row[1]), float(row[2]))
                    camion.append(record)
                except ValueError:
                    print(f'Faltan datos o son incorrectos en la linea {n_linea} del archivo {nombre_archivo}.')
    except FileNotFoundError:
        print(f'No se encontró el archivo: {nombre_archivo}')
    return camion

def leer_precios(nombre_archivo):
    '''Lee un archivo CSV de precios y lo devuelve
    como un diccionario.'''
    lista_precios = {}
    try:
        with open(nombre_archivo, 'rt', encoding='utf-8') as f:
            rows = csv.reader(f)
            for row in rows:
                if row and len(row) == 2:
                    try:
                        lista_precios[row[0]] = float(row[1])
                    except ValueError:
                        print(f'No se pudo convertir el precio en la fila: {row}')
    except FileNotFoundError:
        print(f'No se encontró el archivo: {nombre_archivo}')
    return lista_precios

def hacer_informe(costos, precios):
    '''Crea los datos del informe a partir de la lista del
    camión y el diccionario de precios.'''
    informe = []
    for c in costos:
        precio_venta = precios.get(c.nombre, 0)
        cambio = precio_venta - c.precio
        registro = (c.nombre, c.cajones, precio_venta, cambio)
        informe.append(registro)
    return informe

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas.
    '''
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt='txt'):
    '''
    Crea un informe a partir de los archivos del camión y precios.
    '''
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    data_informe = hacer_informe(camion, precios)
    
    # Delega la creación del formateador a la función fábrica
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)

def main(argv):
    """
    Función principal que maneja los argumentos de línea de comandos.
    """
    # Verificamos el número de argumentos
    if len(argv) < 3:
        print("Uso: python informe_final_finalPosta.py archivo_camion archivo_precios [formato]")
        print("Formatos disponibles: txt, csv, html")
        return

    archivo_camion = argv[1]
    archivo_precios = argv[2]
    
    # El formato es opcional. Si no se provee, se usa 'txt'.
    if len(argv) == 4:
        fmt = argv[3]
    else:
        fmt = 'txt'
        
    informe_camion(archivo_camion, archivo_precios, fmt)

if __name__ == '__main__':
    main(sys.argv)