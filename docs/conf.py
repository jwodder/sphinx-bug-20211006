from sphinx_bug_20211006 import __version__

project = "sphinx-bug-20211006"
author = "John Thorvald Wodder II"
copyright = "2021 John Thorvald Wodder II"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

exclude_patterns = ["_build"]
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
version = __version__
release = __version__
today_fmt = "%Y %b %d"
default_role = "py:obj"
pygments_style = "sphinx"
todo_include_todos = True

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "prev_next_buttons_location": "both",
}
html_last_updated_fmt = "%Y %b %d"
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True