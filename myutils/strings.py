def clip(string: str, length: int, suffix = "...") -> str:
    """Clip string to max length
    
    If input `string` has less than `length` characters, then return the original string.
    
    If `length` is less than the number of charecters in `suffix`, then return `string` 
    truncated to `length`.
    
    Otherwise returns truncated string with suffix appended, such that the resulting 
    string has `length` characters.

    Args:
        string (str): String to clip
        length (int): Max chars in output string
        suffix (str, optional): String appended to output if original string is clipped. Defaults to "...".

    Returns:
        str: Clipped string
    """

    if len(string) <= length:
        return string
    
    if length < len(suffix):
        return string[:length]
    
    return string[:length - len(suffix)] + suffix
    
