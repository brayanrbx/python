def euler(x):
    suma, aux = 0, 0
    for i in range(x):
        if (i == 0):
            aux = 1
        else:
            aux *= i
        suma += (1 / aux)
    return suma

result = euler(14)
print(result)
