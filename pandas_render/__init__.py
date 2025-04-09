try:
    import pandas
except ImportError:
    pass
else:
    # Extend pandas.Series with `render` method:
    if not hasattr(pandas.Series, "render"):
        from pandas_render.extensions.Series import render_series

        setattr(pandas.Series, "render", render_series)

    # Extend pandas.DataFrame with `render` method:
    if not hasattr(pandas.DataFrame, "render"):
        from pandas_render.extensions.DataFrame import render_dataframe

        setattr(pandas.DataFrame, "render", render_dataframe)

__version__ = "0.2.1"
