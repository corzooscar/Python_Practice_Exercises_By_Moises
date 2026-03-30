from datetime import datetime as dt
import json
import random
import csv


#initialize variables
option = None
randomNumbers = []
possiblesAnswers = ["A","B","C","D"]

#function to sort the ranking
def sorting(diccionario):
    return int(diccionario["score"])

#random number for choosing the question
def generateRandomNumber(lista):
    question = random.randint(0,99)
    if question not in lista:
        lista.append(question)
    else:
        generateRandomNumber(lista)
    return question
generateRandomNumber(randomNumbers)

#read the json
with open("data.json", "r")as f:
    data = json.loads(f.read())



while option != "3":
    option = input("1. Start the Game\n2. Show Ranking\n3. Leave\nYour Option: ")

    if option == "1":

        #Ask username
        userName = None
        while not userName:
            userName = input("Enter your user name: ")

        score = 0
        correctAnswerQuantity = 0
        #Iteration for the 5 questions
        for i in range(5):
            randomNumber = generateRandomNumber(randomNumbers) #generates random number every iteration

            #Shows questions and answers in terminal
            correctAnswer = None
            for key, value in data[randomNumber].items():
                if key == "pregunta":
                    print(f"\nPregunta #{i+1}: {value}")
                if key == "opciones":
                        for opcion, respuesta in value.items():
                            print(opcion, respuesta)
                if key == "respuesta_correcta":
                        correctAnswer = value
            # print(correctAnswer)#prueba

            #Enters the answer and validates if it's correct or incorrect
            userAnswer = "null"
            while userAnswer.capitalize() not in possiblesAnswers:
                userAnswer = input("\nIngrese su respuesta: ") 
                if userAnswer.capitalize() == correctAnswer:
                    print("\nRespuesta correcta!!\n20 puntos añadidos!")
                    score += 20
                    correctAnswerQuantity += 1
                elif userAnswer.capitalize() in possiblesAnswers and userAnswer != correctAnswer:
                    print("\nRespuesta incorrecta")
                elif userAnswer.capitalize() not in possiblesAnswers:
                    print("\nNo escogio una respuesta valida")

        print(f"\n{"-"*10}Fin del juego{"-"*10}\nTotal de puntos: {score}\nRespuestas correctas: {correctAnswerQuantity}")
        print("-"*30)

        #take date and hour of the user ending the game
        unformattedDate = dt.now()
        formatedDate = unformattedDate.strftime("%d/%m/%Y%l:%M:%S %p")

        #taking user's data
        userInfo = {
            "name":userName,
            "score": score,
            "date": formatedDate
        }

        #Validation if the file doesn't exist, it creates it and reads it
        try:
            #Read the ranking.csv and make it a list 
            with open("ranking.csv", "r") as r:
                reader = csv.DictReader(r)
                datos = list(reader)
        except FileNotFoundError:
            #Create the csv and reads it
            with open("ranking.csv", "x") as x:
                print("Archivo de rankings creado")

            with open("ranking.csv", "r") as r:
                reader = csv.DictReader(r)
                datos = list(reader)


        #Add the last user's game information and sort it by score
        datos.append(userInfo)
        datos.sort(reverse=True, key=sorting)


        #Writes the new ranking
        with open("ranking.csv", "w", newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["name","score","date"])
            writer.writeheader()
            writer.writerows(datos)

    elif option == "2":
        try:
            #Read the ranking.csv and make it a list 
            with open("ranking.csv", "r") as r:
                reader = csv.DictReader(r)
                datos = list(reader)
        except FileNotFoundError:
            print("There's no ranking yet, play one game first")
        
        print("-"*100)
        for users in datos:
            print(f"Username: {users.get("name")} | Score: {users.get("score")} | Date: {users.get("date")}")
        print("-"*100)

    elif option == "3":
        print("Goodbye")

    else:   
        print("Invalid option, choose an option from 1 to 3")