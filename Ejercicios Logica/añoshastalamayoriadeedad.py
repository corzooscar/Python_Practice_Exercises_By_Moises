edad = int(input("Ingrese su edad y veremos cuanto le falta para ser mayor de edad: "))

if edad >= 18:
    print("Usted ya es mayor de edad")
elif edad < 18:
    print(f"Le faltan {18-edad} año/s para ser mayor de edad")