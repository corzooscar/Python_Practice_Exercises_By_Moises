palabra = input('Ingrese una palabra: ')

mayuscula = 0
minuscula = 0

for i in palabra:
    if i.isupper():
        mayuscula += 1
    elif i.islower():
        minuscula += 1

print(f'''La palabra "{palabra}" contiene:
Mayuscula: {mayuscula}
Minuscula: {minuscula}''')
