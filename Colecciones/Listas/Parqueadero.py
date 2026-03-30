parking = [None]*10
option = 0


while option != "4":
    #Opciones 
    option = input("\n1. Show cars\n2. Enter a car\n3. Take out a car\n4. Leave\nEnter an option: ")
    
    #Mostrar los carros en el parqueadero
    if option == "1":
        for idx, car in enumerate(parking):
            if car is None:
                print(f"Spot {idx+1}: Free")
            else:
                print(f"Spot {idx+1}: {car}")

    #Ingresar un carro
    elif option == "2":
        #Validación si esta lleno el parqueadero
        if None not in parking:
            print("The parking lot is full, you can't enter a car")

        else:
            #Ingresar la placa
            carPlate = input("Enter your car plate: ").upper()
            

            #Validación de la placa tenga la longitud y caracteres correctos
            if len(carPlate) != 6:
                print("The car plate must have 6 characters")

            elif not carPlate[:3].isalpha():
                print("The first 3 characters must be letters")

            elif not carPlate[3:].isdigit():
                print("The last 3 characters must be digits")
            
            else:
                #Validación si la placa ya esta adentro
                if carPlate in parking:
                    print("The car is already in the parking lot")

                #Validación si la placa no esta dentro
                elif carPlate not in parking:
                    #Meter el carro al parqueadero
                    spot = parking.index(None)
                    parking[spot] = carPlate
    
    #Sacar un carro
    elif option == "3":

        #Ingresar placa
        carPlate = input("Enter your car plate: ").upper()

        #Validación de la placa tenga la longitud y caracteres correctos
        if len(carPlate) != 6:
            print("The car plate must have 6 characters")

        elif not carPlate[:3].isalpha():
            print("The first 3 characters must be letters")

        elif not carPlate[3:].isdigit():
            print("The last 3 characters must be digits")
            
        else:
            #Validación si el carro no esta dentro
            if carPlate not in parking:
                print("The car is not in the parking lot")

            #Validación de que el carro este adentro
            elif carPlate in parking:
                spot = parking.index(carPlate)
                parking[spot] = None
    
    #Salir del programa
    elif option == "4":
        print("Goodbye!!!")
    
    #Validación de otro número
    else:
        print("Not a valid option, choose a number from 1 to 4")

