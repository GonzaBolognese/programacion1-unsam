def valor_absoluto(n):
    '''
    Devuelve el valor absoluto de n.
    '''
    if n >= 0:
        return n
    else:
        return -n
    
def suma_pares(l):
    '''
    Calcula la sumatoria de los numeros pares.

    Pre: la lista contiene solo números enteros.
    Pos: Se devuelve el valor de sumar todos los números pares
        Si la lista esta vacía se devuelve 0.
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res ##res contiene la sumatoria de los numeros pares

def veces(a, b):
    '''
    Multiplica a por b.
    Si b es 0 devuelve. 
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res ##res contiene el valor de sumar a, b veces

def collatz(n):
    '''
    Calcula el número de pasos necesarios para que un número entero 'n'
    llegue a 1 siguiendo la secuencia de Collatz.

    Pre: n es un entero.
    Pos: Se devuelve el número de pasos hasta alcanzar 1

    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res #res contiene el número de pasos hasta alcanzar 1

