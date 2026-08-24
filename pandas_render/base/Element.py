from xml.etree.ElementTree import Element as XmlElement
from xml.etree.ElementTree import tostring


class Element:
    def __init__(
        self,
        tag: str,
        attribs=dict[str, str],
        text: str | None = None,
    ):
        element = XmlElement(tag, attrib=attribs)
        element.text = text if text else None
        self.element = element

    def render(self) -> str:
        return tostring(self.element).decode()
