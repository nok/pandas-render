from typing import Dict, Optional

from pandas_render.make.Element import Element


class Link(Element):

    def __init__(self,
                 attribs: Optional[Dict[str, str]] = None,
                 text: Optional[str] = '{{ content }}'):
        if not attribs:
            attribs = {}
        attribs.update(dict(href='{{ content }}'))
        super().__init__(tag='a', attribs=attribs, text=text)
