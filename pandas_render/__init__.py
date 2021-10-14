import pandas as pd


def init():
    if not hasattr(pd.Series, 'render'):
        from pandas_render.pandas.Series import render
        setattr(pd.Series, 'render', render)

    if not hasattr(pd.DataFrame, 'render'):
        from pandas_render.pandas.DataFrame import render
        setattr(pd.DataFrame, 'render', render)


__version__ = '0.1.0'
