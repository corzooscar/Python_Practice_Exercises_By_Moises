numero = float(input("Ingrese un número y determinaremos si es par o impar: "))

if (numero % 2) == 0:
    print(f"El número {numero} es par")
elif (numero % 2) != 0:
    print(f"El número {numero} es impar")
else: 
    print("????")
