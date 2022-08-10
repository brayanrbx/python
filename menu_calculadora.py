# This program realizes a menu with the following options:

print("""
      Bienvenido a la calculadora                __________
                                                | ________ |
      **********************                    |\"\"\"\"\"\"\"\"""|
      1. suma              *                    |[M|#|C][-]|
      2. resta             *                    |[7|8|9][+]|
      2. resta             *                    |[4|5|6][x]|
      3. multiplicacion    *                    |[1|2|3][%]|
      4. division          *                    |[.|O|:][=]|
      5. potencia cuadrada *                    "----------"  hjw
      **********************

      """) # Este es el menu de la calculadora
opcion = input('por favor seleccione el tipo de operacion que desea realizar: ')

"""
    dependiendo de la opción  se realizara un tipo
    operacion en particular, las cuales son establecidas
    mediante el uso del if y elif
    """
    
if (opcion == '1'):
    n1 = float(input("Ingrese el 1er numero: "))
    n2 = float(input("Ingrese el 2do numero: "))
    suma = n1 + n2  #con esta linea se realiza la suma de los dos numeros ingresados
    print("La suma de", n1, '+', n2, 'es', suma)
elif (opcion == '2'):
    n1 = float(input("Ingrese el 1er numero: "))
    n2 = float(input("Ingrese el 2do numero: "))
    resta = n1 - n2  #con esta linea se realiza la resta de los dos numeros ingresados
    print("La resta de", n1, '-', n2, 'es', resta)
elif (opcion == '3'):
    n1 = float(input("Ingrese el 1er numero: "))
    n2 = float(input("Ingrese el 2do numero: "))
    multiplicacion = n1 * n2  #con esta linea se realiza la multiplicacion de los dos numeros ingresados
    print("La multiplicacion de", n1, '*', n2, 'es', multiplicacion)
elif (opcion == '4'):
    n1 = float(input("Ingrese el 1er numero: "))
    n2 = float(input("Ingrese el 2do numero: "))
    if (n2 == 0): #con esta linea se crea la condicion que no permite dividir entre 0
        print("Error, no se puede dividir entre 0")
        exit()
    division = n1 / n2  #con esta linea se realiza la division de los dos numeros ingresados
    print("La division de", n1, '/', n2, 'es', division)
elif (opcion == '5'):
    n1 = float(input("Ingrese el numero que quiere elevar al cuadrado: "))
    potencia = n1 ** 2  #con esta linea se eleva al cuadrado el numero ingresado
    print("La potencia cuadrada de", n1, '^', 2, 'es', potencia)
else:
    print("Error, no selecciono una opcion valida")


