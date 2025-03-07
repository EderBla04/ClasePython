#Escribe un programa que convierta un número entre 1 y 99 en su representación en palabras.
#Instrucciones:
#- Pedir al usuario un número entre 1 y 99.
#- Convertirlo a su forma escrita en español.

numero = int(input("Ingrese un numero entre 1 y 99: "))

unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"]

decenas = ["", "treinta y", "cuarenta y", "cincuenta y", "sesenta y", "setenta y", "ochenta y", "noventa y"]

especiales = ["veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

especiales2 = ["once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]

especiales3 = ["veintiuno", "veintidos", "veintitres", "veinticuatro", "veinticinco", "veintiseis", "veintisiete", "veintiocho", "veintinueve"]



if numero < 11:
    print(unidades[numero])

elif numero % 10 ==0:

    print(especiales[numero // 10 - 2])

else:
    if numero < 20:
        print(especiales2[numero - 11])

    elif numero < 30:
        print(especiales3[numero - 21])

    else:
        print(decenas[numero // 10 - 2], unidades[numero % 10])