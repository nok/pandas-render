from inspect import cleandoc
from typing import Dict, List, Optional, Union

import pandas as pd
from IPython.display import HTML
from jinja2 import Template as JinjaTemplate

from pandas_render.base import Component, Element
from pandas_render.extensions import render
from pandas_render.utils import _chunk


def render_dataframe(
    self: pd.DataFrame,
    templates: Dict[str, Union[str, Element, Component]],
    filter_columns: bool = False,
    custom_columns_names: Optional[List[str]] = None,
    with_thead: bool = True,
    n: Optional[int] = None,
    return_str: bool = False,
) -> Union[str, HTML]:
    # Determine relevant columns:
    if filter_columns:
        visible_columns = list(templates.keys())
    else:
        visible_columns = [col for col in templates.keys() if col in self.columns] + [
            col for col in self.columns if col not in templates.keys()
        ]

    # Overwrite column names if custom names are provided:
    if custom_columns_names and len(custom_columns_names) == len(visible_columns):
        column_names = custom_columns_names
    else:
        column_names = visible_columns

    # Load templates:
    jinja_templates = {}
    for column, template in templates.items():
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

    if (
        n is not None
        and isinstance(n, int)
        and len(visible_columns) == 1
        and visible_columns[0] in rendered_rows[0].keys()
    ):
        # Render content as gallery:
        visible_column = visible_columns[0]
        cells = [row[visible_column] for row in rendered_rows]
        rendered_rows = list(_chunk(cells, n=max(1, n)))

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
    else:
        # Render content as table:
        template = cleandoc("""
        <table class="dataframe" border="1">
            {%- if with_thead -%}
            <thead>
                <tr>
                {%- for column_name in column_names -%}
                    <th>{{ column_name }}</th>
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
            column_names=column_names,
            rows=rendered_rows,
            with_thead=with_thead,
        )
    )

    if return_str:
        return output

    return HTML(output)
