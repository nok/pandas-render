from typing import Union, Dict

import pandas as pd
from IPython.display import HTML

from pandas_render.make.Element import Element
from pandas_render.make import extract


def render(self: pd.DataFrame, columns: Dict[str, Union[str, Element]]):
    formatters = {}
    for column, template in columns.items():
        if column in list(self.columns):
            template = extract(template)
            formatters[column] = lambda x, y=template: y.format(content=x)
    html = self.to_html(escape=False, formatters=formatters)
    return HTML(html)
