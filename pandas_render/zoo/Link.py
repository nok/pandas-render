from typing import Dict, Optional

from pandas_render.make.Element import Element


class Link(Element):

    def __init__(self,
                 attribs: Dict[str, str] = {},
                 text: Optional[str] = '{content}'):
        attribs.update(dict(href='{content}'))
        super().__init__(tag='a', attribs=attribs, text=text)
