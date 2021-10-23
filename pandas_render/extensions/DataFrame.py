from typing import Union, Dict
from inspect import cleandoc

import pandas as pd  # noqa
from IPython.display import HTML  # noqa
from jinja2 import Template as JinjaTemplate

from pandas_render.make.Element import Element
from pandas_render.make.Template import Template
from pandas_render.make import extract


def render(self: pd.DataFrame,
           columns: Dict[str, Union[str, Element, Template]],
           return_str: bool = False) -> Union[str, HTML]:

    # Load templates:
    jinja_templates = {}
    for column, template in columns.items():
        if column in list(self.columns):
            jinja_templates[column] = JinjaTemplate(extract(template))

    # Render data:
    rendered_rows = []
    for row in self.to_dict(orient='records'):
        rendered_row = {}
        for column in row.keys():
            if column in jinja_templates.keys():
                values = {'content': row[column]}
                values.update(row)
                jinja_template = jinja_templates.get(column)
                if jinja_template and isinstance(jinja_template, JinjaTemplate):
                    rendered_row[column] = jinja_template.render(values)
                else:
                    rendered_row[column] = row.get(column)
            else:
                rendered_row[column] = row.get(column)
        rendered_rows.append(rendered_row)

    template = cleandoc('''
    <table class="dataframe" border="1">
        <thead>
            <tr>
            {% for column in columns %}
                <th>{{ column }}</th>
            {% endfor %}
            </tr>
        </thead>
        <tbody>
        {% for row in rows %}
            <tr>
            {% for column in columns %}
                <td>{{ row[column] }}</td>
            {% endfor %}
            </tr>
        {% endfor %}
        </tbody>
    </table>
    ''')

    output = JinjaTemplate(template).render(dict(columns=list(self.columns), rows=rendered_rows))

    if return_str:
        return output

    return HTML(output)
