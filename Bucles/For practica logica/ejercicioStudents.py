students = []

studentsQuantity = int(input("How many students are you going to register?: "))

for i in range(studentsQuantity):
    studentFullName = input(f"Enter the {i+1} student's full name: ")
    studentAge = int(input(f"Enter the {i+1} student's age: "))

    students.append({
        "fullname": studentFullName,
        "age": studentAge
    })


for i, student in enumerate(students):
    print(f"The {i+1} student's full name is {student['fullname']} and their age is {student['age']}")