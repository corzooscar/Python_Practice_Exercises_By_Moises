print("Ingrese dos números y veremos cual es mayor")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
elif num1 < num2:
    print(f"El número {num2} es mayor que {num1}")
elif num1 == num2:
    print(f"El número {num1} es igual que {num2}")
else: 
    print("huh")