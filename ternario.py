# This program show the uses of the ternary operator.

#operador ternario
valor = 2 if (5 > 3) else 4
print(valor)

#forma menos usada, no recomendable

valor = (4, 2) [5 > 3]
print(valor)

#otra forma usando operadores logicos
valor = (5 > 3) and 2 or 4
print(valor)
