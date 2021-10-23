def test_version():
    from pandas_render import __version__
    assert __version__ == '0.1.0'


def test_implicit_initialization():
    import pandas_render  # noqa
    import pandas  # noqa

    assert hasattr(pandas.Series, 'render')
    assert hasattr(pandas.DataFrame, 'render')
