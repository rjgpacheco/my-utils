"""
Collection of utilities I use often.

Some are just ways I like calling specific functions.
"""

import re
import numpy as np

def chunks(lst, n):
    """
    Splits lst into n chunks.
    
    Taken from Jason Mitchell at https://stackoverflow.com/a/29679492.
    """
    return [list(x) for x in np.array_split(lst, n)]


def chunks_n(lst, n):
    """
    Yield successive n-sized chunks from lst.
    
    Taken from Ned Batchelder at https://stackoverflow.com/a/312464.
    """
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def flatten(list_of_lists: list) -> list:
    """
    Flatten a list of lists.
    
    Taken from Alex Martelli at https://stackoverflow.com/a/952952.
    """
    return [item for sublist in list_of_lists for item in sublist]


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
