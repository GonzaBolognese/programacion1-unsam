frutas = 'Manzana,naranja,Mandarina,Banana,Kiwi'
frutas += ",Pera"
frutas = "Melon,"+frutas
contiene=frutas[14:21]
letrasA=0
frutas=frutas.replace("Melon", "Sandia")
print(len(frutas))