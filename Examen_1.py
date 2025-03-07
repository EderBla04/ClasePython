#Ejercicio 1

#Escribe un programa que determine si un numero es primo o no

cont = 0

entrada = int(input("Ingresa un numero: "))

if entrada == 0 :
    print("Es primo")
elif entrada == 1:
    print("Es primo")

for i in range(2, entrada):

    if entrada % i == 0:
        cont+=1



if cont <= 2: print("El numero",entrada, "es primo")
else: print("No es primo")