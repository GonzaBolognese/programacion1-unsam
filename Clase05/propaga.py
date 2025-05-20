def propagar(vector):
    lista = vector
    i = 0
    while i < len(lista) - 1:
        if lista[i] == 1 and lista[i-1] == 0:
            lista[i-1] = 1
        if lista[i] == 1 and lista[i+1] == 0:
            lista[i+1] = 1
        i += 1

    j = 0
    while j < len(lista) - 1:
        if lista[j] == 0 and lista[j+1] == 1:
            lista = propagar(lista)
            break
        j += 1
        
    return lista

prueba = propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
prueba1 = propagar([ 0, 0, 0, 1, 0, 0])
    
print(prueba)
print(prueba1)
            
