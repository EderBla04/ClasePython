def saludar():

    print("¡Hola, bienvenido a la clase de Python!")



saludar()


def saludarPersona(nombre):

    print(f"Hola, {nombre}")


saludarPersona("Gael")

def suma(a, b):

    return a+b

resultado = suma(3, 4)

print(resultado)


'Ejemplos com args'

def sumar (*args):

    return sum(args)

print(sumar(1, 2, 3, 4))


f = lambda x,y : x + y

print(f(3, 4))