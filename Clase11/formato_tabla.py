class FormatoTabla:
    '''
    Clase base para la creación de tablas.
    '''
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        # Es necesario convertir todos los datos a string antes de unirlos
        print(','.join(str(d) for d in data_fila))

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        # Imprime la fila de encabezado <tr> con celdas <th>
        fila_th = ''.join(f'<th>{h}</th>' for h in headers)
        print(f'<tr>{fila_th}</tr>')

    def fila(self, data_fila):
        # Imprime una fila de datos <tr> con celdas <td>
        fila_td = ''.join(f'<td>{d}</td>' for d in data_fila)
        print(f'<tr>{fila_td}</tr>')

def crear_formateador(nombre):
    '''
    Crea un objeto formateador dado un nombre de formato.
    Formatos soportados: 'txt', 'csv', 'html'.
    '''
    if nombre.lower() == 'txt':
        return FormatoTablaTXT()
    elif nombre.lower() == 'csv':
        return FormatoTablaCSV()
    elif nombre.lower() == 'html':
        return FormatoTablaHTML()
    else:
        # Si el formato no es válido, lanza un error.
        raise RuntimeError(f'Formato desconocido: {nombre}')