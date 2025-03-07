lista = []

n = int(input("Ingrese cuantos numeros quiere: "))

for i in range(n):
    num = int(input("Ingrese un numero: "))
    lista.append(num)

lista.sort()

print(lista)

print("La suma es: ", sum(lista))

print("El promedio es: ", (sum(lista)/ len(lista)))

print("El tamaño es: ", len(lista))

print("EL numero mayo es: ", max(lista))

print("EL numero menos es: ", min(lista))