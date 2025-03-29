SHELL := /bin/bash

export PYTHONPATH=$(shell pwd)

lint:
	uvx ruff check .

test:
	uv run pytest --cov-report term --cov-report html --cov

setup::
	uv sync --all-extras --all-groups

serve:
	uv run --with jupyter jupyter lab
