opcion = 0
while opcion != 3:
    opcion = int(input('\n1. Saludar\n2. Despedirse\n3. Salir\nIngrese una opción: '))
    if opcion == 1:
        print('\nHolaa')
    elif opcion == 2:
        print('\nAdios')
    else:
        print('\nIngrese una opción valida')