import os
import shutil
import datetime
import sys

def procesar_nombre(fname):
    """
    Dado un nombre de archivo con formato 'nombre_YYYYMMDD.png',
    devuelve una tupla con el nuevo nombre ('nombre.png') y la fecha como datetime.
    
    >>> procesar_nombre('correlation_20200924.png')
    ('correlation.png', datetime.datetime(2020, 9, 24, 0, 0))
    """
    nueva_fecha = datetime.datetime.strptime(fname[-12:-4], '%Y%m%d')
    nuevo_nombre = fname[:-13] + fname[-4:]
    return nuevo_nombre, nueva_fecha

def procesar(fname, destino):
    """
    Procesa un archivo PNG: obtiene nombre y fecha corregida,
    actualiza la fecha del sistema y lo mueve al directorio destino.
    """
    nuevo_nombre, fecha = procesar_nombre(os.path.basename(fname))
    
    path_destino = os.path.join(destino, nuevo_nombre)
    
    # Cambiar fecha de modificación y acceso del archivo
    timestamp = fecha.timestamp()
    os.utime(fname, (timestamp, timestamp))
    
    # Mover el archivo con el nuevo nombre
    shutil.move(fname, path_destino)

def ordenar_imgs(origen, destino):
    """
    Recorre el directorio origen buscando archivos .png,
    y los procesa uno por uno moviéndolos al directorio destino.
    """
    if not os.path.exists(destino):
        os.mkdir(destino)

    for root, dirs, files in os.walk(origen):
        for name in files:
            if name.endswith("png"):
                path_completo = os.path.join(root, name)
                procesar(path_completo, destino)

# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print("Uso: python ordenar_imgs.py <directorio_origen> <directorio_destino>")
#         sys.exit(1)
#     
#     origen = sys.argv[1]
#     destino = sys.argv[2]
#     ordenar_imgs(origen, destino)
