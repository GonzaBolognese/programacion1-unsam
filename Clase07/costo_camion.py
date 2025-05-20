import informe_funciones

def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion(nombre_archivo)
    costo_total = 0.0
    for item in camion:
        try:
            costo_total += item['cajones'] * item['precio']
        except KeyError as e:
            print(f'[ERROR] Falta la clave esperada en un registro: {e}')
        except TypeError:
            print(f'[ERROR] No se pudo calcular el costo de: {item}')
    print(f'El costo total fue de: {costo_total}')
    return costo_total

costo_camion("./Data/camion.csv")
