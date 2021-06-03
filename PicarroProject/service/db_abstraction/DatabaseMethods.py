import sqlite3
from sqlite3 import Error
import json

"""
    The following file contains methods that interact with the database
    directly, and converts the tuples from the result into JSON objects.
"""

# Creates connection to DB, returns connection object to use in queries
def createConnection(file):
    con = None
    try:
        con = sqlite3.connect(file)
    except Error as e:
        print(e)

    return con

# Closes connection to DB
def closeConnection(con):
    con.close()

# Inserts single task into TODO table
def insertTask(con, taskContent):
    cur = con.cursor()
    cur.execute("INSERT INTO todo (task) VALUES ('" + taskContent + "')")
    lastId = cur.lastrowid
    con.commit()
    return lastId

# Deletes single task into TODO table
def deleteTask(con, id):
    if checkIfExists(con, id) is False:
        return False
    else:
        cur = con.cursor()
        cur.execute("DELETE FROM todo WHERE id = " + str(id))
        con.commit()
        return True

# Retrieves single task
def getTask(con, id):
    cur = con.cursor()
    cur.execute("SELECT id, date_added, task, completed FROM todo WHERE id = " + str(id))
    res = cur.fetchone()
    if res is None:
        return res
    else:
        return dbToJson(res)

# Retrieves all tasks
def getAllTasks(con):
    cur = con.cursor()
    cur.execute("SELECT * FROM todo")
    res = cur.fetchall()
    if res is None:
        return res
    else:
        return dbToJsonList(res)

# Updates task description
def changeTaskDescription(con, id, newDesc):
    if checkIfExists(con, id) is False:
        return False
    else:
        cur = con.cursor()
        cur.execute("UPDATE todo SET task = '" + newDesc + "' WHERE id = " + str(id))
        con.commit()
        return True

# Switches 'boolean' complete value to 1, which means the task has been completed
def changeTaskToComplete(con, id):
    if checkIfExists(con, id) is False:
        return False
    else:
        cur = con.cursor()
        cur.execute("UPDATE todo SET completed = 1 WHERE id = " + str(id))
        con.commit()
        return True

# Switches 'boolean' complete value to 0, which means the task is now incomplete
def changeTaskToIncomplete(con, id):
    if checkIfExists(con, id) is False:
        return False
    else:
        cur = con.cursor()
        cur.execute("UPDATE todo SET completed = 0 WHERE id = " + str(id))
        con.commit()
        return True

# converts tuple from DB into JSON object
def dbToJson(resObj):
    obj = dict()
    resObj = tuple(resObj)
    date = resObj[1]
    task = resObj[2]
    completed = resObj[3]
    obj[resObj[0]] = {
        "date_added" : date, "task" : task, "completed" : completed
    }
    return obj

# converts a list of tuples into JSON objects
def dbToJsonList(resList):
    objDictList = dict()
    objDict = dict()
    for res in resList:
        date = res[1]
        task = res[2]
        completed = res[3]
        tempDict = {
            "date_added" : date, "task" : task, "completed" : completed
        }
        objDict[res[0]] = tempDict
    return objDict

# runs query to check if row item exists, given ID
def checkIfExists(con, id):
    cur = con.cursor()
    cur.execute("SELECT id FROM todo WHERE id = " + str(id))
    res = cur.fetchone()
    if res is None:
        return False
    else:
        return True
