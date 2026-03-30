print("Veremos su signo zodiacal dependiendo de su dia y fecha de nacimiento")
dia = int(input("Ingrese su dia de nacimiento (1-31): "))
mes = int(input("Ingrese su mes de nacimiento: (1-12)"))

#Comprobación
if (dia <= 31 and dia >= 1) and (mes <= 12 and mes >= 1):
    #zodiacal
    
    #Acuario
    if (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
        print("Su signo zodiacal es Acuario!!")
    #Piscis
    elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
        print("Su signo zodiacal es Piscis!!")
    #Aries
    elif (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
        print("Su signo zodiacal es Aries!!")
    #Tauro    
    elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
        print("Su signo zodiacal es Tauro!!")
    #Geminis
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
        print("Su signo zodiacal es Géminis!!")
    #Cáncer
    elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
        print("Su signo zodiacal es Cáncer")
    #Leo
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        print("Su signo zodiacal es Leo!!")
    #Virgo
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        print("Su signo zodiacal es Virgo!!")
    #Libra
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        print("Su signo zodiacal es Libra!!")
    #Escorpio
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        print("Su signo zodiacal es Escorpio!!")
    #Sagitario
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        print("Su signo zodiacal es Sagitario!!")
    #Capricornio
    elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
        print("Su signo zodiacal es Capricornio!!")
else: 
    print("Ingrese una fecha valida, los dias van de 1 a 31 y los meses de 1 a 12")
    