from collections import namedtuple
from inspect import cleandoc
from typing import List, Tuple, Union

from IPython.display import Javascript
from jinja2 import Template as JinjaTemplate


def load(
    libraries: Union[
        str,
        Tuple[str, str],
        List[Union[str, Tuple[str, str]]],
    ],
    return_str: bool = False,
):
    """Load external JavaScript libraries synchronously."""
    if isinstance(libraries, (str, tuple)):
        libraries = [libraries]

    Library = namedtuple("Library", "name src")
    valid_libraries: List[Library] = []

    for library in libraries:
        if isinstance(library, str):
            if library == "alpinejs":
                library = Library(
                    name="alpinejs",
                    src="https://unpkg.com/alpinejs",
                )
                valid_libraries.append(library)
        else:
            if isinstance(library, tuple):
                library = Library(name=library[0], src=library[1])
                valid_libraries.append(library)

    template = JinjaTemplate(
        cleandoc("""
        var loadScriptSync = function(name, src) {
            if (document.querySelector('script[data-pandas-render-library="' + name + '"]')) {
                return;
            }
            var script = document.createElement('script');
            script.src = src;
            script.type = 'text/javascript';
            script.async = false;
            script.setAttribute("data-pandas-render-library", name);
            document.getElementsByTagName('head')[0].appendChild(script);
        };
        {%- for library in libraries -%}
        loadScriptSync("{{ library.name }}", "{{ library.src }}");
        {%- endfor -%}
    """),
        autoescape=False,
    )

    output = ""
    if len(valid_libraries) > 0:
        output = template.render(libraries=valid_libraries)

    if return_str:
        return output

    return Javascript(output)


def _chunk(sequence, n: int):
    for i in range(0, len(sequence), n):
        yield sequence[i : i + n]
