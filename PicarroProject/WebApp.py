from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, request, json
import service.TodoListService as service

"""
    The following file contains the endpoints needed to interact with the API
    service. Each endpoint also handles response messages and initial
    verification of ID or content.
"""

app = Flask(__name__)

# Following code from
# https://sean-bradley.medium.com/add-swagger-ui-to-your-python-flask-api-683bfbb32b36
### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Todo-List-CLI-Service"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

"""
 Contains endpoints for TODO list program
"""

# Test if app can receive requests
@app.route("/hello")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/get-all-tasks", methods=['GET'])
def getAllTasks():
    taskList = service.getAllTasks()
    if taskList is None:
        return json.dumps({'success':False, 'description': 'IDs not found'}), 404, {'ContentType':'application/json'}
    else:
        jsonObjectDict = taskList
        return json.jsonify(jsonObjectDict)

@app.route("/get-task/<int:id>", methods=['GET'])
def getTask(id):
    task = service.getTask(id)
    if task is None:
        return json.dumps({'success':False, 'description': 'ID not found'}), 404, {'ContentType':'application/json'}
    else:
        jsonObject = task
        return json.jsonify(jsonObject)

@app.route("/add-task", methods=['POST'])
def addTask():
    jsonData = request.get_json()
    if jsonData is None or jsonData.get("task") is None or jsonData.get("task") == "" or not isinstance(jsonData.get("task"), str):
        return json.dumps({'success':False, 'description': 'Bad Request'}), 400, {'ContentType':'application/json'}
    else:
        jsonDict = dict(jsonData)
        lastId = service.insertTask(str(jsonDict.get("task")))
        return str(lastId)

@app.route("/change-task-description/<int:id>", methods=['PUT'])
def changeTaskDescription(id):
    jsonData = request.get_json()
    jsonDict = dict(jsonData)
    res = service.changeTaskDescription(id, str(jsonDict.get("task")))
    if res is False:
        return json.dumps({'success':False, 'description': 'ID not found'}), 404, {'ContentType':'application/json'}
    elif jsonData.get("task") is None:
        return json.dumps({'success':False, 'description': 'Bad Request'}), 400, {'ContentType':'application/json'}
    else:
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/complete-task/<int:id>", methods=['PUT'])
def changeTaskToComplete(id):
    res = service.changeTaskToComplete(id)
    if res is False:
        return json.dumps({'success':False, 'description': 'ID not found'}), 404, {'ContentType':'application/json'}
    else:
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/incomplete-task/<int:id>", methods=['PUT'])
def changeTaskToIncomplete(id):
    res = service.changeTaskToIncomplete(id)
    if res is False:
        return json.dumps({'success':False, 'description': 'ID not found'}), 404, {'ContentType':'application/json'}
    else:
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/delete-task/<int:id>", methods=['DELETE'])
def deleteTask(id):
    res = service.deleteTask(id)
    if res is False:
        return json.dumps({'success':False, 'description': 'ID not found'}), 404, {'ContentType':'application/json'}
    else:
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
