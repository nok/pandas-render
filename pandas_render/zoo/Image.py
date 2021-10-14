from typing import Dict

from pandas_render.make.Element import Element


class Image(Element):

    def __init__(self, attribs: Dict[str, str] = {}):
        attribs.update(dict(src='{content}', alt='{content}'))
        super().__init__(tag='img', attribs=attribs)
