def sierpinski(layers: int) -> str:
    """
    Generates a Sierpinski triangle with a given number of layers as a string.

    Args:
        layers (int): Number of layers in the triangle.

    Returns:
        str: The Sierpinski triangle as a string.

    Example:
        >>> print(sierpinski(2))
        "L\nLL\nL L\nLLLL\n"
    """
    s = ""
    for i in range(1 << layers):
        for j in range(i + 1):
            s += " " if j & ~i else "L"
        s += "\n"
    return s

def print_sierpinski(layers: int) -> None:
    """
    Prints a Sierpinski triangle with a given number of layers to stdout.

    Args:
        layers (int): Number of layers in the triangle.

    Example:
        >>> print_sierpinski(2)
        L
        LL
        L L
        LLLL
    """
    print(sierpinski(layers), end="")