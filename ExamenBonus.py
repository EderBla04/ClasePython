#Descripción:
#Dado un número entero n, generar y mostrar su "secuencia extraña" siguiendo estas reglas:
#- Si n es par, se divide entre 2.
#- Si n es impar, se multiplica por 3 y se suma 1.
#- Se repite el proceso hasta que n sea 1.
#Instrucciones:
#1. Pedir al usuario un número entero positivo.
#2. Mostrar la secuencia generada hasta llegar a 1.

n = int(input("Ingrese un numero entero positivo: "))

while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1


