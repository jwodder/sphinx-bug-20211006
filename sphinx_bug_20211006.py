def show_in_documentation(x: int) -> str:
    """ I want this function to appear in the documentation. """
    return str(x)

def dont_show_documentation(x: int) -> int:
    """ I do not want this function to appear in the documentation. """
    return x + 42
