import pytest
from IPython.display import HTML

from pandas_render import pandas as pd


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.DataFrame(
        [
            dict(name="Anna", age=20),
            dict(name="Bob", age=30),
            dict(name="Christian", age=40),
        ]
    )


def test_content(df: pd.DataFrame):
    table = df["name"].render("{{ content }}", n=2, return_str=True)
    assert table.count("<tr>") == 2

    assert "Anna" in table and "Bob" in table and "Christian" in table

    table = df["name"].render("{{ content }}", n=2)
    assert isinstance(table, HTML)
