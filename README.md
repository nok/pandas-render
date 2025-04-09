# pandas-render

[pandas-render](https://github.com/nok/pandas-render) is a [pandas](https://github.com/pandas-dev/pandas) and [polars](https://github.com/pola-rs/polars) extension for rendering DataFrames and Series as HTML tables, with support for custom styling and formatting.


## Installation

```bash
pip install pandas-render[pandas]
```

```bash
pip install pandas-render[polars]
```


## Usage

This is a simple example that demonstrates the basic functionality. The column names are used to match individual [Jinja2](https://github.com/pallets/jinja) templates. And `{{ content }}` is the placeholder for the content of the original cell.

```python
from pandas_render import pandas as pd

df = pd.DataFrame(
    [
        dict(name="Alice", age=25, hobbies=["coding"]),
        dict(name="Bob", age=30, hobbies=["reading", "hiking"]),
    ]
)

df.render(
    templates=dict(
        name="<strong>{{ content }}</strong>",
        age="{{ content }} years old",
        hobbies="<em>{{ content|join(', ') }}</em>",
    ),
    table_column_names=["Name", "Age", "Hobbies"],
)
```

The result is a rendered dataframe:

<table class="dataframe"><thead><tr><th>Name</th><th>Age</th><th>Hobbies</th></tr></thead><tbody><tr><td><strong>Alice</strong></td><td>25 years old</td><td><em>coding</em></td></tr><tr><td><strong>Bob</strong></td><td>30 years old</td><td><em>reading, hiking</em></td></tr></tbody></table>


## Examples

Exciting and more powerful features can be explored and learned in the [Getting Started](examples/01_getting_started.ipynb) notebook.

List of all notebooks with examples:

- [Getting Started](examples/01_getting_started.ipynb) ✨
- [Components](examples/02_components.ipynb)


## Contributing

We encourage you to contribute to this project! Please check out the [contributing guidelines](CONTRIBUTING.md) about how to proceed.


## License

This package is Open Source Software released under the [BSD-3-Clause](LICENSE) license.
