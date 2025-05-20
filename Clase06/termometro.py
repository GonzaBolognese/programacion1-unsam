import random
import numpy as np

def medir_temp(n):
    mediciones = np.zeros(n)
    resumen = []
    for i in range(n):
        medicion = round(random.normalvariate(37.5,0.2),2)
        mediciones[i-1] = medicion
        resumen.append(medicion)
    np.savetxt('./Data/temperaturas.npy', mediciones)
    return resumen

def resumen_temp(n):
    mediciones = medir_temp(n)
    print(mediciones)
    return (max(mediciones), 
            min(mediciones), 
            round(sum(mediciones)/n,2),
            mediciones[n//2],
            mediciones[(n//2)//2],
            mediciones[(n//2) + (n//2)//2])


#print(round(random.normalvariate(37.5,0.2),2))
#print(medir_temp(10))
print(resumen_temp(999))

    