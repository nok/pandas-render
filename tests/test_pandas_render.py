def test_implicit_initialization():
    from pandas_render import pandas as pd

    assert hasattr(pd.Series, "render")
    assert hasattr(pd.DataFrame, "render")


def test_initialization_with_library():
    from IPython.display import Javascript

    from pandas_render.utils import load

    output = load("alpinejs")
    assert isinstance(output, Javascript)

    alpinejs_output = 'loadScriptSync("alpinejs", "https://unpkg.com/alpinejs");'

    output = load("alpinejs", return_str=True)
    assert isinstance(output, str)
    assert alpinejs_output in output

    output = load(("alpinejs", "https://unpkg.com/alpinejs"), return_str=True)
    assert alpinejs_output in output

    output = load([("alpinejs", "https://unpkg.com/alpinejs")], return_str=True)
    assert alpinejs_output in output

    output = load(["alpinejs", ("vuejs", "https://unpkg.com/vue")], return_str=True)
    assert alpinejs_output in output
    assert 'loadScriptSync("vuejs", "https://unpkg.com/vue")' in output
