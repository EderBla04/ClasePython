'''

Crea un programa que permite al usuario una lista de compras con
las siguientes funciones:

Agregar un producto a la lista
Eliminar un producto a la lista
Mostrar la lista actualizada
Salir del programa


'''

lista = []



while True:

    print("1. Agregar un producto a la lista")
    print("2. Eliminar un producto a la lista")
    print("3. Mostrar la lista actualizada")
    print("4. Salir del programa")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        lista.append(input("Ingrese un producto: "))

    elif opcion == "2":
        lista.remove((input("Ingrese el numero del producto: ")))

    elif opcion == "3":
        print(lista)

    else:
        break