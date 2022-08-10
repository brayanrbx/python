# This program show a menu

menu = """
    MENU
---------------
1 - Sopas     |
2 - Secos     |
3 - Bebidas   |
4 - Ensaladas |
5 - Postres   |
6 - Salir     |
---------------
"""
bandera = True
while bandera:
    print (menu)
    opcion = int(input("Escoga la opcion de su agradado:  "))
    if opcion is 1:
        print ("Sopa de Queso, pescado, Ajiaco, Mute")
    elif opcion is 2:
        print ("Arroz de Coco, Manteca, Camaron, Pollo, Calentado")
    elif opcion is 3:
        print ("Guarapo, Corrozo, Limonada panela, Borojo")
    elif opcion is 4:
        print ("Ensalada de Pepino, Aguacate, Lechuga, Tomate, Griega")
    elif opcion is 5:
        print ("Postre tiramizu ")
    elif opcion is 6:
        print ("Saliste de la sesion ")
        break
    else:
        print ("Digita bien tu numero")