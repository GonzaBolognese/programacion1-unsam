def sumar_enteros_ciclo(desde, hasta):
    '''
    Calcula la sumatoria de los números entre desde y hasta.
    Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    medidor = desde
    suma = 0
    while medidor<=hasta:
        suma += medidor
        medidor += 1
    return suma

def sumar_enteros(desde, hasta):
    '''
    Calcula la sumatoria de los números entre desde y hasta.
    Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    base = ((desde*(desde+1))/2)-desde
    final = (hasta*(hasta+1))/2
    suma = int(final - base)

    return suma

print(sumar_enteros_ciclo(340,879))
print(sumar_enteros(340,879))