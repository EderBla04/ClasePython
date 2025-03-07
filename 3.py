lista = []

i=0

while i< 10:

    lista.append(int(input("Ingrese un numero: ")))
    i+=1


print(lista)

print("La suma es: ", sum(lista))

print("El promedio es: ", (sum(lista)/ len(lista)))

print("EL numero mayor es: ", max(lista))

print("EL numero menor es: ", min(lista))