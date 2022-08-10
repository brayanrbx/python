# This program calculates the hipotenuse of a right triangle.

cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)