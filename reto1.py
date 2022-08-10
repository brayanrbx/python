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

