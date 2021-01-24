import re

def whole_word_pattern(string: str) -> str:
    """
    Transforms the string 'string' so that a regex search only matches the 
    whole word form of 'string', and not as part of any substring.

    Taken from Felix Kling at https://stackoverflow.com/a/4155064.
    """
    return r"\b" + re.escape(string) + r"\b"


def whole_word_replace(pattern: str, replacement: str, string: str) -> str:
    """
    Replaces all occurences of 'pattern' with 'replacement' in 'string'.

    Will only match whole word occurences of 'pattern'.

    Example:
    >>> whole_word_replace('cat', 'dog', 'It was a catastrofic day for my cat.')
    'It was a catastrofic day for my dog.'
    """
    return re.sub(whole_word_pattern(pattern), replacement, string)

