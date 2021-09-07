.ONESHELL:

PYTHON := py
PIP := pip
APP := src/app.py
VENV := .venv\Scripts\activate

run:
	${VENV}
	${PYTHON} ${APP}

clean:
	rm -r -f .venv

quick.start:
	${PYTHON} -m venv .venv
	${VENV}
	${PIP} install -r requirements.txt
	${PYTHON} ${APP}
