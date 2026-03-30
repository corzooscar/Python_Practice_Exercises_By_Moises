contraseña = 'python123'
intentoContraseña = None
while contraseña != intentoContraseña:
    intentoContraseña = input('Ingrese la contraseña: ')
    
    if intentoContraseña == contraseña:
        print('Bienvenido')
    else:
        print('Contraseña incorrecta')