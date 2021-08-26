.ONESHELL:

export PYTHON := py
export PIP := pip
export APP := src/app.py
export VENV := .venv\Scripts\activate

venv:
	${VENV}

run:
	( \
		${VENV}; \
		${PYTHON} ${APP}; \
	)

clean:
	rm -r -f .venv

quick.start:
	( \
		${PYTHON} -m venv .venv; \
		${VENV}; \
		${PIP} install -r requirements.txt; \
		${PYTHON} ${APP}; \
	)
