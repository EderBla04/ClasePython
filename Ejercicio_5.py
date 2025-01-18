#E J E R C I C I O S

import math

#EJercicio 1
#Comversion de unidades de tiempo
#Crear un programa que solicite una cantidad de segundos y
#la convierta en horas, minutos y segundos. Por ejemplo:

print("-------Ejercicio 1-------")

segundos = int(input("Ingrese la cantidad de segundos: "))

dias = segundos // 86400
horas = (segundos % 86400) // 3600
minutos = ((segundos % 86400) % 3600) // 60
segundos = ((segundos % 86400) % 3600) % 60


print(dias, "dias", horas, "horas", minutos, "minutos", segundos, "segundos")

print("-------Ejercicio 2-------")
#Ejercicio 2
#Calculadora de IMC
#Pedir al usuario su peso(kg) y estatura(cm)
#Calcular el IMC usando la formula e imprimirlo

peso = float(input("Ingrese su peso en kg: "))
estatura = int(input("Ingrese su estatura en cm: "))

print("Su IMC es: ", peso / ((estatura/100)**2))

print("-------Ejercicio 3-------")

#Ejercicio 3
#Calculo de imterese compuesto
#Pedir al usuaario el capital inicial, la tasa de interes
#y el numero de años, luego calcular
#el interes compuesto usando la formula e imprimirlo

p= float(input("Ingrese el capital inicial: "))
r= float(input("Ingrese la tasa de interes: "))
t= int(input("Ingrese el numero de años: "))

print("El interes compuesto es: ", p*(1+r)**t)

print("-------Ejercicio 4-------")

#Ejercicio 4
#Resolucion  de ecuacion cuadritica
#Solicitar a, b, c para resolver usando la formula
#imprimir ambas soluciones

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print("Las soluciones son: ", x1, " ",x2)

