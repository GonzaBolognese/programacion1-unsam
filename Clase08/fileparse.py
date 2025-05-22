import csv

def parse_csv(nombre_archivo, select=None, types=[], has_headers=True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    rows = csv.reader(nombre_archivo)
    # Lee los encabezados
    if has_headers:
        headers = next(rows)
    # Si se indicó un selector de columnas,
    #    buscar los índices de las columnas especificadas.
    # Y en ese caso achicar el conjunto de encabezados para diccionarios
    if select:
        try:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            encabezado = select
        except UnboundLocalError as e:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
    else:
        indices = []
    registros = []
    for row in rows:
        if not row:    # Saltea filas sin datos
            continue
        if indices:
            row = [row[index] for index in indices]
        if len(types) != 0:
            for i, t in enumerate(types):
                try: 
                    row[i] = t(row[i]) 
                except ValueError as e:
                    if not silence_errors:
                        print(f'Fila {i}: No pude convertir {row}')
                        print(f'Fila {i}: Motivo: {e}')
                except IndexError as e:
                    raise RuntimeError(f'El archivo tuvo problemas de iteración por el siguiente motivo: {e}')
        
        # Armar el diccionario
        if has_headers:
            registro = dict(zip(headers, row))
            registros.append(registro)
        else:
            registros.append(tuple(row))

    return registros

with open('../Data/missing.csv') as f:
    camion = parse_csv('../Data/missing.csv', types = [str, int, float])
print(camion)