def generar_espiral(n):
    matriz = [[0] * n for _ in range(n)]

    izquierda, derecha = 0, n - 1
    arriba, abajo = 0, n - 1
    num = 1

    while izquierda <= derecha and arriba <= abajo:

        for i in range(izquierda, derecha + 1):
            matriz[arriba][i] = num
            num += 1
        arriba += 1

        for i in range(arriba, abajo + 1):
            matriz[i][derecha] = num
            num += 1
        derecha -= 1

        for i in range(derecha, izquierda - 1, -1):
            matriz[abajo][i] = num
            num += 1
        abajo -= 1

        for i in range(abajo, arriba - 1, -1):
            matriz[i][izquierda] = num
            num += 1
        izquierda += 1

    return matriz


def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()



n = int(input("Introduce un número entero n (mayor o igual a 3): "))
if n < 3:
    print("El número debe ser mayor o igual a 3.")
else:
    matriz = generar_espiral(n)
    imprimir_matriz(matriz)

