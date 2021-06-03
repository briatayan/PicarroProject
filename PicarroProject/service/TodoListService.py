import service.db_abstraction.DatabaseMethods as methods

"""
    The following file contains service methods that the web app controller
    can interact with in order to access the database.
"""

def createConnection():
    file = "todo.db"
    con = methods.createConnection(file)
    return con

def closeConnection(con):
    methods.closeConnection(con)

def getAllTasks():
    con = createConnection()
    taskList = methods.getAllTasks(con)
    closeConnection(con)
    return taskList

def getTask(id):
    con = createConnection()
    task = methods.getTask(con, id)
    closeConnection(con)
    return task

def insertTask(taskContent):
    con = createConnection()
    lastId = methods.insertTask(con, taskContent)
    closeConnection(con)
    return lastId

def changeTaskDescription(id, taskContent):
    con = createConnection()
    res = methods.changeTaskDescription(con, id, taskContent)
    closeConnection(con)
    return res

def changeTaskToComplete(id):
    con = createConnection()
    res = methods.changeTaskToComplete(con, id)
    closeConnection(con)
    return res

def changeTaskToIncomplete(id):
    con = createConnection()
    res = methods.changeTaskToIncomplete(con, id)
    closeConnection(con)
    return res

def deleteTask(id):
    con = createConnection()
    res = methods.deleteTask(con, id)
    closeConnection(con)
    return res
