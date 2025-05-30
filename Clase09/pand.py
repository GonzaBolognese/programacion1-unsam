import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

df_jacarandas = df[df['nombre_com']=='Jacarandá']
jacarandas_head = df_jacarandas.head(5)
jacarandas_tail = df_jacarandas.tail(10)
jacarandas_info = df_jacarandas.describe()
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
jacarandas_info = df_jacarandas.describe()
cant_ejemplares = df['nombre_com'].value_counts()

# sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')
# plt.show()

#print(df_jacarandas.iloc[0:3,0:2])
# print(pd.date_range('20200923', periods = 7))
# print(pd.date_range('20200923 14:00', periods = 6, freq = 'H'))


#-------Caminatas al azar----------
# idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
# s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
# s2 = s1.cumsum()
# w = 5 # ancho en minutos de la ventana
# s3 = s2.rolling(w,min_periods = 1).mean()
# df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
# df_series_23.plot()
# plt.show()

#--------12 personas caminando 8 horas-----------
horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']
df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()
w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()
df_walk_suav.to_csv('caminata_apostolica.csv')