import os
import re

print("Bienvenido al sistema de ubicacion para zonas publicas WIFI")
user = "51606" # Usuario para ingresar
password = "60615" # Contraseña de ingreso
print("Para acceder por favor digite como usuario:", user, " y como contraseña:", password)
n_user = input("Digite su nombre de usuario: ") # variable para guardar el usuario ingresado

# condicional para verificar que el usuario ingresado coincida con el usuario registrado
if (n_user != user):
    print("Error", "debe ingresar un usuario valido")
    exit()
else:
    print("user successful")

n_pass = input("Digite su contraseña: ") # variable para guardar la contraseña ingresada

# condicional para verificar que la contraseña ingresada coincida con la contraseña registrada
if (n_pass != password):
    print("Error", "debe ingresar una contraseña correcta")
    exit()
else:
    print("password successful")

# codigo de seguridad para poder iniciar sesion
n1 = 606
n2 = ((6 * 0 + 6) + (6 * 6 - 0)) * 0
print("Para continuar ingrese el valor del codigo de seguridad ", n1, "+", n2, "=", end=" ")
catpcha = int(input())

# condicional para verificar el codigo de seguridad
if (catpcha == (n1 + n2)):
    print("Sesión iniciada")
else:
    print("Error, el codigo de seguridad ingresado es incorrecto")

os.system("cls") # borrar la pantalla

def menu(a):
    """[funcion que permite recorrer una lista e imprimirla con us indices]

    Args:
        a (list): [opciones para un menu]
    """
    for i in range(0, len(a)):
        print(i + 1, '.', a[i])

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

def cambio_password(a):
    """[funcion para realizar el cambio de contraseña]

    Args:
        a ([str]): [se ingresa un string que tiene almacenada la variable a cambiar]

    Returns:
        [str]: [se retorna el string donde esta almacenada la nueva contraseña]
    """
    confirmacion = input("Digite la contraseña actual: ")
    if (confirmacion == a):
        newpassword = input("Ingrese su nueva contraseña: ")
        if (newpassword == a):
            print("Error, Esa contraseña ya existe")
            exit()
        else:
            a = newpassword
            return a
    else:
        print("Error, esa no es la contraseña actual")
        exit()

def validation_float():
    """[funcion para validar el tipo de dato ingresado por el usuario]

    Returns:
        [float]: [si es posible la conversion se retorna un float]
    """
    while True:
        num_format = re.compile("^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$")
        entrada = input("ingrese un numero: ")
        if num_format.match(entrada) == None:
            print("La opción que ingreso no es un numero")
            print("vuelva y digite un numero")
        elif (entrada == ""):
                print("Error")
                exit()
        else:
            flotante = float(entrada)
            return flotante

def coordenadas(b):
    """[funcion para ingresar las coordenadas]

    Args:
        b ([list]): [lista vacia que se llenara por medio de esta funcion]
    """
    for i in range(3):
        if (i == 0):
            b.append([])
            print("Introduce las coordenadas de la casa")
        if (i == 1):
            print("Introduce las coordenadas del trabajo")
            b.append([])
        if (i == 2):
            print("Introduce las coordenadas del parque")
            b.append([])
        for j in range(2):
            if (j == 0):
                print("Las coordenadas para latitud deben estar en el rango Sup: -3.002 hasta Inf:-4.227")
                print("Introduce las coordenadas de latitud: ", end="")
                latitud = validation_float()
                if (latitud < -4.227) or (latitud > -3.002):
                    print("Error coordenada")
                    exit()
                else:
                    latitud = float("{0:.3f}".format(latitud))
                    temp = latitud
            if (j == 1):
                print("Las coordenadas para longitud deben estar en el rango Or:-69.714 hasta Occ:-70.365")
                print("Introduce las coordenadas de longitud: ", end="")
                longitud = validation_float()
                if (longitud < -70.365) or (longitud > -69.714):
                    print("Error coordenada")
                    exit()
                else:
                    longitud = round(longitud, 3)
                    b[i].append(str((temp)))
                    b[i].append(str(longitud))

def show_coordenadas(c):
    """[funcion para mostrar las coordenadas actuales]

    Args:
        c ([list]): [se recibe la lista con las coordenadas actuales]
    """
    for i in range(len(c)):
        print("coordenada [latitud,longitud] {} : {}".format((i + 1), c[i]))

