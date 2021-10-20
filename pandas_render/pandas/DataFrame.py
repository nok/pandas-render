from typing import Union, Dict

import pandas as pd
from IPython.display import HTML
from jinja2 import Template as JinjaTemplate

from pandas_render.make.Element import Element
from pandas_render.make import extract


def render(self: pd.DataFrame, columns: Dict[str, Union[str, Element]]):

    # Load templates:
    templates = {}
    for column, template in columns.items():
        if column in list(self.columns):
            templates[column] = JinjaTemplate(extract(template))

    # Update entries:
    outs = []
    for row in self.to_dict(orient='records'):
        entry = {}
        for column in row.keys():
            if column in templates.keys():
                values = {'content': row[column]}
                values.update(row)
                entry[column] = templates.get(column).render(values)
            else:
                entry[column] = row.get(column)
        outs.append(entry)

    html = '''
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
    '''
    return HTML(JinjaTemplate(html).render(dict(columns=list(self.columns), rows=outs)))
