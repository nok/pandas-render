SHELL := /bin/bash

export PYTHONPATH=$(shell pwd)

export CONDA_ENV_NAME=pandas-render

yapf:
		$(ACTIVATE_CONDA_ENV) poetry run yapf -i -r pandas_render

pytest:
		$(ACTIVATE_CONDA_ENV) poetry run pytest --cov
