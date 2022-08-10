# This programa is a simple calculator

print('''
      Bienvenido a la calculadora

      **********************
      1. suma              *
      2. resta             *
      2. resta             *
      3. multiplicacion    *
      4. division          *
      5. potencia cuadrada *
      **********************

      ''') # Este es el menu de la calculadora

opcion = input('por favor seleccione el tipo de operacion que desea realizar: ')

if (opcion == '1'):
    n1 = float(input("Ingrese el 1er numero: "))
    n2 = float(input("Ingrese el 2do numero: "))
    suma = n1 + n2
    print("La suma de", n1, '+', n2, 'es', suma)
elif (opcion == '2'):
    n1 = float(input("Ingrese el 1er numero: "))
    n2 = float(input("Ingrese el 2do numero: "))
    resta = n1 - n2
    print("La resta de", n1, '-', n2, 'es', resta)
elif (opcion == '3'):
    n1 = float(input("Ingrese el 1er numero: "))
    n2 = float(input("Ingrese el 2do numero: "))
    multiplicacion = n1 * n2
    print("La multiplicacion de", n1, '*', n2, 'es', multiplicacion)
elif (opcion == '4'):
    n1 = float(input("Ingrese el 1er numero: "))
    n2 = float(input("Ingrese el 2do numero: "))
    if (n2 == 0):
        print("Error, no se puede dividir entre 0")
        exit()
    division = n1 / n2
    print("La division de", n1, '/', n2, 'es', division)
elif (opcion == '5'):
    n1 = float(input("Ingrese el numero que quiere elevar al cuadrado: "))
    potencia = n1 ** 2
    print("La potencia cuadrada de", n1, '^', 2, 'es', potencia)
else:
    print("Error, no selecciono una opcion valida")


