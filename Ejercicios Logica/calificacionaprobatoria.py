calificacion = float(input("Ingrese la calificación y veremos si aprobó o reprobó: "))

if calificacion >= 60:
    print(f"Aprobo con una calificación de {calificacion}")
elif calificacion < 60:
    print(f"Desaprobo con una calificación de {calificacion}")
else:
    print("huh")