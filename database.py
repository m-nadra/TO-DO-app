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
            count = 1
            for i in table:
                print(f"{count}. Task: {i[1]}, Deadline: {i[2]}")
                count += 1
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