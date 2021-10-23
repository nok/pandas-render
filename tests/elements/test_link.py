from pandas_render.elements import Link


def test_element_link():

    template = Link().render()
    assert template == '<a href="{{ content }}">{{ content }}</a>'

    template = Link(attribs={
        'target': '{{ content }}'
    }).render()
    assert template == '<a href="{{ content }}" target="{{ content }}">{{ content }}</a>'
