from typing import Union

from pandas_render.base import Element
from pandas_render.base import Component

from pandas_render.elements import collection as elements_collection
from pandas_render.components import collection as components_collection


def render(something: Union[str, Element, Component, type]) -> str:
    if isinstance(something, str):
        clazz = elements_collection.get(something) or components_collection.get(something)
        if clazz:
            return clazz().render()
        return something

    # Check customized instances:
    for clazz in [Element, Component]:
        if isinstance(something, clazz) and hasattr(something, 'render'):
            return something.render()

    # Check passed classes:
    collection = list(elements_collection.values()) + list(components_collection.values())
    for clazz in collection:
        if issubclass(something, clazz):
            something = something()
            if hasattr(something, 'render'):
                return something.render()

    return '{{ content }}'
