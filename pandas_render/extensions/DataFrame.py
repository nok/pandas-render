from __future__ import annotations

from inspect import cleandoc, signature
from typing import Dict, List, Optional, Union

from IPython.display import HTML
from jinja2 import Template as JinjaTemplate

from pandas_render.base import Component, Element
from pandas_render.extensions import render
from pandas_render.utils import _chunk

try:
    import pandas as pd
except ImportError:
    pass

try:
    import polars as pl
except ImportError:
    pass


def render_dataframe(
    self: Union["pd.DataFrame", "pl.DataFrame"],
    templates: Dict[str, Union[str, Element, Component]],
    filter_columns: bool = False,
    table_with_thead: bool = True,
    table_column_names: Optional[List[str]] = None,
    table_css_classes: Optional[List[str]] = ["dataframe"],
    n: Optional[int] = None,
    return_str: bool = False,
) -> Union[str, HTML]:
    # Determine relevant columns:
    if filter_columns:
        column_names = list(templates.keys())
    else:
        column_names = [col for col in templates.keys() if col in self.columns] + [
            col for col in self.columns if col not in templates.keys()
        ]

    # Overwrite column names if custom names are provided:
    if table_column_names is None or len(table_column_names) != len(column_names):
        table_column_names = column_names

    # Load templates:
    jinja_templates = {}
    for column, template in templates.items():
        if column in list(self.columns):
            jinja_templates[column] = JinjaTemplate(render(template))

    # Convert data:
    if hasattr(self, "to_dict"):
        sig = signature(self.to_dict)
        if "orient" in sig.parameters:
            rows = self.to_dict(orient="records")
        elif "as_series" in sig.parameters:
            rows = self.to_dict(as_series=False)
            rows = [dict(zip(rows, record)) for record in zip(*rows.values())]
        else:
            raise ValueError("Unsupported to_dict signature.")
    else:
        raise ValueError("Unsupported DataFrame type.")

    # Render data:
    rendered_rows = []
    for row in rows:
        rendered_row = {}
        for column in row.keys():
            if column in column_names:
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
        and len(column_names) == 1
        and column_names[0] in rendered_rows[0].keys()
    ):
        # Render content as gallery:
        column_name = column_names[0]
        cells = [row[column_name] for row in rendered_rows]
        rendered_rows = list(_chunk(cells, n=max(1, n)))

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
    else:
        # Render content as table:
        template = cleandoc("""
        <table {% if table_css_classes %}class="{{ table_css_classes|join(' ') }}"{% endif %}>
            {%- if table_with_thead -%}
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
            columns=column_names,
            column_names=table_column_names,
            rows=rendered_rows,
            table_with_thead=table_with_thead,
            table_css_classes=table_css_classes,
        )
    )

    if return_str:
        return output

    return HTML(output)
