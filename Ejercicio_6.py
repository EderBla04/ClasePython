#Ejercicio 1
#Solicitar al usuario un texto e imprimir al reves

texto=input("1.- Introduzca una cadena de caracteres")
print(texto[::-1])

#Ejercicio 2
#Pedir al usuario una frase
#Pedir al usuario una palabra para reemplazar
#Pedir al usuario una nueva palabra
#Mostrar el resulado del reemplazo

frase=input("2.- Dame una frase bro")
palabraog=input("Dame una palabra vieja a reemplazar:")
palabranew=input("Dame la palabra para sustituir")
print(frase.replace(palabraog, palabranew))

#Ejercicio 3
#Pedir al usuario una cadena
#Pedir un entero
#Imprimir esa palabra el numero de veces que el usuario ingreso
texto=input("3.- Dame una cadena: ")
n=int(input("Dame un numero entero: "))
print(texto * n)