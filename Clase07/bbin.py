def busqueda_binaria(lista, x, verbose=False):
    '''Búsqueda binaria.
    Devuelve el índice si x está en lista, -1 si no está.
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio
            break
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return pos


def donde_insertar(lista, x, izquierda=0, derecha=None):
    '''Devuelve la posición de x si está, o la posición donde insertarlo'''
    if derecha is None:
        derecha = len(lista)
    
    if izquierda >= derecha:
        return izquierda

    medio = int((izquierda + derecha) / 2)
    
    if lista[medio] < x:
        return donde_insertar(lista, x, medio + 1, derecha)
    else:
        return donde_insertar(lista, x, izquierda, medio)




def insertar(lista, x):
    indice = donde_insertar(lista, x)
    if indice > len(lista)-1:
        lista.append(x)
        return (indice, lista)
    if lista[indice]!=x:
        izquierda = lista[0:indice]
        izquierda.append(x)
        derecha = lista[indice:]
        lista = izquierda + derecha
    return (indice, lista)

def busqueda_binaria_comps(lista, x):
    pos = -1
    izq = 0
    der = len(lista)-1
    comps = 0

    while izq <= der:
        comps += 1
        medio = (izq+der) // 2
        if lista[medio] == x:
            pos = medio
            break
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return (pos, comps)
    

    
#print(donde_insertar([1, 3, 8, 14,16,17,22,33,45],55))
#print(insertar([1, 3, 8, 14,16,17,22,33,45],12))
print(busqueda_binaria_comps([1, 3, 8, 14,16,17,22,33,45],0))