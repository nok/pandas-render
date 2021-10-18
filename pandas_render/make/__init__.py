from typing import Union

from .Element import Element

from ..elements import Image
from ..elements import Link

elements = dict(image=Image, link=Link)


def extract(template: Union[str, Element]) -> str:
    if isinstance(template, str):
        if template in elements.keys():
            template = elements.get(template)
            template = template()
            return template.render()
        return template

    if isinstance(template, Element):
        return template.render()

    if issubclass(template, Element):
        template = template()
        return template.render()
