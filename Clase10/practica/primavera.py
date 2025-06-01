import datetime

def primavera ():
  hoy = datetime.date.today()
  primavera = datetime.date(2025, 9, 21)
  diferencia = primavera - hoy
  return diferencia.days

print(primavera())
