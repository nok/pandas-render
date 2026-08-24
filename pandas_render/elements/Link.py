from pandas_render.base import Element


class Link(Element):
    def __init__(
        self,
        attribs: dict[str, str] | None = None,
        text: str | None = "{{ content }}",
    ):
        if not attribs:
            attribs = {}
        if "href" not in attribs:
            attribs["href"] = "{{ content }}"
        if "target" not in attribs:
            attribs["target"] = "_blank"
        super().__init__(
            tag="a",
            attribs=attribs,
            text=text,
        )
