from typing import Optional, Union, List, Tuple
from collections import namedtuple
from inspect import cleandoc

from IPython.display import Javascript  # noqa
from jinja2 import Template as JinjaTemplate
import pandas  # noqa


def _handle_extensions():
    if not hasattr(pandas.Series, 'render'):
        from pandas_render.extensions.Series import render_series
        setattr(pandas.Series, 'render', render_series)

    if not hasattr(pandas.DataFrame, 'render'):
        from pandas_render.extensions.DataFrame import render_dataframe
        setattr(pandas.DataFrame, 'render', render_dataframe)


def _handle_libraries(
        libraries: Union[str, Tuple[str, str], List[Union[str, Tuple[str, str]]]]) -> str:
    Library = namedtuple('Library', 'src scope')

    if isinstance(libraries, (str, tuple)):
        libraries = [libraries]

    valid_libraries: List[Library] = []
    if isinstance(libraries, list):
        for library in libraries:
            if isinstance(library, str):
                if library == 'alpine':
                    library = Library(
                        src='https://unpkg.com/alpinejs@3.4.2/dist/cdn.min.js',
                        scope='window.Alpine')
                else:
                    library = Library(src=library, scope='null')
            elif isinstance(library, tuple) and len(library) >= 2:
                library = Library(src=library[0], scope=library[1])

            if isinstance(library, Library):
                valid_libraries.append(library)

    template = JinjaTemplate(
        cleandoc("""
        var loadScriptSync = function(src, scope) {
            if (scope != null && !scope) {
                var script = document.createElement('script');
                script.src = src;
                script.type = 'text/javascript';
                script.async = false;
                document.getElementsByTagName('head')[0].appendChild(script);
            }
        };
        {%- for library in libraries -%}
        loadScriptSync("{{ library.src }}", {{ library.scope }});
        {%- endfor -%}
    """))

    output = ''
    if len(valid_libraries):
        output = template.render(libraries=valid_libraries)
    return output


def init(libraries: Optional[Union[str, Tuple[str, str], List[Union[str, Tuple[str, str]]]]] = None,
         return_str: bool = False) -> Optional[Union[str, Javascript]]:
    _handle_extensions()
    if libraries:
        output = _handle_libraries(libraries)
        if return_str:
            return output
        return Javascript(output)
    return None


init()  # default initialization without any additional libraries

__version__ = '0.2.1'
