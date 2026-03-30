import os

#functions
def add_daily_blocker(blocker):
        with open("database.txt", "a") as a:
             a.write(f"{blocker}\n")

def show_all_blockers():
    with open("database.txt", "r") as r:
        return r.read()

#Initilize variable
option = None

#Validation to create file if it doesn't exist
fileValidation = os.path.exists("database.txt")

if not fileValidation:
     with open("database.txt", "x") as x:
         print("\n[Data base file created]")



#Menu
while option != "3":
    print(f"\n{"-"*20}Menu{"-"*20}")
    option = input("1. Add blocker to database\n2. Show blockers\n3. Leave\nYour Option: ")
    if option == "1":
            blocker = input("\nHi, what's is your blocker today?\nYour blocker: ")
            add_daily_blocker(blocker)
    elif option == "2":
        print(f"\n{"-"*18}Blockers{"-"*18}\n{show_all_blockers()}")

    elif option == "3":
        print("\nGoodbye!!")
    
    else:
         print("Choose a valid option, (1-3)")


#Protocol Selection

#To report a file error I would use Jira becasue it is designed to track technical issues, allowing me to set a ticket to the right person
#and set the priority level.
#Jira also keeps track of the error's history, that way the team who have to fix the error can keep an eye on the progress of the ticket until it is solved.
#So i just need to ask to the assigned team member to review my ticket at their time of convinience and provide me with an update of the expected resolution time


#Vocabulary Integration

#The script waits the user's input to select one of the options, if the user selects option 1 the script is going to add a blocker to the database, becasue i used "a" mode
#it won't overwrite the current database if there's any information, the script is only going to add the new information, that way the information persists. 
#If the option 2 is selected, the script is going reach out all the blockers in the database and show it,
#so the script fetchs the information saved in the database and displays it in console. Option 3 just ends the script. There's a validation to
#make the database in case there's none 