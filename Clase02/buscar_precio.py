def buscar_precio(fruta):
    try:
        ruta = r"C:\Users\gonza\OneDrive\Escritorio\Programacion_1\Ejercicios\programacion1-unsam\data\precios.csv"
        f = open(ruta, "rt")
        data = f.read()
        arr = data.split("\n")
        text = f'{fruta} no figura en el listado de precios.'
        for s in arr:
            if(fruta in s):
                text=f'El precio de un cajón de {fruta} es: {s.split(",")[1]}'
        print(text)
    except:
        print('El valor ingresado debe ser un texto')
    

buscar_precio("Frambuesa")
buscar_precio("Banana")
buscar_precio("Melon")
buscar_precio(4)

