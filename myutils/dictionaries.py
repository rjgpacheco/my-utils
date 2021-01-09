"""
A collection of utility functions to work with dictionaries.
"""
from copy import deepcopy
from typing import Union
from typing import Sequence


def delete_field(dictionary: dict, field, inplace=True) -> Union[dict, None]:
    """
    Recursive delete `field` in `dictionary`.

    Dictionary is modified in palce if `inplace=True` (default)
    """

    #  Safe copy
    if not inplace:
        dictionary = deepcopy(dictionary)

    for k, v in list(dictionary.items()):
        if k == field:
            del dictionary[k]

        if isinstance(v, dict):
            delete_field(v, field, inplace=True)

    #  If not inplace, return
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


def check_dict_has_kv(dictionary: dict, key, value) -> bool:
    """
    Check if `dictionary` has entry `key` with value `value`.
    """
    if key in list(dictionary.keys()) and dictionary[key] == value:
        return True
    return False


def check_dict_kv_in_list(dictionary: dict, key, values: Sequence) -> bool:
    """
    Check if `dictionary` has entry `key` with value in `values`.
    """
    if key in list(dictionary.keys()) and dictionary[key] in values:
        return True
    return False


def merge_dicts_kv(dictionaries: Sequence[dict]) -> dict:
    """
    Merges a list of dictionaries to a single dictionary. 

    For keys shared between dictionaries, their values will be concatenated.

    All values in output dictionary are lists.
    """
    dictionary = {}
    for i, subdict in enumerate(dictionaries):
        if not isinstance(subdict, dict):
            raise ValueError(f"dictionaries[{i}] is of type '{type(subdict)}'")

        for k, v in subdict.items():
            if isinstance(v, dict):
                raise ValueError("Supplied dictionaries must not have dictionaries as values.")

            if k not in dictionary.keys():
                dictionary[k] = []

            dictionary.get(k, []).append(v)
    return dictionary


def delete_subdicts(dictionary: dict, dicts: Sequence[dict], inplace=True) -> Union[dict, None]:
    """
    Deletes sub dictionaires present as values in `dictionary`, if they match a dict in dicts
    """
    #  Safe copy
    if not inplace:
        dictionary = deepcopy(dictionary)

    #  Merge all dicts as k -> Sequence(keys) so we don't need to iterate over all of them
    to_exclude = merge_dicts_kv(dicts)
    for k, v in list(dictionary.items()):
        if not isinstance(v, dict):
            continue

        for badkey, badvalues in to_exclude.items():
            if badkey in list(v.keys()) and v[badkey] in badvalues:
                del dictionary[k]

    #  If not inplace, return
    if not inplace:
        return dictionary

