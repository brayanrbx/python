# This program show the use a while loop

import os

def validacion_int():
    """[funcion para validar el tipo dato ingresado por el usuario]

    Returns:
        [int]: [se retorna un entero]
    """
    while True:
        try:
            entero = int(input())
            return entero
        except ValueError:
            print("Error, el valor ingresado no es un numero entero")
            print("vuelva y digite un numero entero")

def validacion_float():
    """[funcion para validar el tipo dato ingresado por el usuario]

    Returns:
        [float]: [se retorna un flotante]
    """
    while True:
        try:
            flotante = float(input())
            return flotante
        except ValueError:
            print("Error, el valor ingresado no es un numero")
            print("vuelva y digite un numero")

while True:
    print("""
      Wavy
       _.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._
     ,'_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._`.
    ( (                                                          ) )
     ) )                    Bienvenido                          ( (
    ( (                                                          ) )
     ) )          Por favor seleccione la opcion                ( (
    ( (                  que desea realizar                      ) )
     ) )                                                        ( (
    ( (           1. Saludar                                     ) )
     ) )          2. Es par                                     ( (
    ( (           3. Promedio                                    ) )
     ) )          4. Módulo                                     ( (
    ( (           5. porcentaje                                  ) )
     ) )          6. Potencia                                   ( (
    ( (           7. Fibonacci                                   ) )
     ) )          0. Salir                                      ( (
    ( (                                                          ) )
     ) )_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.( (
     `._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._,'
    hjw
""")
    print("Ingresa el numero de la opcion que quieres escoger: ", end="")
    opcion = validacion_int()
    if (opcion == 0):
        break
    elif (opcion == 1):
        print("Por favor ingrese la hora en formato de 24 horas "
        "para recibir el saludo correspondiente: ", end="")
        hora = validacion_int()
        if (0 <= hora < 12):
            print("Good morning")
        elif (12 <= hora < 19):
            print("Good afternoon")
        elif (19 <= hora < 24):
            print("Good evening")
        else:
            print("Ha ingresado una hora incorrecta")
    elif (opcion == 2):
        print("Por favor ingrese un numero entero: ", end="")
        numero = validacion_int()
        print(f"El numero {numero} es par" if ((numero % 2) == 0) else f"El numero {numero} es impar")
    elif (opcion == 3):
        print("Por favor ingrese el 1er numero: ", end="")
        n1 = validacion_float()
        print("Por favor ingrese el 2do numero: ", end="")
        n2 = validacion_float()
        print("Por favor ingrese el 3er numero: ", end="")
        n3 = validacion_float()
        print("Por favor ingrese el 4to numero: ", end="")
        n4 = validacion_float()
        print("Por favor ingrese el 5to numero: ", end="")
        n5 = validacion_float()
        promedio = (n1 + n2 + n3 + n4 + n5) / 5
        print("El promedio de los numeros ingresados es:", promedio)
    elif (opcion == 4):
        print("Por favor ingrese el dividendo: ", end="")
        n1 = validacion_float()
        print("Por favor ingrese el divisor: ", end="")
        n2 = validacion_float()
        if (n2 == 0):
            print("Error, No se puede dividir entre 0")
        modulo = (n1 % n2)
        print(f"El modulo de {n1} % {n2} es {modulo}")
    elif (opcion == 5):
        print("Por favor ingrese el numero al que quiere sacarle un porcentaje: ", end="")
        n1 = validacion_float()
        print("Por favor ingrese el valor del porcentaje en un rango de 1-100: ", end="")
        n2 = validacion_float()
        porcentaje = (n2 / 100)
        porcentaje_n1 = (n1 * porcentaje)
        print(f"El {n2}% de {n1} es {porcentaje_n1}")
    elif (opcion == 6):
        print("Por favor ingrese un numero: ", end="")
        n1 = validacion_float()
        print("Por favor ingrese el exponente: ", end="")
        n2 = validacion_float()
        potencia = (n1 ** n2)
        print(f"{n1} ^ {n2} es {potencia}")
    elif (opcion == 7):
        print("Ingrese numero de terminos para la sucesion: ", end="")
        sucesion = validacion_int()
        x, y = 0, 1
        for i in range(sucesion):
            print(x, end=' ')
            x, y = y, x + y
    elif (opcion > 7):
        print("Error, No existe esa opcion")

    input("\nPresione enter para continuar")
    os.system("cls")


