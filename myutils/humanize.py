def clamp(value, format="{:}", floor=None, ceil=None, floor_token="<", ceil_token=">"):
    """Returns number with the specified format, clamped between floor and ceil.
    If the number is larger than ceil or smaller than floor, then the respective limit
    will be returned, formatted and prepended with a token specifying as such.
    Examples:
        ```pycon
        >>> clamp(123.456)
        '123.456'
        >>> clamp(0.0001, floor=0.01)
        '<0.01'
        >>> clamp(0.99, format="{:.0%}", ceil=0.99)
        '99%'
        >>> clamp(0.999, format="{:.0%}", ceil=0.99)
        '>99%'
        >>> clamp(1, format=intword, floor=1e6, floor_token="under ")
        'under 1.0 million'
        >>> clamp(None) is None
        True
        ```
    Args:
        value (int, float): Input number.
        format (str OR callable): Can either be a formatting string, or a callable
        function than receives value and returns a string.
        floor (int, float): Smallest value before clamping.
        ceil (int, float): Largest value before clamping.
        floor_token (str): If value is smaller than floor, token will be prepended
        to output.
        ceil_token (str): If value is larger than ceil, token will be prepended
        to output.
    Returns:
        str: Formatted number. The output is clamped between the indicated floor and
        ceil. If the number if larger than ceil or smaller than floor, the output will
        be prepended with a token indicating as such.
    """
    if value is None:
        return None

    if floor is not None and value < floor:
        value = floor
        token = floor_token
    elif ceil is not None and value > ceil:
        value = ceil
        token = ceil_token
    else:
        token = ""

    if isinstance(format, str):
        return token + format.format(value)
    elif callable(format):
        return token + format(value)
    else:
        raise ValueError(
            "Invalid format. Must be either a valid formatting string, or a function "
            "that accepts value and returns a string."
        )