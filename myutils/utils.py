"""
Collection of utilities I use often.

Some are just ways I like calling specific functions.
"""

import hashlib
import random
import re
from typing import Sequence

import numpy as np


def is_iterable(val):
    """
    Checks if `val` is iterable.


    This method calls `iter(val)`. If an exception is raised, it's not an iterable. 

    This is the 'correct' way, to account for the mess types are in Python.

    For details, see https://stackoverflow.com/a/1952655
    """
    try:
        iter(val)
    except TypeError:
        return False
    return True


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


def flatten(list_of_lists: list, exclude: Sequence = (str)) -> list:
    """
    Flatten a list of lists.

    This will also flatten items that are list like, such as strings.

    To exclude them, pass a list of types to `exclude`.

    By default, strings are excluded.

    Taken from Alex Martelli at https://stackoverflow.com/a/952952.
    """
    needs_flattening = lambda item: is_iterable(item) and not isinstance(item, exclude)

    while any(map(needs_flattening, list_of_lists)):
        list_of_lists = flatten_one_level(list_of_lists, exclude=exclude)

    return list_of_lists


def flatten_one_level(list_of_lists: list, exclude: Sequence = (str)) -> list:
    """
    Flatten a list of lists.

    Will only flatten a single level, so entries in output can also be lists.

    This will also flatten items that are list like, such as strings.

    To exclude them, pass a list of types to `exclude`.

    By default, strings are excluded.

    Taken from Alex Martelli at https://stackoverflow.com/a/952952.
    """
    #  Wrap non sequences in list, so we don't have problems later.
    need_wrap = lambda item: isinstance(item, exclude) or not is_iterable(item)
    list_of_lists = [[item] if need_wrap(item) else item for item in list_of_lists]
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


def pretty_round(x, precision=0):
    s = f"{x:.{precision}%}"

    if precision == 0 and s == "0%":
        return "<1%"

    if s == "0." + "0" * precision + "%":
        return "<0." + "0" * (precision - 1) + "1%"

    return s


def get_bytes_hash(bytes, hash_function=hashlib.md5, chunk_size=4096):
    """
    Return hash of byte stream.

    Adapted from quantumSoup at https://stackoverflow.com/a/3431838.
    """
    hash = hash_function()
    for chunk in iter(lambda: bytes.read(chunk_size), b""):
        hash.update(chunk)

    return hash


def get_file_hash(file_path, hash_function=hashlib.md5, chunk_size=4096):
    """
    Return hash of file contents.
    """
    with open(file_path, "rb") as f:
        return get_bytes_hash(f, hash_function=hash_function, chunk_size=chunk_size)

