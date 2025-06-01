import datetime

def dia_reincorporación (fecha_inicio):
    inicio = datetime.datetime.strptime(fecha_inicio, '%d/%m/%Y')
    inicio = inicio.date()
    duracion_licencia = datetime.timedelta(days=200)
    reincoporación = inicio + duracion_licencia
    print(reincoporación)


dia_reincorporación('26/09/2020')