def buscar_u_elemento(lista, e):
    pos = -1
    i = 0
    for i, z in enumerate(lista):
        if e == z:
            pos = i
        i += 1
    return pos

def buscar_n_elemento(lista, e):
    pos = 0
    i = 0
    for i, z in enumerate(lista):
        if z == e:
            pos += 1
        i +=0
    return pos

def maximo(lista):
    m = lista[0]
    for e in lista:
        if e>m:
            m = e
    return m

def minimo(lista):
    m = lista[0]
    for e in lista:
        if e<m:
            m = e
    return m

def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    print(invertida)

invertir_lista([1, 2, 3, 4, 5])
invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])