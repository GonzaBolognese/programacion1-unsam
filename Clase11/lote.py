import fileparse
import os
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = int(cajones)
        self.precio = float(precio)

    def costo (self):
        return self.cajones*self.precio
    
    def vender(self, cant):
        self.cajones -= cant
        return self.cajones
    
    def __str__(self):
        return f'({self.nombre}, {self.cajones}, {self.precio})'
    
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'

def lista_lotes (ruta):
    with open(ruta) as lineas:
        camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion

directorio = './Data'
archivo = 'camion.csv'
fname = os.path.join(directorio,archivo)
camion = lista_lotes(fname)