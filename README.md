<p align="center">
  <img src="https://raw.githubusercontent.com/nok/pandas-render/refs/heads/main/assets/pandas-render.png" alt="pandas-render" height=130>
</p>

<h1 align="center">pandas-render</h1>

<p align="center">Render <a href="https://github.com/pandas-dev/pandas" target="_pandas">pandas</a> or <a href="https://github.com/pola-rs/polars" target="_polars">polars</a> DataFrames and Series as HTML tables with flexibility for formatting and styling.</p>

<div align="center">

![GitHub Repo stars](https://img.shields.io/github/stars/nok/pandas-render)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/nok)

</div>


## Installation

```bash
pip install "pandas-render[pandas]"
```

```bash
pip install "pandas-render[polars]"
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


## Support

Do you like this project? Fuel it with a ☕ coffee on [Ko-fi](https://ko-fi.com/nok). Every little bit helps and means a lot!


## Contributing

We encourage you to contribute to this project! Please check out the [contributing guidelines](CONTRIBUTING.md) about how to proceed.


## License

This package is Open Source Software released under the [BSD-3-Clause](LICENSE) license.
