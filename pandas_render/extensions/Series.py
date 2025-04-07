from inspect import cleandoc
from typing import List, Optional, Union

import pandas as pd
from IPython.display import HTML
from jinja2 import Template as JinjaTemplate

from pandas_render.base.Element import Element
from pandas_render.extensions import render
from pandas_render.utils import _chunk


def render_series(
    self: pd.Series,
    template: Union[str, Element],
    table_css_classes: Optional[List[str]] = ["dataframe"],
    n: int = 1,
    return_str: bool = False,
) -> Union[str, HTML]:
    # Gather and render data:
    jinja_template = JinjaTemplate(render(template))
    cells = [jinja_template.render(dict(content=cell)) for cell in self]
    rows = list(_chunk(cells, n=max(1, n)))

    template = cleandoc("""
    <table {% if table_css_classes %}class="{{ table_css_classes|join(' ') }}"{% endif %}>
        {%- for row in rows -%}
        <tr>
            {%- for cell in row -%}
            <td>{{ cell }}</td>
            {%- endfor -%}
        </tr>
        {%- endfor -%}
    </table>
    """)

    output = JinjaTemplate(template).render(
        dict(
            rows=rows,
            table_css_classes=table_css_classes,
        )
    )

    if return_str:
        return output

    return HTML(output)
