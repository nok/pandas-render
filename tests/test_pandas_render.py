def test_version():
    from pandas_render import __version__

    assert __version__ == "0.2.1"


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

    alpine = "https://unpkg.com/alpinejs@3.4.2/dist/cdn.min.js"

    output = init("alpine", return_str=True)
    assert isinstance(output, str)
    assert f'loadScriptSync("{alpine}", window.Alpine);' in output

    output = init((alpine, "window.Alpine"), return_str=True)
    assert f'loadScriptSync("{alpine}", window.Alpine);' in output

    output = init([(alpine, "window.Alpine")], return_str=True)
    assert f'loadScriptSync("{alpine}", window.Alpine);' in output

    output = init(alpine, return_str=True)
    assert f'loadScriptSync("{alpine}", null);' in output

    output = init(["alpine", ("a.js", "window.a"), "b.js"], return_str=True)
    assert f'loadScriptSync("{alpine}", window.Alpine);' in output
    assert 'loadScriptSync("a.js", window.a);' in output
    assert 'loadScriptSync("b.js", null);' in output
