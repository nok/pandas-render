from pandas_render.elements import Link


def test_element_link():
    template = Link().render()
    assert 'href="{{ content }}"' in template

    template = Link(
        attribs={
            "target": "{{ content }}",
        }
    ).render()
    assert 'target="{{ content }}"' in template
    assert 'href="{{ content }}"' in template
