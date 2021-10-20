from typing import Union

import pandas as pd
from IPython.display import HTML
from jinja2 import Template as JinjaTemplate

from pandas_render.make.Element import Element
from pandas_render.make import extract


def render(self: pd.Series, template: Union[str, Element], size: int = 1):
    template = JinjaTemplate(extract(template))
    cells = [template.render(dict(content=cell)) for cell in self]

    def _chunks(elements, n: int):
        for i in range(0, len(elements), n):
            yield elements[i:i + n]

    rows = [f'<td>{cell}</td>' for cell in cells]
    rows = list(_chunks(rows, max(1, size)))
    cols = ['<tr>{}</tr>'.format(''.join(row)) for row in rows]
    html = '<table>{}</table>'.format(''.join(cols))

    return HTML(html)
