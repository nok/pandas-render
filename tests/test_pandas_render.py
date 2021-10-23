def test_version():
    from pandas_render import __version__
    assert __version__ == '0.1.0'


def test_implicit_initialization():
    import pandas_render  # noqa
    import pandas  # noqa

    assert hasattr(pandas.Series, 'render')
    assert hasattr(pandas.DataFrame, 'render')


def test_initialization_with_library():
    from IPython.display import Javascript  # noqa
    from pandas_render import init  # noqa

    output = init('alpine')
    assert type(output) == Javascript

    alpine = 'https://unpkg.com/alpinejs@3.4.2/dist/cdn.min.js'

    output = init('alpine', return_str=True)
    assert type(output) == str
    assert f'loadScriptSync("{alpine}", window.Alpine);' in output

    output = init((alpine, 'window.Alpine'), return_str=True)
    assert f'loadScriptSync("{alpine}", window.Alpine);' in output

    output = init([(alpine, 'window.Alpine')], return_str=True)
    assert f'loadScriptSync("{alpine}", window.Alpine);' in output

    output = init(alpine, return_str=True)
    assert f'loadScriptSync("{alpine}", null);' in output

    output = init(['alpine', ('a.js', 'window.a'), 'b.js'], return_str=True)
    assert f'loadScriptSync("{alpine}", window.Alpine);' in output
    assert f'loadScriptSync("a.js", window.a);' in output
    assert f'loadScriptSync("b.js", null);' in output
