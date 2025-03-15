def diccionario_geringoso(lista):
    diccionario = {}
    def traductor(palabra):
        vocales = 'aeiouAEIOU'
        cadena = ''
        for c in palabra:
            cadena += c
            if c in vocales:
                cadena += 'p' + c
        return cadena
    for l in lista:
        diccionario[l] = traductor(l)
    print(diccionario)

lista=['banana', 'manzana', 'mandarina']
diccionario_geringoso(lista)