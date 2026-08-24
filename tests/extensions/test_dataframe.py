import pytest
from IPython.display import HTML

from pandas_render import pandas as pd


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"name": "Anna", "age": 20},
            {"name": "Bob", "age": 30},
            {"name": "Christian", "age": 40},
        ]
    )


def test_content(df: pd.DataFrame):
    table = df.render(
        {
            "name": "{{ content|upper }}",
            "foobar": "{{ content }}",
        },
        return_str=True,
    )
    for name in ["ANNA", "BOB", "CHRISTIAN"]:
        assert name in table
    assert "foobar" not in table

    table = df.render(
        {
            "age": "{{ content }}",
        },
        filter_columns=True,
        return_str=True,
    )
    assert "Anna" not in table

    table = df.render(
        {
            "name": "{{ content|upper }}",
            "age": "{{ content }}",
        }
    )
    assert isinstance(table, HTML)
