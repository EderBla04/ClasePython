lista = []

mayor=0
cont = 0
while cont < 15:
    lista.append(int(input("Ingrese un numero: ")))
    cont += 1

lista.sort()
print(lista)

media = sum(lista) / len(lista)

print("La media es: ", media)

mediana = lista[len(lista) // 2]

print("La mediana es: ", mediana)

contPrimos = 0

for i in lista:

    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0:
            break

    else:
        contPrimos += 1


print("La cantidad de numeros primos es: ", contPrimos)


numeroRepetido = max(set(lista), key = lista.count)

print("El numero que mas se repite es: ", numeroRepetido)

sinRepetir = []

for i in lista:

    if i not in sinRepetir:
        sinRepetir.append(i)


print("Los numeros sin repetir son: ", sinRepetir)

