archivo = open("datos.txt", "r")

contenido = archivo.read() #Lee todo el contenido del archivo

print(contenido)

archivo.close() #Cierra el archivo


archivo = open("datos.txt", "r")

linea = archivo.readline() #Lee una linea del archivo
print(linea)
archivo.close()

archivo = open("datos.txt", "r")
lineas= archivo.readlines() #Lee todas las lineas del archivo
print(lineas)
archivo.close()

with open ("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)