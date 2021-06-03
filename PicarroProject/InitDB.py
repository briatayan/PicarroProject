import sqlite3
import os.path
from os import path

"""
    The following file initializes the .db file that the API interacts with.
    If the table already exists or the DB file already exists, then it prints a
    message.
"""

def createDb():
    con = sqlite3.connect('todo.db')

    cur = con.cursor()

    # creates TODO table
    try:
        cur.execute(''' CREATE TABLE todo (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                    date_added DATETIME DEFAULT CURRENT_TIMESTAMP, task text, completed INTEGER DEFAULT 0) ''')
    except:
        print("Table already exists.")

    # test insertion into Table
    #cur.execute("INSERT INTO todo (task) VALUES ('test task')")

    # commit addition of table
    con.commit()

    # check insertion into Table
    #for row in cur.execute('SELECT * FROM todo'):
    #   print(row)

    # close connection to DB
    con.close()


def main():
    if (not path.exists('todo.db')):
        createDb()
    else:
        print("DB already exists")

main()
