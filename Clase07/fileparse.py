import csv

def parse_csv(nombre_archivo, select=None, types=[], has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        if has_headers:
            headers = next(rows)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            encabezado = select
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
                    row[i] = t(row[i]) 
            
            # Armar el diccionario
            if has_headers:
                registro = dict(zip(headers, row))
                registros.append(registro)
            else:
                registros.append(tuple(row))

    return registros