import database as db

while True:
    print("""
1) Today's tasks
2) Add a task
0) Exit
""")
    userInput = int(input(">"))
    match userInput:
        case 1:
            db.printTasks()
        case 2:
            taskName = input("Enter task name: ")
            taskDeadline = input("Enter date (yyyy-MM-dd): ")
            db.addTask(taskName, taskDeadline)
        case 0:
            break
        case _:
            print("Invalid input.")
