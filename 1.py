'''

Crea Un programa que seleccione Un
númera secreto aleatorio entre 1 y
20 utilizando la función random. randrange(). El usuario deberá adivinar
el numero, y el programa dara pistas indicando si el númere ingresado es
mayor o menor que el numerg secreto. El usuario tiene un máximo de 5 intentos


Pasos para implementar el prograna
iuporta random
Usa random. randrange(1, 20) para generar un númere aleatorio entre 1 y 21
Solicita al usuario un númerg e indica si es mayor o menor que el número
Permite un mdximo de 5 intentos para adivinar el numerg
Si el usuario adivina correctamente, felicitalo
usuario no adivina en 5 intentos, revela el número secreto

'''

import random

intentos = 0

numero_secreto = random.randint(1, 21)

gano = False

while (intentos < 5):

    numero = int(input("Ingresa el numero:"))

    if (numero == numero_secreto):
        print("EXCELENTE")
        gano = True
        break

    elif (numero > numero_secreto):
        print("Es menor")

    elif (numero < numero_secreto):
        print("Es mayor")

    intentos += 1

if (gano == False):
    print("Perdiste")