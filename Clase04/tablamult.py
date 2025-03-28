def ver_tablas():
    headers = [f'{"":>7s}',f'{"-----"}']
    tablas = []
    
    for n in range(10):
        headers[0] += f'{n:<4d}'
        headers[1] += f'{"----"}' 
        tab = [f'{n}:']
        for m in range(10):
            tab.append(n*m)
        tablas.append(tab)

    for h in headers:
        print(h)
    for t in tablas:
        i = 0
        text = f''
        for n in t:
            if i == 0:
                text += f'{n:^4s}'
            else:
                text += f'{n:>4d}'
            i +=1
        print(text)

ver_tablas()