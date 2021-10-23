from typing import Dict, Optional

from pandas_render.base import Element


class Image(Element):

    def __init__(self, attribs: Optional[Dict[str, str]] = None):
        if not attribs:
            attribs = {}
        attribs.update(dict(alt='{{ content }}', src='{{ content }}'))
        super().__init__(tag='img', attribs=attribs)
