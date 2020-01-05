.PHONY: start

ENV ?= . ../env/bin/activate; \
	   PYTHONPATH=$(shell realpath ..)
MIXINS = $(shell realpath app/templates/mixins/)

start:
	$(ENV) FLASK_APP=run.py FLASK_ENV=development flask run --port=5000 --extra-files=$(MIXINS)
