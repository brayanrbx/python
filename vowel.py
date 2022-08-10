# This program omits whatever vowels are in the string

userWord = input("Ingresa una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if (letra == "A") or (letra == "E") or (letra == "I") or (letra == "O") or (letra == "U"):
        continue
    else:
        print(letra)