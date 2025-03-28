SHELL := /bin/bash
.DEFAULT_GOAL := help

help:
	@echo "init - install and configure environment. Included: install-requirements, pre-commit-configuration"
	@echo "install-requirements - install python and ansible dependencies"
	@echo "pre-commit-config - install and configure pre-commit hooks"
	@echo "test - run molecule test"
	@echo "docs - create README.md with ansible-doctor"

docs:
	ansible-doctor .

init:
	@make pre-commit-config
	@make install-requirements

pre-commit-config:
	pre-commit clean
	pre-commit uninstall
	pre-commit install --install-hooks -f
	pre-commit install --hook-type commit-msg

install-requirements:
	pip install -r requirements.txt

test:
	molecule -v test
