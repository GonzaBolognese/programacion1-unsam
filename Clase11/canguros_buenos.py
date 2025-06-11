class Canguro:
    """Un Canguro es un marsupial."""
    # El problema se encuentra en la definición del método __init__.
    # def __init__(self, nombre, contenido=[]):
    # El valor por defecto para un parámetro de una función se crea por unica vez,
    # cuando la función es definida, no cada vez que es llamada.
    def __init__(self, nombre, contenido=None):
        """Inicializa un canguro.

        nombre: string
        contenido: lista con el contenido inicial del marsupio.
                   Si no se provee, se crea una lista vacía.
        """
        self.nombre = nombre
        if contenido is None:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido

    def __str__(self):
        """Devuelve una representación como cadena de este Canguro."""
        t = [f'{self.nombre} tiene en su marsupio:']
        for obj in self.contenido_marsupio:
            # Usamos str(obj) para obtener la representación de cada objeto,
            # lo que llamará al método __str__ del objeto si lo tiene.
            s = f'    {str(obj)}'
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)


print(madre_canguro)
print('---')
print(cangurito)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.