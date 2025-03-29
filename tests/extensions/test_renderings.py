from pandas_render.extensions import render
from pandas_render.elements import Image, Link
from pandas_render.components import Toggle


def test_and_compare_renderings():
    # Test valid shortcuts:
    assert render("image") == render(Image) == render(Image())
    assert render("link") == render(Link) == render(Link())
    assert render("toggle") == render(Toggle) == render(Toggle())

    # Test valid templates:
    example = '<img alt="{{ content }}" src="{{ content }}" />'
    assert render(example) == example

    # Test invalid templates:
    assert render(float) == "{{ content }}"
