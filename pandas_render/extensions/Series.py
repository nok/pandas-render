from typing import Union
from inspect import cleandoc

import pandas as pd  # noqa
from IPython.display import HTML  # noqa
from jinja2 import Template as JinjaTemplate

from pandas_render.base.Element import Element
from pandas_render.extensions import render


def _chunk(sequence, n: int):
    for i in range(0, len(sequence), n):
        yield sequence[i:i + n]


def render_series(self: pd.Series,
                  template: Union[str, Element],
                  n: int = 1,
                  return_str: bool = False) -> Union[str, HTML]:

    # Gather and render data:
    jinja_template = JinjaTemplate(render(template))
    cells = [jinja_template.render(dict(content=cell)) for cell in self]
    rows = list(_chunk(cells, n=max(1, n)))

    template = cleandoc("""
    <table>
        {%- for row in rows -%}
        <tr>
            {%- for cell in row -%}
            <td>{{ cell }}</td>
            {%- endfor -%}
        </tr>
        {%- endfor -%}
    </table>
    """)

    output = JinjaTemplate(template).render(dict(rows=rows))

    if return_str:
        return output

    return HTML(output)
