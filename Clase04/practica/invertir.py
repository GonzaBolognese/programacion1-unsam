precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }

#Si usás el método items(), obtenés pares (clave,valor):
print(precios.items())

#Sin embargo, si lo que querés son pares (valor, clave)

lista_precios = list(zip(precios.values(),precios.keys()))
print(lista_precios)

#¿Por qué haría algo así? Por un lado porque te permite realizar cierto tipo de procesamiento de datos sobre la información del diccionario.
min(lista_precios)
max(lista_precios)
sorted(lista_precios)


