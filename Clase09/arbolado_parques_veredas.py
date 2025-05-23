import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]
frecuencia = df_lineal['nombre_cientifico'].value_counts()
top_10_frecuencia = frecuencia.head(10)

#Top 10 arboles mas frecuentes
#print(top_10_frecuencia)

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

#Boxplot diametro_altura_pecho
# df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
# plt.suptitle('')
# plt.title('Diametro pecho')
# plt.show()

#Boxplot altura_arbol
# df_lineal_seleccion.boxplot('altura_arbol', by= 'nombre_cientifico') #Con pandas
# sns.boxplot(data= df_lineal_seleccion, x='nombre_cientifico', y='altura_arbol') #Con Seaborn
# plt.suptitle('')
# plt.title('Altura_arboles')
# plt.show()

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
plt.show()