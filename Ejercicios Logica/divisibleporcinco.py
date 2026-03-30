numero = int(input("Ingrese un número y veremos si es divisible por 5: "))

if (numero % 5) == 0:
    print(f"El número {numero} es divisible por 5, su división es {numero/5}")
elif (numero % 5) != 0:
    print(f"El número {numero} no es divisible por 5")
else:
    print("huh")