def test_implicit_initialization():
    import pandas as pd

    from pandas_render import init

    init()

    assert hasattr(pd.Series, "render")
    assert hasattr(pd.DataFrame, "render")


def test_initialization_with_library():
    from IPython.display import Javascript

    from pandas_render import init

    output = init("alpine")
    assert isinstance(output, Javascript)

    alpinejs_output = 'loadScriptSync("alpinejs", "https://unpkg.com/alpinejs");'

    output = init("alpinejs", return_str=True)
    assert isinstance(output, str)
    assert alpinejs_output in output

    output = init(("alpinejs", "https://unpkg.com/alpinejs"), return_str=True)
    assert alpinejs_output in output

    output = init([("alpinejs", "https://unpkg.com/alpinejs")], return_str=True)
    assert alpinejs_output in output

    output = init(["alpinejs", ("vuejs", "https://unpkg.com/vue")], return_str=True)
    assert alpinejs_output in output
    assert 'loadScriptSync("vuejs", "https://unpkg.com/vue")' in output
