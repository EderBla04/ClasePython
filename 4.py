import csv

with open('iris.csv', 'r') as archivo:

    contenido = archivo.read()
    print(contenido)


print("------------")

with open('iris.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    datos = list(lector)
    print(encabezado)
    print(datos[5])

