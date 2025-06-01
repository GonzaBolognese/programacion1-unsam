import datetime

def dias_habiles(inicio, fin, feriados):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    fin_de_semana = ["Sábado", "Domingo"]
    inicio = datetime.datetime.strptime(inicio, '%d/%m/%Y').date()
    fin = datetime.datetime.strptime(fin, '%d/%m/%Y').date()
    habiles = 0
    for i in range((fin-inicio).days):
        dia_sumados = datetime.timedelta(days=i+1)
        fecha_string = (inicio+dia_sumados).strftime('%d/%m/%Y')
        dia_semana = (inicio+dia_sumados).weekday()
        if fecha_string not in feriados and dias_semana[dia_semana] not in fin_de_semana:
            habiles += 1
    return habiles
    

dias_habiles('20/09/2020', '31/12/2020', ['12/10/2020', '23/11/2020', '07/12/2020', '08/12/2020', '25/12/2020'])
