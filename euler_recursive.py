def euler(x):
    suma = 0
    if (x == 0):
        suma = 1
        return suma
    else:
        suma = (1 / factorial(x))
        return (suma + euler(x - 1))

def factorial(x):
    if (x == 0):
        return 1
    else:
        return (x * factorial(x - 1))

result = euler(14)
print(result)