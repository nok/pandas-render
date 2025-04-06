#!/usr/bin/env bash

cd "$(dirname "$0")"

for py_file in $(find . -type f -name '*.py')
do
  ipynp_file="${py_file%.py}.ipynb"
  echo "$py_file -> $ipynp_file"

  uv run jupytext \
    --from "py:percent" \
    --to "notebook" "$py_file"

  uv run jupyter nbconvert \
    --to notebook \
    --execute "$ipynp_file" \
    --output $(basename -- "$ipynp_file")
done
