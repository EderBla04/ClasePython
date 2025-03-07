#Escribe un programa que reciba una lista de palabras separadas por comas y las ordene de mayor
#a menor longitud.
#Instrucciones:
#- Pedir al usuario una lista de palabras separadas por comas.
#- Ordenarlas de la más larga a la más corta.
#- Imprimir la lista ordenada.

palabras = input("Ingrese una lista de palabras separadas por comas: ")

listaDePalabras = palabras.split(",")

listaDePalabras.sort(key=len, reverse=True)

print("Lista ordenada de mayor a menor longitud: ", listaDePalabras)

