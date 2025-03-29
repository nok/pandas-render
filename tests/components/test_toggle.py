from pandas_render.components import Toggle


def test_element_toggle():
    template = Toggle("foobar").render()
    assert "foobar" in template
    assert 'button @click="open = !open"' in template
