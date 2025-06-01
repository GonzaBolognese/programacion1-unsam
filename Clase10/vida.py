import datetime

def vida_en_segundos(fecha_nac):
    fecha_hora = datetime.datetime.now()
    hoy_seg = fecha_hora.timestamp()
    nacimiento = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y').timestamp()

    print(hoy_seg)
    print(nacimiento)
    print('-------------------------------------')
    print(hoy_seg-nacimiento)

vida_en_segundos('17/03/2000')