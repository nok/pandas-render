from typing import Dict, Optional

from xml.etree.ElementTree import Element as XmlElement
from xml.etree.ElementTree import tostring


class Element:

    def __init__(self, tag: str, attribs=Dict[str, str], text: Optional[str] = None):
        element = XmlElement(tag, attrib=attribs)
        element.text = text if text else None
        self.element = element

    def render(self) -> str:
        return tostring(self.element).decode()
