listaDeNumeros = []

for i in range(5):

    listaDeNumeros.append(int(input(f"Ingrese el numero {i+1}:")))




try:

    indice = int(input("Ingrese el indice del numero: "))

    print(listaDeNumeros[indice-1])

except IndexError:
    print("No existe")

