print("Compararemos 3 números y veremos cual es el más grande de los 3")
num1 = int(input("Ingrese el primer número: " ))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: " ))

if num1 > num2 and num1 > num3:
    print(f"El número {num1} es más grande que {num2} y {num3}")
elif num2 > num1 and num2 > num3:
    print(f"El número {num2} es más grande que {num1} y {num3}")
elif num3 > num1 and num3 > num1:
    print(f"El número {num3} es más grande que {num1} y {num2}")
elif num1 == num2 and  num2 == num3:
    print("Los números son iguales")
else:
    print("huh")