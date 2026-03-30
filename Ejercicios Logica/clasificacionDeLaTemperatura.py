print("Ingrese una temperatura y determinaremos si hace frio, calor o una temperatura agradable")
temperatura = float(input("Ingrese la temperatura (Celsius): "))

if temperatura < 15:
    print("Hace frio")
elif temperatura > 25:
    print("Hace calor")
else:
    print("Temperatura agradable")