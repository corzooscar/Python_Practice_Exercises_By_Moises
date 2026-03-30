studentsList = []
option = None

while option != "3":
    option = input("\n1. Register a student.\n2. Show registered students.\n3. Leave.\nChoose an option: ")

    if option == "1":
        try:
            studentsQuantity = int(input("\nHow many students are you going to register?\nNumber: "))
        
            for i in range(studentsQuantity):
                subjectsAndGrades = []
                studentFullName = input(f"\nEnter the {i+1} student's full name.\nFull name: ")
                
                subjectQuantity = int(input("\nHow many subjects are you going to register for this student?\nNumber: "))
                
                for i in range(subjectQuantity):
                    subject = input(f"\nEnter the {i+1} subject for the student.\nSubject: ")
                    grade = float(input(f"\nEnter the {subject} grade.\nGrade: "))

                    subjectsAndGrades.append({
                        "subject":subject,
                        "grade":grade,
                    })
                
                studentsList.append({
                    "studentName":studentFullName,
                    "subjectsAndGrades":subjectsAndGrades
                })

                print(f"\n-----Student {i+1} registered sucessfully-----")
        except:
            print("\n----- ERROR -----\nEnter a valid number")


    elif option == "2":
        print(f"\n{"-"*8}Students{"-"*8}")
        for i, student in enumerate(studentsList):
            sum_grades = 0
            gradesQuantity = 0
            print(f"{i+1}. {student['studentName']}\n")
            
            for i, studentSubjectAndGrade in enumerate(student["subjectsAndGrades"]):
                print(f"Subject {i+1}: {studentSubjectAndGrade['subject']}\nGrade: {studentSubjectAndGrade['grade']}\n")
                
                for key, value in studentSubjectAndGrade.items():
                    if key == 'grade':
                        sum_grades += value
                        gradesQuantity += 1
                gradesAverage = sum_grades / gradesQuantity
        
            print(f"Grades Average: {gradesAverage}\n{"-"*25}")

        print(f"{"-"*5}End of the list{"-"*5}")
    
    elif option == "3":
        print(f"\nGoodbye!!")

    else:
        print("Choose a valid option.")
