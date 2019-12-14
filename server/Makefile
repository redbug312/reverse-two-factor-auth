.PHONY: start

PID = server.pid
FLASK = env/bin/flask

start:
	. env/bin/activate
	if [ -e $(PID) ]; then \
		kill -TERM $$(cat $(PID)) || true; \
	fi;
	export FLASK_APP=run.py FLASK_ENV=development
	$(FLASK) run & echo $$! > $(PID)

