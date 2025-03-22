#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.5. Función tiene_a()
#Comentario: El error era de tipo sintactico. Los errores eran dos:
# 1 - El return False dentro del bucle while, ya que esto hacia que si el primer caracter del string no era una 'a' la funcion se frene tipo.
#    Lo corregí haciendo que retorne False una vez haya recorrido todo el string y salga del bucle while.
# 2 - Dentro del if estaba comparando de forma sensitiveCase lo cual hacia que si el texto ingresado estaba en mayuscula no iba a detectar una 'a'
#    Lo corregí usando el metodo .lower() para transformar cada letra en minuscula a la hora de comparar en el if.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        else:
            i += 1
    return False

#tiene_a('UNSAM 2020')
#tiene_a('abracadabra')
#tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.6. Función tiene_a()
#Comentario: El error era de tipo sintactico.
# 1 - Faltaban los ':' al final de la linea del def, al final de la linea del while y al final de la linea del if.
# 2 - Estaba mal escrito el return del booleano False, ya que estaba escrito sin capitalizar y eso no representa al booleano
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.7. Función tiene_uno(), nuevamente
#Comentario: El error es un error en tiempo de ejecución. 
# 1 - El problema es que asume que el dato ingresado va a ser un string
#    Lo corregí agarrando el paramatro ingresando y pasandolo por el metodo str() y guardando ese parametro pasado por el str() en una variable y trabaje con esa variable nueva .

def tiene_uno(expresion):
    texto = str(expresion)
    n = len(texto)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if texto[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
#Ejercicio 3.8. Función suma()
#Comentario: El error es error semántico.
# El error era que no se estaba retornando el resultado de c por lo cual al ejecutar la funcion esta no devolvia nada.
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
#print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.9. leer_camion()
#Comentario: El error es error semántico.
# El error era que la variable registro tiene que estar creada dentro del bucle for para que por cada fila se formatee el diccionario
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion(r"./Data/camion.csv")
pprint(camion)
