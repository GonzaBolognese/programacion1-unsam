class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.
        '''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.
        '''
        return len(self.items) == 0


class TorreDeControl:
    """
    Modela una torre de control de un aeropuerto con una pista,
    gestionando colas para aterrizajes y despegues.
    """

    def __init__(self):
        """
        Inicializa la torre de control con dos colas vacías:
        una para arribos y otra para partidas.
        """
        self.arribos = Cola()
        self.partidas = Cola()

    def nuevo_arribo(self, vuelo):
        """
        Agrega un vuelo a la cola de aterrizajes (arribos).
        """
        self.arribos.encolar(vuelo)

    def nueva_partida(self, vuelo):
        """
        Agrega un vuelo a la cola de despegues (partidas).
        """
        self.partidas.encolar(vuelo)

    def ver_estado(self):
        """
        Imprime el estado actual de ambas colas.
        """
        arribos_str = ', '.join(self.arribos.items)
        partidas_str = ', '.join(self.partidas.items)
        
        print(f'Vuelos esperando para aterrizar: {arribos_str}')
        print(f'Vuelos esperando para despegar: {partidas_str}')

    def asignar_pista(self):
        """
        Asigna la pista al próximo vuelo según la prioridad:
        primero los aterrizajes, luego los despegues.
        """
        if not self.arribos.esta_vacia():
            vuelo = self.arribos.desencolar()
            print(f'El vuelo {vuelo} aterrizó con éxito.')
        elif not self.partidas.esta_vacia():
            vuelo = self.partidas.desencolar()
            print(f'El vuelo {vuelo} despegó con éxito.')
        else:
            print('No hay vuelos en espera.')