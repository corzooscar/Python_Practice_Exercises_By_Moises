import random
numero  = int(input("Ingrese un número del 1 al 10: "))

if numero >= 1 and numero <= 10:
    #adivinar
    valor = random.randint(1, 10)
    if numero == valor:
        print("Victoria!!!")
    else:
        print("Perdiste")
else:
    print("Ingrese un número valido, del 1 al 10")