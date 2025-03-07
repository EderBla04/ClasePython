import csv

suma = 0
contador = 0
promedio = 0
with open('Iris.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    next(lector)


    for fila in lector:
        suma += float(fila[1])
        contador += 1


promedio = suma / contador

print(promedio)

