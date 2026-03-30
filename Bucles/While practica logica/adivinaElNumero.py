secreto = 28
numero = 0
while numero != secreto:
    numero = int(input('Ingrese un número para adivinar el número secreto: '))
    if numero > secreto:
        print(f'El número secreto es menor a {numero}')
    elif numero < secreto:
        print(f'El número secreto es mayor a {numero}')
    elif numero == secreto:
        print(f'Ganaste!!!, Ingresaste el número secreto')
    else:
        print('huh')

