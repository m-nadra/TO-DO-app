import sqlite3


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