def new_coordenadas():
    """[funcion para actualizar las coordenadas actuales]

    Returns:
        [float]: [se retornan 2 float al final de la funcion]
    """
    print("Las coordenadas para latitud deben estar en el rango Sup: -3.002 hasta Inf:-4.227")
    print("Ingrese las nuevas coordenadas para latitud: ", end="")
    latitud = validation_float()
    if (latitud < -4.227) or (latitud > -3.002):
        print("Error coordenada")
        exit()
    else:
        latitud = float("{0:.3f}".format(latitud))
        temp = latitud
    print("Las coordenadas para longitud deben estar en el rango Or:-69.714 hasta Occ:-70.365")
    print("Ingrese las nuevas coordenadas para longitud: ", end="")
    longitud = validation_float()
    if (longitud < -70.365) or (longitud > -69.714):
        print("Error coordenada")
        exit()
    else:
        longitud = round(longitud, 3)
        temp1 = longitud
        return temp, temp1

def update_coordenadas(c):
    """[funcion para actualizar una de las coordenadas actuales]

    Args:
        c ([list]): [se ingresa una lista con las coordenadas actuales]
    """
    print("la coordenada 1 es la que esta más al sur")
    print("la coordenada 2 es la que esta más al occidente")
    print("presione 1, 2 o 3 para actualizar la respectiva coordenada")
    print("presiones 0 para regresar al menu")
    seleccion = input()
    if (seleccion == '0'):
        pass
    elif (seleccion == '1'):
        print("ha seleccionado actualizar las coordenadas de la casa")
        new_latitud, new_longitud = new_coordenadas()
        c[0][0] = str(new_latitud)
        c[0][1] = str(new_longitud)
    elif (seleccion == '2'):
        print("ha seleccionado actualizar las coordenadas del trabajo")
        new_latitud, new_longitud = new_coordenadas()
        c[1][0] = str(new_latitud)
        c[1][1] = str(new_longitud)
    elif (seleccion == '3'):
        print("ha seleccionado actualizar las coordenadas del parque")
        new_latitud, new_longitud = new_coordenadas()
        c[2][0] = str(new_latitud)
        c[2][1] = str(new_longitud)
    else:
        print("Error actualización")
        exit()

# lista de opciones para el menu
option = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona WIFI mas cercana",
        "Guardar archivo con ubicacion cercana", "Actualizar registros de zonas WIFI desde archivos",
        "Elegir opcion de menu favorita", "Cerrar sesion"]

coordenada = [] # lista vacia para ingresar las coordenadas
n = True # variable para controlar si el usuario ya ha ingresado las coordenadas

# ciclo para visualizar el menu hasta que el usuario decida cerrar sesion
while True:
    menu(option)
    print("Seleccione una de las opciones del menu: ", end="")
    opcion = validacion_int()
    cont = 3
    while (opcion < 1) or (opcion > 7):
        if (cont == 0):
            print(f"Error tus intentos restantes son {cont}")
            exit()
        print(f"Error, opcion invalida, te quedan {cont} intentos")
        print("Seleccione una opcion: ", end="")
        opcion = validacion_int()
        cont -= 1
    if ((opcion - 1) == option.index("Cambiar contraseña")):
        password = cambio_password(password)
    elif ((opcion - 1) == option.index("Ingresar coordenadas actuales")):
        if (n == True):
            print("Debe ingresar las coordenadas actuales")
            coordenadas(coordenada)
            n = False
        else:
            show_coordenadas(coordenada)
            update_coordenadas(coordenada)
    elif ((opcion - 1) == option.index("Ubicar zona WIFI mas cercana")):
        print("Usted ha elegido la opción 4")
        exit()
    elif ((opcion - 1) == option.index("Guardar archivo con ubicacion cercana")):
        print("Usted ha elegido la opción 4")
        exit()
    elif ((opcion - 1) == option.index("Actualizar registros de zonas WIFI desde archivos")):
        print("Usted ha elegido la opción 5")
        exit()
    elif (opcion == 6):
        print("Por favor seleccione una opcion del 1-5 como favorito: ", end="")
        favorite = validacion_int()
        if (favorite < 1) or (favorite > 5):
            print("Error, ha ingresado una opcion invalida")
            exit()
        else:
            print("para confirmar la seleccion debera responder las siguientes preguntas")
            print("Antes era un ocho pero perdi mi parte superior, la respuesta es: ", end="")
            n1 = validacion_int()
            if (n1 != 0):
                print("Error, respuesta incorrecta")
            else:
                print("Soy hermano del nueve pero siempre mi cabeza mira al piso, la respuesta es: ", end="")
                n2 = validacion_int()
                if (n2 != 6):
                    print("Error, respuesta incorrecta")
                else:
                    temp = option[favorite - 1]
                    option.remove(option[favorite - 1])
                    option.insert(0, temp)
                    os.system("cls")
    elif (opcion == 7):
        print("has seleccionado cerrar sesion")
        print("Hasta pronto")
        exit()




