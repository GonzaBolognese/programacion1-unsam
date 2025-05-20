import random

def tirar(dados):
    tirada = []
    for i in range(dados):
        tirada.append(random.randint(1,6))
    return sorted(tirada)


def juego(t=3, lista=[]):
    '''
    juego busca en 3 tiradas de dados juntar 5 dados iguales
    primero tira y se guarda los dados del mismo numero que se hayan repetido mas veces
    Y vuelve a tirar los dados restantes intentando que los 5 dados sean iguales
    Si los 5 dados son iguales deja de tirar y devuelve la lista con 5 numeros iguales
    Sino luego de 3 tiradas devuelve como le quedo la tirada final.
    '''
    if len(lista) == 0:
        dados = tirar(5)
        lista = dados
    else:
        if len(lista) == 5 and max(lista) == min (lista):
            return lista
        dados = tirar(5-len(lista))
        lista = sorted(lista + dados)
    numeros = [0,0,0,0,0,0]
    mejor = 0
    index = 0
    for n in lista:
        numeros[n-1]+=1
    for i,c in enumerate(numeros):
        if c > mejor:
            mejor = c
            index = i
    
    if t > 1:
        if mejor == 1:
            return juego(t=t-1)
        nuevo =[]
        for i in range(numeros[index]):
            nuevo.append(index+1)
        return juego(t=t-1, lista=nuevo)
    return lista



print(juego())
