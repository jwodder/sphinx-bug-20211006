"""
MVCE for a bug in Sphinx

Visit <https://github.com/jwodder/sphinx-bug-20211006> for more information.
"""

__version__ = "0.1.0.dev1"
__author__ = "John Thorvald Wodder II"
__author_email__ = "sphinx-bug-20211006@varonathe.org"
__license__ = "MIT"
__url__ = "https://github.com/jwodder/sphinx-bug-20211006"

def show_in_documentation(x: int) -> str:
    """ I want this function to appear in the documentation. """
    return str(x)

def dont_show_documentation(x: int) -> int:
    """ I do not want this function to appear in the documentation. """
    return x + 42
