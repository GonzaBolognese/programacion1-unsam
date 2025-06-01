import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

directorio = './Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
archivo_vereda = 'arbolado-publico-lineal-2017-2018.csv'

fparques = os.path.join(directorio, archivo_parques)
fvereda = os.path.join(directorio, archivo_vereda)

df_parques = pd.read_csv(fparques)
df_veredas = pd.read_csv(fvereda)

cols_parques = ['altura_tot', 'diametro']
cols_veredas = ['altura_arbol', 'diametro_altura_pecho']

df_tipas_parques = df_parques[df_parques['nombre_cie']=='Tipuana Tipu'].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'].copy()

df_tipas_parques = df_tipas_parques[cols_parques].rename(columns={'altura_tot':'altura'})
df_tipas_veredas = df_tipas_veredas[cols_veredas].rename(columns={'altura_arbol':'altura', 'diametro_altura_pecho': 'diametro'})

df_tipas_parques['ambiente'] = ['parque' for _ in range(len(df_tipas_parques))]
df_tipas_veredas['ambiente'] = ['vereda' for _ in range(len(df_tipas_veredas))]

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura',by = 'ambiente')
#sns.boxplot(data = df_tipas, x = 'ambiente', y = 'diametro')
plt.show()

#print(df_tipas)


