.PHONY: start test

PARALLEL := parallel --tag --lb

export ENV ?= . $(shell pwd)/env/bin/activate; \
	          PYTHONPATH=$(shell pwd)

start:
	$(ENV) $(PARALLEL) make start -C ::: server broker

test:
	$(ENV) pytest test
