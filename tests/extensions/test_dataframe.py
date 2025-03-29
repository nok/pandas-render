import pytest

import pandas as pd
from pandas_render import init

from IPython.display import HTML

init()


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
    table = df.render(
        dict(
            name="{{ content|upper }}",
            foobar="{{ content }}",
        ),
        return_str=True,
    )
    for name in ["ANNA", "BOB", "CHRISTIAN"]:
        assert name in table
    assert "foobar" not in table

    table = df.render(
        dict(
            age="{{ content }}",
        ),
        filter_columns=True,
        return_str=True,
    )
    assert "Anna" not in table

    table = df.render(
        dict(
            name="{{ content|upper }}",
            age="{{ content }}",
        )
    )
    assert isinstance(table, HTML)
