from __future__ import annotations

from typing import Union


def _extend(package: Union["pandas", "polars"]):
    # Extend pandas.Series with `render` method:
    if not hasattr(package.Series, "render"):
        from pandas_render.extensions.Series import render_series

        setattr(package.Series, "render", render_series)

    # Extend pandas.DataFrame with `render` method:
    if not hasattr(package.DataFrame, "render"):
        from pandas_render.extensions.DataFrame import render_dataframe

        setattr(package.DataFrame, "render", render_dataframe)


try:
    import pandas
except ImportError:
    pass
else:
    _extend(pandas)

try:
    import polars
except ImportError:
    pass
else:
    _extend(polars)

__version__ = "0.4.0"
