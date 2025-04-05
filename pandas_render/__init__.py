from collections import namedtuple
from inspect import cleandoc
from typing import List, Optional, Tuple, Union

import pandas  # noqa
from IPython.display import Javascript  # noqa
from jinja2 import Template as JinjaTemplate


def _handle_extensions():
    if not hasattr(pandas.Series, "render"):
        from pandas_render.extensions.Series import render_series

        setattr(pandas.Series, "render", render_series)

    if not hasattr(pandas.DataFrame, "render"):
        from pandas_render.extensions.DataFrame import render_dataframe

        setattr(pandas.DataFrame, "render", render_dataframe)


def _handle_libraries(
    libraries: Union[str, Tuple[str, str], List[Union[str, Tuple[str, str]]]],
) -> str:
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
    return output


def init(
    libraries: Optional[
        Union[str, Tuple[str, str], List[Union[str, Tuple[str, str]]]]
    ] = None,
    return_str: bool = False,
) -> Optional[Union[str, Javascript]]:
    _handle_extensions()
    if libraries:
        output = _handle_libraries(libraries)
        if return_str:
            return output
        return Javascript(output)
    return None


init()  # default initialization without any additional libraries

__version__ = "0.2.1"
