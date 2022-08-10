import os

print("Bienvenido al sistema de ubicacion para zonas publicas WIFI")
user = "51606" # Usuario para ingresar
password = "60615" # Contraseña de ingreso
print("Para acceder por favor digite como usuario:", user, " y como contraseña:", password)
n_user = input("Digite su nombre de usuario: ")

if (n_user != user):
    print("Error", "debe ingresar un usuario valido")
    exit()
else:
    print("user successful")

n_pass = input("Digite su contraseña: ")

if (n_pass != password):
    print("Error", "debe ingresar una contraseña correcta")
    exit()
else:
    print("password successful")

#Codigo de seguridad
n1 = 606
n2 = ((6 * 0 + 6) + (6 * 6 - 0)) * 0
print("Para continuar ingrese el valor del codigo de seguridad ", n1, "+", n2, "=", end=" ")
catpcha = int(input())

if (catpcha == (n1 + n2)):
    print("Sesión iniciada")
else:
    print("Error, el codigo de seguridad ingresado es incorrecto")

os.system("cls")

def menu(a):
    for i in range(0, len(a)):
        print(i + 1, '.', a[i])

def seleccion ():
    opcion = int(input("\nPor favor seleccione la opcion que desea realizar: "))
    return opcion

option = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona WIFI mas cercana",
        "Guardar archivo con ubicacion cercana", "Actualizar registros de zonas WIFI desde archivos",
        "Elegir opcion de menu favorita", "Cerrar sesion"]

while True:
    menu(option)
    opcion = seleccion()
    cont = 3
    while (opcion < 1) or (opcion > 7):
        if (cont == 0):
            print(f"Error tus intentos restantes son {cont} ")
            exit()
        print(f"Error, opcion invalida, te quedan {cont} intentos")
        opcion = seleccion()
        cont -= 1
    if (opcion == 1):
        print("Usted ha elegido la opción 1")
        exit()
    elif (opcion == 2):
        print("Usted ha elegido la opción 2")
        exit()
    elif (opcion == 3):
        print("Usted ha elegido la opción 3")
        exit()
    elif (opcion == 4):
        print("Usted ha elegido la opción 4")
        exit()
    elif (opcion == 5):
        print("Usted ha elegido la opción 5")
        exit()
    elif (opcion == 6):
        favorite = int(input("Por favor seleccione una opcion del 1-5 como favorito: "))
        if (favorite < 1) or (favorite > 5):
            print("Error, ha ingresado una opcion invalida")
            exit()
        else:
            print("para confirmar la seleccion debera responder las siguientes preguntas")
            n1 = int(input("Antes era un ocho pero perdi mi parte superior, la respuesta es: "))
            if (n1 != 0):
                print("Error, respuesta incorrecta")
            else:
                n2 = int(input("Soy hermano del nueve pero siempre mi cabeza mira al piso, la respuesta es: "))
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




