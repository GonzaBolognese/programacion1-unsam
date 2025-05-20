import random
N = 1000000

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada

def es_generala(tirada):
    return max(tirada) == min(tirada)

def prob_generala(n):
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

def prob_estad_gener():
    print(round((1/6)**4, 6))

def prob_generala(N)

prob_generala(N)
prob_estad_gener()