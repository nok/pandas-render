from pandas_render.elements import Image


def test_element_image():

    template = Image().render()
    assert template == '<img alt="{{ content }}" src="{{ content }}" />'

    template = Image(attribs={
        'style': 'background: white'
    }).render()
    assert template == '<img alt="{{ content }}" src="{{ content }}" style="background: white" />'

    template = Image(attribs={
        'style': 'background: white',
        'title': '{{ content }}'
    }).render()
    assert template == '<img alt="{{ content }}" src="{{ content }}" style="background: white" title="{{ content }}" />'
