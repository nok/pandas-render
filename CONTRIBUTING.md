## Development

We rely on [uv](https://docs.astral.sh/uv/) for package management. Ensure uv is installed before proceeding.

In addition we follow the [Conventional Commits](https://www.conventionalcommits.org/) standard to maintain a clear and organized commit history.

### Environment

To create a new local environment in `./.venv`, run:
```bash
uv sync --all-groups
```

Alternatively, execute:
```bash
make setup
```

Both commands will set up your environment with the necessary dependencies.

### Testing

To run all unit tests based on [pytest](https://github.com/pytest-dev/pytest/), run:
```bash
uv run pytest --cov-report term --cov-report html --cov
```

Alternatively, execute:
```bash
make test
```

### Linting

We use [ruff](https://github.com/astral-sh/ruff) for linting.

Install ruff using:
```bash
uv tool install ruff
```

Run the following command to analyze linting issues:
```bash
uvx ruff check .
```

Alternatively, execute:
```bash
make lint
```
