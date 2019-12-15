.PHONY: start test

ROOT = $(shell pwd)
export FLASK  = $(ROOT)/env/bin/flask
export PYTEST = $(ROOT)/env/bin/pytest


start:
	PYTHONPATH=$(ROOT) make start -C server

test:
	PYTHONPATH=$(ROOT) $(PYTEST) test
