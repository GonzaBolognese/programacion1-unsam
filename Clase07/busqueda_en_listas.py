def busqueda_lineal_lordenada(lista,e):
    '''
    Si se encuentra un elemento mayor a e la funcion
    devuelve la posición de ese numero
    sino hay ningun numero mayor a e devuelve -1
    '''
    pos = -1
    for i, z in enumerate(lista):
        if z>e:
            pos = i
            break
    return pos


def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista, x, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(lista)
    
    if izquierda >= derecha:
        return izquierda

    medio = int((izquierda + derecha) / 2)
    
    if lista[medio] < x:
        return donde_insertar(lista, x, medio + 1, derecha)
    else:
        return donde_insertar(lista, x, izquierda, medio)




prueba = donde_insertar([0,2,5,6,8,10,11,15,16,25], 12)

print(prueba)

