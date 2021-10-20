from typing import Optional

import pandas as pd


def init(backend: Optional[str] = None):
    if not hasattr(pd.Series, 'render'):
        from pandas_render.pandas.Series import render
        setattr(pd.Series, 'render', render)

    if not hasattr(pd.DataFrame, 'render'):
        from pandas_render.pandas.DataFrame import render
        setattr(pd.DataFrame, 'render', render)

    if backend and backend == 'alpine':
        from IPython.display import Javascript

        return Javascript("""
            var loadScriptSync = function(src, scope) {{
                if (!scope) {{
                    var script = document.createElement('script');
                    script.src = src;
                    script.type = 'text/javascript';
                    script.async = false;
                    document.getElementsByTagName('head')[0].appendChild(script);
                }}
            }};
            loadScriptSync("{src}", {scope});
        """.format(
            **dict(src='https://unpkg.com/alpinejs@3.4.2/dist/cdn.min.js', scope='window.Alpine')))


__version__ = '0.1.0'
