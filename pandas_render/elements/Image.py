from typing import Dict, Optional

from pandas_render.base import Element


class Image(Element):
    def __init__(
        self,
        attribs: Optional[Dict[str, str]] = None,
    ):
        if not attribs:
            attribs = {}
        if "src" not in attribs:
            attribs["src"] = "{{ content }}"
        if "loading" not in attribs:
            attribs["loading"] = "lazy"
        super().__init__(
            tag="img",
            attribs=attribs,
        )
