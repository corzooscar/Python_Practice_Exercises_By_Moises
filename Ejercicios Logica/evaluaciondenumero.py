numero = int(input("Ingrese un número y veremos si es multiplo de 2, de 3 o de ambos: "))

if (numero % 2 == 0) and (numero % 3 == 0):
    print(f"El número {numero} es multiplo de 2 y 3.")
elif numero % 2 == 0:
    print(f"El número {numero} es multiplo de 2")
elif numero % 3 == 0:
    print(f"El número {numero} es multiplo de 3")
else:
    print(f"El número {numero} no es multiplo de ninguno")