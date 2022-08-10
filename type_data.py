# This program show the type of data

print("""
      Tipos de datos
      ----------
      1. str   |
      2. int   |
      3. bool  |
      4. float |
      ----------
      """)
t_dato = input("Seleccione el tipo de dato que desea ingresar: ")
if (t_dato == '1'):
    t_dato = input("Digite el dato de tipo string: ")
    print(t_dato, "este tipo de dato es ", type(t_dato))
elif (t_dato == '2'):
    t_dato = int(input("Digite el dato de tipo entero: "))
    print(t_dato, "este tipo de dato es ", type(t_dato))
elif (t_dato == '3'):
    t_dato = input("Digite el dato de tipo booleano: ")
    if (t_dato == 'False') or (t_dato == 'None') or (t_dato == '0') or (t_dato == '0.0'):
        t_dato = bool(t_dato)
        t_dato = not(t_dato)
        print(t_dato, "este tipo de dato es ", type(t_dato))
        exit()
    t_dato = bool(t_dato)
    print(t_dato, "este tipo de dato es ", type(t_dato))
elif (t_dato == '4'):
    t_dato = float(input("Digite el dato de tipo flotante: "))
    print(t_dato, "este tipo de dato es ", type(t_dato))
else:
    print("Error, no ha seleccionado una opcion valida")

