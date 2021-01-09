"""
A collection of utility functions to work with dictionaries.
"""
from copy import deepcopy
from typing import Union

def delete_field(dictionary: dict, field, inplace=True) -> Union[dict, None]:
    """
    Recursive delete `field` in `dictionary`.

    Dictionary is modified in palce if `inplace=True` (default)
    """

    # Safe copy
    if not inplace:
        dictionary = deepcopy(dictionary)

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

    #  Safe copy
    if not inplace:
        dictionary = deepcopy(dictionary)

    for k, v in list(dictionary.items()):
        if isinstance(v, dict):
            filter_fields(v, fields, inplace=True)
            continue

        if k not in fields:
            del dictionary[k]

    #  If not inplace, return
    if not inplace:
        return dictionary
