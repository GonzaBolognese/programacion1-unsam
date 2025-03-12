cadena = 'Geringoso'
vocales = 'aeiouAEIOU'
capadepenapa = ''
for c in cadena:
    capadepenapa += c
    if c in vocales:
        capadepenapa += 'p' + c
print(capadepenapa)