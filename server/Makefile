.PHONY: start

ENV ?= . ../env/bin/activate; \
	   PYTHONPATH=$(shell pwd/..)

start:
	$(ENV) FLASK_APP=run.py FLASK_ENV=development flask run

