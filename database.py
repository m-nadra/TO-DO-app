import sqlite3


def printTasks():
    con = sqlite3.connect('todo.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM task;")
    print(cursor.fetchall())
    cursor.close()
    con.close()
