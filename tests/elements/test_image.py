from pandas_render.elements import Image


def test_element_image():
    template = Image().render()

    assert template.startswith("<img")
    assert template.endswith("/>")
    assert 'alt="{{ content }}"' in template
    assert 'src="{{ content }}"' in template

    template = Image(
        attribs={
            "style": "background: white",
        }
    ).render()
    assert 'style="background: white"' in template

    template = Image(
        attribs={
            "style": "background: white",
            "title": "{{ content }}",
        }
    ).render()
    assert 'style="background: white"' in template
    assert 'title="{{ content }}"' in template
