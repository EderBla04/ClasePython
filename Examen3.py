#Escribe un programa que reduzca un número a un solo dígito sumando repetidamente sus dígitos.

#Instrucciones:
#- Pedir al usuario un número entero positivo.
#- Sumar sus dígitos hasta que quede un solo número.

num = int(input("Ingrese un numero entero: "))

suma = 0

while num > 9:
    suma = 0
    while num > 0:
        suma += num % 10
        num //= 10
    num = suma


print("El numero reducido a un solo digito es: ", num)