import random
#Ejercicio 1

n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un numero: "))

for i in range(n1, n2 + 1):
    if i % 2 == 0:
        print(i)


#Ejercicio 2
numeroSecreto= random.randint(1, 100)

for i in range(5):
    numero = int(input("Ingrese un numero: "))
    if numeroSecreto > numero: print("El numero secreto es mayor")
    elif numeroSecreto < numero: print("El numero secreto es menor")
    else:
        print("Adivinaste el numero secreto")
        break;



print("El numero secreto es: ", numeroSecreto)