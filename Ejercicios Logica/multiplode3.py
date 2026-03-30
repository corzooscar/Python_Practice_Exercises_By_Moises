numero = int(input("Ingrese un número y veremos si es un multiplo de 3: "))

if (numero % 3) == 0:
    print(f"El número {numero} es multiplo de 3")
elif (numero % 3) != 0:
    print(f"El número {numero} no es multiplo de 3")