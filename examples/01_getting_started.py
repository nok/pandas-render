# %% [markdown]
# # pandas-render
#
# ## Getting Started
#
# This example shows how to use pandas-render to create a simple HTML table from a pandas DataFrame. It demonstrates how to use Jinja2 templates to format the content of each cell, and how to create links and images in the table.
#
# ### Import
# Either import pandas with pandas-render explicitly:

# %%
from pandas_render import pandas as pd

# %% [markdown]
# Or import it implicitly after importing pandas:
#
# ```python
# import pandas as pd
# import pandas_render  # noqa
# ```

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
# Here is the original rendering of the DataFrame. It's a simple table with no formatting or styling. It's not very readable, and the data is not very visually appealing.

# %%
df.head()

# %% [markdown]
# ### Rendering
# Now we can use `render` to create a more visually appealing table. The `render` method takes a dictionary of column names and their corresponding templates. Use the placeholder `{{ content }}` to access the content of each cell. Each value is a [Jinja2](https://github.com/pallets/jinja) template with all features (e.g. filters) to format the content.

# %%
df.render(
    templates=dict(
        title="{{ content|upper }}",
        id='<a href="https://www.imdb.com/title/{{ content }}" target="_blank">Link</a>',
        image_url='<img src="{{ content }}" width="100"/>',
        rating="<strong>{{ content }}</strong>",
        actors="<em>{{ content|join(', ') }}</em>",
    ),
)

# %% [markdown]
# ### Filtering and Ordering
# You can also filter the columns to be rendered. By default, all columns are rendered. To filter the columns, set `filter_columns=True`. This will only render the columns that are specified in the `columns` dictionary. In addition to filtering, you can also order the columns. The order of the columns in the `columns` dictionary will be used to determine the order of the columns in the rendered table.

# %%
df.render(
    templates=dict(
        image_url='<img src="{{ content }}" width="100"/>',
        title="{{ content|upper }}",
    ),
    filter_columns=True,
)


# %% [markdown]
# ### Dynamic Placeholder
# You can also use dynamic placeholders in the templates. It means that you can use each name of a column as a placeholder in the template. This allows you to create templates that are more flexible and can be reused for different columns. For example, you can use `{{ content }}` to access the content of the cell, and `{{ title }}` to access the title of the movie or TV series.
# And if you have a column with lists of values, you can use either the filter `join` or a loop to render the content dynamically.

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
    table_column_names=["Image", "Title", "Actors"],
)

# %% [markdown]
# ### Gallery
# If you have just one column to render, you can use the parameter `n` to specify the number of cells to render in each row side by side. This is useful for creating an overview of images or other content. The table head will be hidden automatically.

# %%
df.render(
    templates=dict(
        image_url="""
            <div style="text-align: center;">
                <img src="{{ content }}" width="100"/>
                <p><a href="https://www.imdb.com/title/{{ id }}" target="_blank">{{ title|upper }}</a></p>
                <p><smaller><strong>{{ rating }} ★</strong></smaller></p>
            </div>
        """,
    ),
    filter_columns=True,
    n=2,
)
