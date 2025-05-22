import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def multiples_caminos(largo, n):
    '''
    Devuelve n randomwalks en una lista

    pre: Random tiene que ser un numero entero
    Pos: Devuelve una lista con n randomwalks
    '''
    lista = []

    for i in range(n):
        lista[i] = randomwalk(largo)
    return lista




def f_principal(lista):
    fig = plt.figure()
    colores = ['blue', 'orange', 'green', 'red', 'purple', 'brown',
               'pink', 'gray', 'olive', 'cyan', 'black', 'darkcyan']
    plt.subplot(2,1,1)
    for i in range(len(lista)):
        plt.plot(lista[i-1],color=colores[i-1], linewidth=1, linestyle="--")
        
    plt.xticks([],labels='tiempo'), plt.yticks([],labels='distancia al origen')
    plt.show()

if __name__ == '__main__':
    N = 100000
    caminos = multiples_caminos(N, 12)
    f_principal(caminos)