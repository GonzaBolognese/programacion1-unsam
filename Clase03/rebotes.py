import sys

if len(sys.argv) == 1:
    altura = 100
else:
    altura = int(sys.argv[1])

rebotes = 1

while rebotes<=10:
    altura = altura * (3/5)
    print(round(altura, 2))
    rebotes +=1