from inspect import cleandoc

from jinja2 import Template as JinjaTemplate

from pandas_render.base import Component


class Toggle(Component):

    def __init__(self,
                 content: str = '{{ content }}',
                 is_open: bool = False,
                 show: str = 'Show',
                 hide: str = 'Hide'):
        template = cleandoc("""
        <div x-data="{ open: {{ is_open }} }" style="text-align: center;">
            <div x-show="open">
                {{ content }}
            </div>
            <button @click="open = !open" x-text="open ? '{{ hide }}': '{{ show }}'"></button>
        </div>
        """)

        output = JinjaTemplate(template).render(
            dict(
                is_open='true' if is_open else 'false',
                content=content,
                show=show,
                hide=hide,
            ))

        super().__init__(template=output)
