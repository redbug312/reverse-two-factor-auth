.PHONY: start

PID = server.pid

start:
	. env/bin/activate
	if [ -e $(PID) ]; then \
		kill -TERM $$(cat $(PID)) || true; \
	fi;
	env FLASK_APP=run.py flask run & echo $$! > $(PID)

