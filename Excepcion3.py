from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

try:
    archivo = open("archivo.txt")
    contenido = archivo.read()

except FileNotFoundError:
    print("Error: El archivo no existe")

finally:
    print("Finalizando operacion")


 try:
    numero = int(input("Introduce un numero: "))

 except ValueError:
     print("Error :No ingresesre un numero.")

 else:
     print(f)


