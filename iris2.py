import csv



prom=0

with open("Iris.csv", "r") as archivo_entrada:
    lector = csv.reader(archivo_entrada)
    next(lector)

    cont = 0

    for fila in lector:
        prom += float(fila[1])
        cont += 1

prom = prom/cont

print("Contador: ", cont)
print("promedio: ", prom)
