
entrada = input("Ingresa una frase: ")


cont = 0

for i in entrada:
    if i == "A" or i == "a":
        cont+=1
    elif i == "E" or i == "e":
        cont+=1
    elif i == "I" or i == "i":
        cont+=1
    elif i =="O" or i == "o":
        cont+=1
    elif i == "U" or i == "u":
        cont+=1

print("El numero de vocales es: ", cont)


