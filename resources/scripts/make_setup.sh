#!/usr/bin/env bash

ROOT_DIR="$(cd "$(dirname "$0")/../.."; pwd -P)"
cd "$ROOT_DIR"

#CFLAGS=-Wno-implicit-function-declaration pyenv install 3.6.2
pyenv local 3.6.2
poetry config virtualenvs.in-project true
poetry env use 3.6.2
poetry install
poetry run python -m ipykernel install --name pandas-render
