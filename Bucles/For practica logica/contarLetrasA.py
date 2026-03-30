palabra = input('Ingrese una palabra: ')

a=0
for i in palabra:
    if i.lower() == "a":
        a += 1
print(f'En la palabra "{palabra}" hay {a} A')