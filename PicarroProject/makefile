PYTHON = python3

.DEFAULT_GOAL = help

.PHONY: clean-pyc reinitialize-db develop run-cli

help:
	@echo "--------------------------------------------------"
	@echo "For instructions on how to set up the project,"
	@echo "please read the documentation at 'README.md'"
	@echo "--------------------------------------------------"

clean-pyc:
		find . -name '*.pyc' -exec rm --force {} +
		find . -name '*.pyo'

develop:
	( \
		. Scripts/activate && \
		pip install -r requirements.txt && \
		${PYTHON} InitDB.py && \
		export FLASK_APP=WebApp.py && \
		${PYTHON} -m flask run \
	)

clean-build: clean-pyc
	rm todo.db
	${PYTHON} InitDB.py

reinitialize-db:
	${PYTHON} InitDB.py

test: clean-build
	${PYTHON} test.py
