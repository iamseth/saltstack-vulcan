SHELL := /bin/bash

build:
	@python setup.py build

install:
	@python setup.py install

lint:
	@pylint -r n --rcfile .pylintrc vulcan

test:
	@python -m unittest discover

deploy:
	@python setup.py sdist upload -r pypi

clean:
	@rm -rf build saltstack_vulcan.egg-info dist formulas


.PHONY: build lint test deploy clean
