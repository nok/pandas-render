# %% [markdown]
# # pandas-render
#
# [pandas-render](https://github.com/nok/pandas-render) is a [pandas](https://github.com/pandas-dev/pandas) extension for rendering DataFrames and Series as HTML tables, with support for custom styling and formatting.
#
# Installation:
#
# ```bash
# pip install pandas-render
# ```
#
# ## Components
#
# ### Import
# Import pandas with pandas-render explicitly:

# %%
from pandas_render import pandas as pd

# %% [markdown]
# ### Data
# Create a DataFrame with some sample data. The DataFrame contains information about TV series and movies.

# %%
df = pd.DataFrame(
    [
        dict(
            title="Severance",
            id="tt11280740",
            year=2022,
            image_url="https://m.media-amazon.com/images/M/MV5BZDI5YzJhODQtMzQyNy00YWNmLWIxMjUtNDBjNjA5YWRjMzExXkEyXkFqcGc@._V1_QL75_UX380_CR0,4,380,562_.jpg",
            rating=8.7,
            actors=["Adam Scott", "Britt Lower", "Zach Cherry"],
        ),
        dict(
            title="Stranger Things",
            id="tt4574334",
            year=2016,
            image_url="https://m.media-amazon.com/images/M/MV5BMjg2NmM0MTEtYWY2Yy00NmFlLTllNTMtMjVkZjEwMGVlNzdjXkEyXkFqcGc@._V1_QL75_UX380_CR0,0,380,562_.jpg",
            rating=8.6,
            actors=["Millie Bobby Brown", "Finn Wolfhard"],
        ),
        dict(
            title="Python",
            id="tt0209264",
            year=2000,
            image_url="https://m.media-amazon.com/images/M/MV5BZWUwNjExYTYtZmM3ZS00NzA1LWJhNjYtMWExNGEwZTVjNDM3XkEyXkFqcGc@._V1_QL75_UY562_CR8,0,380,562_.jpg",
            rating=3.7,
            actors=["Frayne Rosanoff"],
        ),
    ]
)

# %% [markdown]
# ### Rendering
# Just like in the first example, we can render the DataFrame as an HTML table.

# %%
title_template = """
<p><a href="https://www.imdb.com/title/{{ id }}" target="_blank">{{ content|upper }}</a></p>
<p><smaller>Year: {{ year }}</smaller></p>
<p><smaller>Rating: <strong>{{ rating }}</strong></smaller></p>
"""

actors_template = """
{% if content %}
    {% for actor in content %}
        <p>{{ actor }}</p>
    {% endfor %}
{% else %}
    <p>No actors</p>
{% endif %}
"""

df.render(
    templates=dict(
        image_url='<img src="{{ content }}" width="100"/>',
        title=title_template,
        actors=actors_template,
    ),
    filter_columns=True,
)

# %% [markdown]
# ### Toggle Component
# The `Toggle` component is a simple toggle switch that can be used to show or hide content. It can be used to create interactive elements in your HTML table. First of all we need to load the `alpinejs` library. This is a JavaScript library that provides the functionality for the toggle component. The `load` function loads the library and makes it available for use in the HTML table.

# %%
from pandas_render import load

load(libraries="alpinejs")

# %%
from pandas_render.components import Toggle

df.render(
    templates=dict(
        image_url='<img src="{{ content }}" width="100"/>',
        title=title_template,
        actors=Toggle(actors_template),
    ),
    filter_columns=True,
)
