from pandas_render.make.Template import Template


class Toggle(Template):

    def __init__(self, content: str, show: str = 'Show', hide: str = 'Hide'):
        template = """
        <div x-data="{{{{ open: false }}}}" style="text-align: center;">
            <div x-show="open">
                {content}
            </div>
            <button @click="open = !open" x-text="open ? '{hide}': '{show}'"></button>
        </div>
        """.format(**dict(
            content=content,
            show=show,
            hide=hide,
        ))
        super().__init__(template=template)
