import os
import re
import math

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
        [float]: [se realiza la conversion del dato ingresado y se retorna un float]
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
                    latitud = ("{0:.3f}".format(latitud))
                    temp = latitud
            if (j == 1):
                print("Las coordenadas para longitud deben estar en el rango Or:-69.714 hasta Occ:-70.365")
                print("Introduce las coordenadas de longitud: ", end="")
                longitud = validation_float()
                if (longitud < -70.365) or (longitud > -69.714):
                    print("Error coordenada")
                    exit()
                else:
                    longitud = ("{0:.3f}".format(longitud))
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
        latitud = ("{0:.3f}".format(latitud))
        temp = latitud
    print("Las coordenadas para longitud deben estar en el rango Or:-69.714 hasta Occ:-70.365")
    print("Ingrese las nuevas coordenadas para longitud: ", end="")
    longitud = validation_float()
    if (longitud < -70.365) or (longitud > -69.714):
        print("Error coordenada")
        exit()
    else:
        longitud = ("{0:.3f}".format(longitud))
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

def choose_ubicacion(coordenada, lista_ubicacion):
    """[funcion para elegir elegir la ubicacion actual y obtener las distancias de las zonas wifi mas cercanas]

    Args:
        coordenada ([list]): [lista con las coordenadas actuales]
        lista_ubicacion ([list]): [lista de las coordenadas de las zonas wifi]

    Returns:
        [list]: [se retorna una lista con la ubicacion actual]
    """
    print("por favor elija su ubicación actual (1, 2 o 3) para calcular la distancia"
        "a los puntos de conexion:", end=" ")
    opcion = input()
    if (opcion == '1') or (opcion == '2') or (opcion == '3'):
        ubicacion_actual = coordenada[int(opcion) - 1]
        distances(float(ubicacion_actual[0]), float(ubicacion_actual[1]), lista_ubicacion)
        return ubicacion_actual
    else:
        print("Error ubicación")
        exit()

def distances(x1, y1, lista_ubicacion):
    """[funcion para seleccionar las coordenadas actuales y las coordenadas de las zonas wifi]

    Args:
        x1 ([float]): [float de un elemento de la lista que contiene la latitud]
        y1 ([float]): [float de un elemento de la lista que contiene la longitud]
        lista_ubicacion ([lista]): [lista de las coordenadas de las zonas wifi]
    """
    if (len(lista_ubicacion[0])) < 4:
        for i in range(0, len(lista_ubicacion)):
            lista_ubicacion[i].append(float(calculo_distance(x1, y1, float(lista_ubicacion[i][0]), float(lista_ubicacion[i][1]))))
    else:
        for i in range(0, len(lista_ubicacion)):
            lista_ubicacion[i][3] = float((calculo_distance(x1, y1, float(lista_ubicacion[i][0]), float(lista_ubicacion[i][1]))))

def calculo_distance(lat1, lon1, lat2, lon2):
    """[funcion para realizar el calculo de las distancias de las coordenadas actuales con las de la zona wifi]

    Args:
        lat1 ([float]): [coordenadas de latitud actuales]
        lon1 ([float]): [coordenadas de longitud actuales]
        lat2 ([float]): [coordenadas de latitud zona wifi]
        lon2 ([float]): [coordenadas de longitud zona wifi]

    Returns:
        [float]: [se retorna la distancia calculada]
    """
    rad=math.pi/180
    dlat=lat2-lat1
    dlon=lon2-lon1
    R=6372.795477598
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    distancia *= 1000
    distancia = ("{0:.3f}".format(distancia))
    return distancia

def zonas_wifi(lista_ubicacion):
    """[funcion para ordenar la lista con las distancias por orden de menor usuarios]

    Args:
        lista_ubicacion ([list]): [lista con las coordenadas de la zona wifi, numero de usuarios y distancia]
    """
    lista_ubicacion.sort(key=lambda item: item[3])
    if (lista_ubicacion[1][2] < lista_ubicacion[0][2]):
        lista_ubicacion[0], lista_ubicacion[1] = lista_ubicacion[1], lista_ubicacion[0]

def show_zonawifi(lista_ubicacion):
    """[funcion para mostrar las 2 zonas wifi mas cercanas]

    Args:
        lista_ubicacion ([list]): [lista ordenada con las zonas wifi mas cercanas]
    """
    for i in range(len(lista_ubicacion[0:2])):
        print("La zona wifi {}: ubicada en {} a {} m, tiene en promedio {} usuarios".format((i + 1), [lista_ubicacion[i][0], lista_ubicacion[i][1]], lista_ubicacion[i][3], lista_ubicacion[i][2]))

