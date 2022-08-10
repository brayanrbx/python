# This program show the use of optional en print

texto = "OpenEDG Python Institute"
for letter in texto:
    if letter == "P":
        break
    print(letter, end= "")

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end= "")