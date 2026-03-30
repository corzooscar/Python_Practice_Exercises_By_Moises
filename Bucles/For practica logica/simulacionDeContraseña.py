for i in range (1,4):
    contraseña = input('Ingrese una contraseña: ')

    if contraseña == "python123":
        print('Acceso permitido')
        break
    else:
        print(f'Contraseña incorrecta, le quedan {3-i} intentos')
