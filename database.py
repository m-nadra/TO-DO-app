import sqlite3
import datetime


def printTasks():
    con = sqlite3.connect('todo.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM task;")
    table = cursor.fetchall()
    if len(table) == 0:
        print("No tasks to do.")
    else:
        for i in table:
            print(f"Task: {i[1]}, Deadline: {i[2]}")
    cursor.close()
    con.close()


def addTask(name, deadline):
    con = sqlite3.connect('todo.db')
    cursor = con.cursor()
    userValues = (name, deadline)
    cursor.execute("INSERT INTO task(name, deadline) VALUES(?, ?)", userValues)
    con.commit()
    cursor.close()
    con.close()


def printTodayTasks():
    con = sqlite3.connect('todo.db')
    cursor = con.cursor()
    today = datetime.datetime.now()
    queryDate = (f"{today.year}-{today.month}-{today.day}",)
    cursor.execute("SELECT name FROM task WHERE deadline = ?;", queryDate)
    table = cursor.fetchall()
    if len(table) == 0:
        print("No tasks to do.")
    else:
        for i in table:
            print(f"Task: {i[0]}")
    cursor.close()
    con.close()

def deleteTask():
    con = sqlite3.connect('todo.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM task;")
    table = cursor.fetchall()
    if len(table) == 0:
        print("No tasks to do.")
    else:
        while True:
            count = 0
            for i in table:
                count += 1
                print(f"{count}. Task: {i[1]}, Deadline: {i[2]}")
            taskToDelete = int(input("Enter task number to delete or Enter 0 to exit to menu: "))
            if taskToDelete == 0:
                print("Going back to menu.")
                break
            elif taskToDelete > count or taskToDelete < 1:
                print("Invalid input! Try again.")
                continue
            else:
                cursor.execute("DELETE FROM task WHERE id = ?;", str(table[taskToDelete-1][0]))
                break
    con.commit()
    cursor.close()
    con.close()

def editTask():
    con = sqlite3.connect('todo.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM task;")
    table = cursor.fetchall()
    if len(table) == 0:
        print("No tasks to do.")
    else:
        while True:
            count = 0
            for i in table:
                count += 1
                print(f"{count}. Task: {i[1]}, Deadline: {i[2]}")
            taskToEdit = int(input("Enter task number to edit or Enter 0 to exit to menu: "))
            if taskToEdit == 0:
                print("Going back to menu.")
                break
            elif taskToEdit > count or taskToEdit < 1:
                print("Invalid input! Try again.")
                continue
            else:
                newName = input("Enter new task name: ")
                newDeadline = input("Enter new task deadline: ")
                editTask = (newName, newDeadline, str(table[taskToEdit - 1][0]))
                cursor.execute("UPDATE task SET name = ?, deadline = ? WHERE id = ?;", editTask)
                break
    con.commit()
    cursor.close()
    con.close()
