 #Manejo de cadenas En python las cadenas son inmutables
 #Por lo cual una vez declaradas
 #no se pueden modificar
 #Las cadenas se pueden trabajar como
 #Una lista de caracteres

Cadena = "Hola Mundo"
print(Cadena[0])
print(Cadena[-1]) #Recordar accede al ultimo elemento

#Metodos comunes para cadenas

#A. Cambiar el formato del texto
#1. upper(): Convierte el texto a mayusculas
#2. lower(): Convierte el texto a minusculas
#3. capitalize(): Convierte la primera letra en mayuscula
#4. title(): Convierte la primera letra de cada palabra en mayuscula
#5 strip(): Elimina los espacios en blanco al inicio y al final

cadena = "  hola Python  "
print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print(cadena.title())
print(cadena.strip())

#B: Reemplazar texto:
#1. replace(old, new): Reemplaza toda la ocurrencia de old por new
texto = "hola mundo hola"
print(texto.replace("hola", "Python"))

#C: Buscar y contar texto
#1. find(sub): Devuelva el indice
# donde comienza

#sub (0 -1 si no se encuentra)
#2. count(sub): Devuelve el numero de veces que se encuentra sub

texto = "Python es genial. Python es facil"
print(texto.find("hola")) 
print(texto.count("Python"))






