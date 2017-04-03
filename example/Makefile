SHELL := /bin/bash

.PHONY: all
all:
	@vulcan --debug --config example_vulcan.yaml update
	@mkdir -p dist
	@rsync -a ./salt/ ./dist/salt/ --delete
	@rsync -a ./formulas/ ./dist/formulas/ --delete
	@git log --pretty=oneline | head -n1 | cut -c1-8 > ./dist/SHA
	@echo "Salt is ready in ./dist. Enjoy!"
