.PHONY: start

ENV ?= . ../env/bin/activate; \
	   PYTHONPATH=$(shell realpath ..)

start:
	$(ENV) FLASK_APP=run.py FLASK_ENV=development flask run --port=5000
