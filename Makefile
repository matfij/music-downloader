export MAIN_SCRIPT := src/main.py
export ENVIRONMENT_SCRIPT := .venv\Scripts\activate

.ONESHELL:

activate:
	${ENVIRONMENT_SCRIPT}

run:
	( \
		${ENVIRONMENT_SCRIPT}; \
		py ${MAIN_SCRIPT}; \
	)

clean:
	rm -r -f .venv

quick.start:
	( \
		py -m venv .venv; \
		${ENVIRONMENT_SCRIPT}; \
		pip install -r requirements.txt; \
		py ${MAIN_SCRIPT}; \
	)
