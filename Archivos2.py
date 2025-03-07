import csv

with open ("Iris.csv", "r") as archivo:

    lector = csv.reader(archivo) #
    for fila in lector:
        print(fila)


with open("Iris.csv", "r" ) as archivo:

    lector = csv.reader(archivo)
    encabezado = next(lector)
    datos = list(lector)

    print("Encabezado: ", encabezado)
    print("Primeras filas", datos)