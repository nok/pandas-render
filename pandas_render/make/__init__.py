from typing import Union

from pandas_render.make.Element import Element
from pandas_render.make.Template import Template

from pandas_render.elements import Image, Link
from pandas_render.templates import Toggle

elements = dict(image=Image, link=Link)


def extract(template: Union[str, Element, Template, type]) -> str:
    if isinstance(template, str):
        if template in elements.keys():
            template = elements.get(template)
            template = template()
            return template.render()
        return template

    for clazz in [Element, Template]:
        if isinstance(template, clazz):
            return template.render()

    for clazz in [Image, Link, Toggle]:
        if issubclass(template, clazz):
            template = template()
            return template.render()
