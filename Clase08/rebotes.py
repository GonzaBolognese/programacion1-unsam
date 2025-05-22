

def rebotar (altura, cant_rebotes):
    rebotes = 1
    while rebotes<=int(cant_rebotes):
        altura = float(altura) * (3/5)
        print(f'{rebotes}: {round(altura, 2)}')
        rebotes +=1


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        rebotar(100, 10)
    elif len(sys.argv) == 2:
            rebotar(sys.argv[1], 10)
    else:
        rebotar(sys.argv[1], sys.argv[2])
