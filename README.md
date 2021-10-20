# pandas-render

## Development

### Environment

```bash
CFLAGS=-Wno-implicit-function-declaration pyenv install 3.6.2
pyenv global system
pyenv local 3.6.2
poetry config virtualenvs.in-project true
poetry env use 3.6.2
poetry install
poetry run python -m ipykernel install --name pandas-render
```