def calculo_tiempo(distancia):
    """[funcion para calcular el tiempo del medio de transporte]

    Args:
        distancia ([float]): [se ingresan los valores de las distancias calculadas]

    Returns:
        [float]: [se retorna el tiempo calculado para ir en moto y carro]
    """
    velocidad_moto = 19.44
    velocidad_carro = 20.83
    tiempo_moto = (distancia / velocidad_moto) / 60
    tiempo_moto = ("{0:.3f}".format(tiempo_moto))
    tiempo_carro = (distancia / velocidad_carro) / 60
    tiempo_carro = ("{0:.3f}".format(tiempo_carro))
    return tiempo_moto, tiempo_carro

def indicaciones(ubicacion_actual, lista_ubicacion):
    """[funcion que muestra las indicaciones de llegada]

    Args:
        ubicacion_actual ([list]): [lista que contiene la ubicacion actual]
        lista_ubicacion ([list]): [lista ordenada que contiene las coordenadas de la zona wifi]
    """
    op = input("Elija 1 o 2 para recibir indicaciones de llegada: ")
    if (op < '1') or (op > '2'):
        print("Error zona wifi")
        exit()
    else:
        if (op == '1') or (op == '2'):
            tiempo_moto, tiempo_carro = calculo_tiempo(lista_ubicacion[int(op) - 1][3])
            if (float(lista_ubicacion[int(op) - 1][0]) > float(ubicacion_actual[0])):
                lat = "norte"
            else:
                lat = "sur"
            if (float(lista_ubicacion[int(op) - 1][1]) > float(ubicacion_actual[1])):
                lon = "oriente"
            else:
                lon = "occidente"
        print("debe dirigirse primero al {} y luego al {}, su tiempo de llegada en moto es de {} min, su tiempo de llegada en carro es de {} min".format(lat, lon, tiempo_moto, tiempo_carro))
        return lista_ubicacion[int(op) - 1], tiempo_moto, tiempo_carro
    while True:
        op = input("Presione 0 para salir: ")
        if (op == '0'):
            return

def exportar_archivo(ubicacion_actual, zona_wifi1, tiempo_moto, tiempo_carro):
    """[funcion para exportar datos a un archivo .txt]

    Args:
        ubicacion_actual ([list]): [lista con la ubicacion actual]
        zona_wifi1 ([list]): [lista con las ubicaciones de la zona wifi]
        tiempo_moto ([str]): [variable que contiene el tiempo que se tarda en moto]
        tiempo_carro ([str]): [variable que contiene el tiempo que se tarda en carro]
    """
    informacion = dict(actual=ubicacion_actual, zonawifi1=[zona_wifi1[0], zona_wifi1[1], zona_wifi1[2]], recorrido=[zona_wifi1[3],"carro", tiempo_carro, "moto", tiempo_moto])
    print(informacion)
    push = input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal: ")
    if (push == '1'):
        stream = crear_archivo()
        stream.write(str(informacion))
        print("Exportando archivo")
        stream.close()
        exit()
    elif (push == '0'):
        return

def crear_archivo():
    """[funcion para crear un archivo .txt]

    Returns:
        [TextIOWrapper]: [variable que contiene el metodo para abrir archivos.txt]
    """
    try:
        stream = open("prueba.txt", "w+", encoding="utf-8")
        # aqui se procesa el archivo
        return stream
    except Exception as exc:
        print("No se puede abrir el archivo:", exc)

# lista de opciones para el menu
option = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona WIFI mas cercana",
        "Guardar archivo con ubicacion cercana", "Actualizar registros de zonas WIFI desde archivos",
        "Elegir opcion de menu favorita", "Cerrar sesion"]

coordenada = [] # lista vacia para ingresar las coordenadas
n = True # variable para controlar si el usuario ya ha ingresado las coordenadas
n1 = True # variable para controlar si el usuario ya ha definido su ubicacion actual
n2 = True # variable para controlar si el usuario ya ha exportado su ubicacion actual

lista_ubicacion = [['-3.777', '-70.302',  91], # lista con las ubicaciones para las zonas wifi
                   ['-4.134', '-69.983', 233],
                   ['-4.006', '-70.132', 149],
                   ['-3.846', '-70.222', 211],
                   ]

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
        if (n == True):
            print("Error sin registro de coordenadas")
            break
        else:
            show_coordenadas(coordenada)
            ubicacion_actual = choose_ubicacion(coordenada, lista_ubicacion)
            zonas_wifi(lista_ubicacion)
            show_zonawifi(lista_ubicacion)
            zona_wifi1, tiempo_moto, tiempo_carro = indicaciones(ubicacion_actual, lista_ubicacion)
            n1 = False
    elif ((opcion - 1) == option.index("Guardar archivo con ubicacion cercana")):
        if (n == True) or (n1 == True):
            print("Error de alistamiento")
            break
        else:
            exportar_archivo(ubicacion_actual, zona_wifi1, tiempo_moto, tiempo_carro)
            n2 == False
    elif ((opcion - 1) == option.index("Actualizar registros de zonas WIFI desde archivos")):
            if (n2 == True):
                pass
            else:
                exportar_archivo(ubicacion_actual, zona_wifi1, tiempo_moto, tiempo_carro)
                sele = input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal")
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




