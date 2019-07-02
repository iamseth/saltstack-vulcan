SHELL := /bin/bash


build:
	@python setup.py sdist bdist_wheel

lint:
	@pylint -r n --rcfile .pylintrc vulcan

test:
	@python -m unittest discover

test-release: build
	@twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release: build
	@twine upload dist/*

clean:
	@rm -rf build saltstack_vulcan.egg-info dist formulas


.PHONY: build lint test release clean
