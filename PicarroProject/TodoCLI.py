import argparse
import requests
import json

"""
    The following file contains the configuration and request methods for the
    user-facing CLI.
"""

url = 'http://localhost:5000/'

def formatResponseList(responseObj):
    responseDict = json.loads(responseObj)
    for key, value in responseDict.items():
        print("------------------------------------------------")
        print("Task: " + str(key))
        print("Contents: ")
        print("\tTask Description: " + str(value.get("task")))
        print("\tDate and Time Added: " + str(value.get("date_added")))
        print("\tCompleted: " + str(value.get("completed")))

def checkResponse(responseObj):
    responseDict = json.loads(responseObj)
    if (responseDict.get("success") is True):
        print()
        print("~~ Request Successful ~~")
    else:
        print()
        print("~~ Request Unsuccessful ~~")

def getAllTasks():
    response = requests.get(url + 'get-all-tasks')
    formatResponseList(response.text)

def getTask(id):
    response = requests.get(url + 'get-task/' + str(id))
    if response.status_code == 404:
        print()
        print("ID does not exist.")
    else:
        formatResponseList(response.text)

def addTask(taskContent):
    data = {"task" : taskContent}
    response = requests.post(url + 'add-task', json=data)
    print("New task ID: " + str(response.text))

def completeTask(id):
    response = requests.put(url + 'complete-task/' + str(id))
    checkResponse(response.text)

def incompleteTask(id):
    response = requests.put(url + 'incomplete-task/' + str(id))
    checkResponse(response.text)

def changeTaskDescription(id, taskContent):
    data = {"task" : taskContent}
    response = requests.put(url + 'change-task-description/' + str(id), json=data)
    checkResponse(response.text)

def deleteTask(id):
    response = requests.delete(url + 'delete-task/' + str(id))
    checkResponse(response.text)

parser = argparse.ArgumentParser(description="Todo list CLI program.")
parser.add_argument("request", choices=["getall", "gettask", "addtask", "complete", "incomplete", "updatedesc", "delete"])
parser.add_argument("-i", "--id", type=int, help="ID for task request, used for get, update, delete")
parser.add_argument("-c", "--content", help="Content for task request, used for add, update")
args = parser.parse_args()

if args.request == "getall":
    getAllTasks()
elif args.request == "gettask":
    getTask(args.id)
elif args.request == "addtask":
    addTask(args.content)
elif args.request == "complete":
    completeTask(args.id)
elif args.request == "incomplete":
    incompleteTask(args.id)
elif args.request == "updatedesc":
    changeTaskDescription(args.id, args.content)
elif args.request == "delete":
    deleteTask(args.id)
