

try:

    a = int(input("Numero 1:"))
    b = int(input("Numero 2: "))

    resultado = a/b

    print(f"Resulado : {resultado}")

except ValueError:
    print("Erro: debes ingresar un numero valido")

except ZeroDivisionError:
    print("No puedes dividir entre 0")






