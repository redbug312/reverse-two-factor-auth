.PHONY: start test

export ENV = . $(shell pwd)/env/bin/activate; \
	         PYTHONPATH=$(shell pwd)

start:
	$(ENV) make start -C server

test:
	$(ENV) pytest test
