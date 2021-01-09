"""
Collection of utilities I use often.

Some are just ways I like calling specific functions.
"""

import copy
import random
import re
from typing import Union

import numpy as np


def chunks(lst: list, n: int) -> list:
    """
    Splits lst into n chunks.
    
    Taken from Jason Mitchell at https://stackoverflow.com/a/29679492.
    """
    return [list(x) for x in np.array_split(lst, n)]


def scramble(lst: list) -> list:
    """
    Scrambles a list.

    Taken from koffein at https://stackoverflow.com/a/19836008.
    """
    return sorted(lst, key=lambda _: random.random())


def chunks_n(lst: list, n: int) -> list:
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


def delete_field(dictionary: dict, field, inplace=True) -> Union[dict, None]:
    """
    Recursive delete `field` in `dictionary`.

    Dictionary is modified in palce if `inplace=True` (default)
    """

    # Safe copy
    if not inplace:
        dictionary = copy.deepcopy(dictionary)

    for k, v in list(dictionary.items()):
        if k == field:
            del dictionary[k]

        if isinstance(v, dict):
            delete_field(v, field, inplace=True)

    # If not inplace, return
    if not inplace:
        return dictionary


def filter_fields(dictionary: dict, fields: list, inplace=True) -> Union[dict, None]:
    """
    Deletes from `dictionary` all fields not in `fields`

    Dictionary is modified in palce if `inplace=True` (default)
    """

    # Safe copy
    if not inplace:
        dictionary = copy.deepcopy(dictionary)

    for k, v in list(dictionary.items()):
        if k not in fields:
            del dictionary[k]

        if isinstance(v, dict):
            filter_fields(v, fields, inplace=True)

    # If not inplace, return
    if not inplace:
        return dictionary

