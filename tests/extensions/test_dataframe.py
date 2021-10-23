import pytest

import pandas as pd  # noqa
import pandas_render  # noqa

from IPython.display import HTML  # noqa


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.DataFrame([
        dict(name='Anna', age=20),
        dict(name='Bob', age=30),
        dict(name='Christian', age=40),
    ])


def test_content(df: pd.DataFrame):
    table = df.render(dict(
        name='{{ content|upper }}',
        foobar='{{ content }}',
    ), return_str=True)

    assert \
        'ANNA' in table and \
        'BOB' in table and \
        'CHRISTIAN' in table

    assert 'foobar' not in table

    table = df.render(dict(
        name='{{ content|upper }}',
        age='{{ content }}',
    ))
    assert type(table) == HTML
