from inspect import cleandoc
from typing import Dict, Union

import pandas as pd
from IPython.display import HTML
from jinja2 import Template as JinjaTemplate

from pandas_render.base import Component, Element
from pandas_render.extensions import render


def render_dataframe(
    self: pd.DataFrame,
    columns: Dict[str, Union[str, Element, Component]],
    filter_columns: bool = False,
    with_thead: bool = True,
    return_str: bool = False,
) -> Union[str, HTML]:
    visible_columns = list(columns.keys()) if filter_columns else list(self.columns)

    # Load templates:
    jinja_templates = {}
    for column, template in columns.items():
        if column in list(self.columns):
            jinja_templates[column] = JinjaTemplate(render(template))

    # Render data:
    rendered_rows = []
    for row in self.to_dict(orient="records"):
        rendered_row = {}
        for column in row.keys():
            if column in visible_columns:
                if column in jinja_templates.keys():
                    values = {"content": row[column]}
                    values.update(row)
                    jinja_template = jinja_templates.get(column)
                    if jinja_template:
                        rendered_row[column] = jinja_template.render(values)
                else:
                    rendered_row[column] = row.get(column)
        rendered_rows.append(rendered_row)

    template = cleandoc("""
    <table class="dataframe" border="1">
        {%- if with_thead -%}
        <thead>
            <tr>
            {%- for column in columns -%}
                <th>{{ column }}</th>
            {%- endfor -%}
            </tr>
        </thead>
        {%- endif -%}
        <tbody>
        {%- for row in rows -%}
            <tr>
            {%- for column in columns -%}
                <td>{{ row[column] }}</td>
            {%- endfor -%}
            </tr>
        {%- endfor -%}
        </tbody>
    </table>
    """)

    output = JinjaTemplate(template).render(
        dict(
            columns=visible_columns,
            rows=rendered_rows,
            with_thead=with_thead,
        )
    )

    if return_str:
        return output

    return HTML(output)
