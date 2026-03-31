def greet_names(names: list[str]) -> list[str]:

    """ Recebe uma lista de nomes e retorna uma lista de saudações."""

    return [f"Hello, {nome}!" for nome in names]
    """
    Retorna uma lista de saudações para cada nome.

    Args:
        names (list[str]): lista de nomes

    Returns:
        list[str]: lista com mensagens "Hello, <name>!"
    """
    pass
