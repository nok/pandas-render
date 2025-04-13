from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def render():
    print("Render dataframe")


@app.command()
def serve(
    host: str = "0.0.0.0",
    port: int = 8080,
    directory: Annotated[str, Path, typer.Argument()] = Path.cwd(),
):
    if not directory:
        directory = Path.cwd()

    if not isinstance(directory, Path):
        directory = Path(directory)

    assert directory.exists() and directory.is_dir()

    directory = str(directory.resolve().absolute())

    handler = partial(SimpleHTTPRequestHandler, directory=directory)
    server = ThreadingHTTPServer((host, port), handler)

    print(f"Serving files at http://{host}:{port} ... (ctrl+c to stop)")

    server.serve_forever()
