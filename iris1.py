import csv

with open("Iris.csv", "r") as archivo_entrada:
    lector = csv.reader(archivo_entrada)
    encabezado = next(lector)


    filas_setosa = [fila for fila in lector if fila[-1] == "Iris-setosa"]

   # filas_setosa = [] #lista vacia para guardar las filas de la especie "setas setosas
    #with open("iris.csv", "r") as archivo_entrada:
     #   for fila in lector:
      #      if fila[-1] == "Iris-setosa": #si la especie es "setosa
       #         filas_setosa.append(fila) #agregar la fila a la lista


with open("Iris-setosa.csv", "w", newline="") as archivo_salida:
    escritor = csv.writer(archivo_salida)
    escritor.writerow(encabezado)
    escritor.writerows(filas_setosa)

    print(f"Se guardaron {len(filas_setosa)} filas en 'Iris-setosa.csv'.")






