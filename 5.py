import csv

from Ejercicio_2 import promedio

with open('Iris.csv', 'r') as archivo_entrada:
    lector = csv.reader(archivo_entrada)
    encabezado = next(lector)

    filas_setosa = []

    for fila in lector:
        if fila[-1] == "Iris-setosa":
            filas_setosa.append(fila)

with open('Iris-setosa.csv', 'w', newline="") as archivo_salida:
    escritor = csv.writer(archivo_salida)
    escritor.writerow(encabezado)
    escritor.writerows(filas_setosa)

print(f"Se guaradaron {len(filas_setosa)} filas en Iris-setosa.csv")



