# PicarroProject
This project was intended to be the solution to Picarro's RESTful API challenge to create a CLI that implements CRUD operations on a TO-DO list for a single user. A makefile is provided with several functions to build, run, and test the web server. In summary, the project has a web server that runs using flask, a database that is implemented using SQLite3, and a CLI that uses argparse to accept commands to edit the TO-DO list.

### How to Start Web Server
- Run ```make develop```, which activates the virtual environment, installs specified requirements via pip, creates the SQLite3 database, and runs the flask app. The web server will run until ```CTRL+C``` is pressed.
- If the user wishes to run a clean build before running the develop command, then the user can use ```clean-build``` to remove cached files, and removes and reinitializes the database.
- The user can also reinitialize the database if it's been removed by using ```reinitialize-db```.
- The web server will be running on ```http://localhost:5000```.

### Testing the Web Server
- Run ```make test``` to start a clean build and run unit tests on the endpoints for the web server. This will take several seconds to complete and will display any errors or failures via Python's unittest framework.

### Using the CLI
The CLI is a separate Python script that accepts different arguments to send requests to the running web server. The following commands are:
- ```python3 TodoCLI.py getall```: Retrieves a list of all tasks in the database.
- ```python3 TodoCLI.py gettask [-i ID]```: Retrieves a task given an existing ID.
- ```python3 TodoCLI.py addtask [-c CONTENT]```: Adds a task to the list given the description of a task.
- ```python3 TodoCLI.py complete [-i ID]```: Marks a task as complete given an existing ID.
- ```python3 TodoCLI.py incomplete [-i ID]```: Marks a task as incomplete given an existing ID.
- ```python3 TodoCLI.py updatedesc [-i ID] [-c CONTENT]```: Updates a task's description given an existing ID.
- ```python3 TodoCLI.py delete [-i ID]```: Deletes a task given an existing ID.
<br><br><b> Each command has entry validation and will return responses if given invalid input. </b>

### Swagger UI
The web server also has Swagger implemented to document the API's endpoints and schemas. It can be accessed at ```http://localhost:5000/swagger```.
