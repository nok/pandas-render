SHELL := /bin/bash

export PYTHONPATH=$(shell pwd)

lint:
	uvx ruff check .

test:
	uv run pytest --cov --cov-report term --cov-report html -n auto tests

setup::
	uv sync --all-groups

serve:
	uv run --with jupyter jupyter lab

build:
	uvx hatch build
