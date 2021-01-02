"""
This library works with pandas and numpy. 

The packages often produce types such as int64 that do not have a serialization
method when calling `json.dumps`.

This package is just so we can convert objects to JSON safely. 

I read about this serialization feature in 
https://ellisvalentiner.com/post/serializing-numpyfloat32-json/.

Most of the code was take from there. 

Credit goes to Ellis Michael Valentiner, the author of that post.
"""


import json
import numpy as np
from functools import singledispatch


@singledispatch
def to_serializable(val):
    """Used by default."""
    return str(val)


@to_serializable.register(np.int64)
def ts_int64(val):
    """Used if *val* is an instance of numpy.int64."""
    return np.int(val)


def to_json(dictionary, indent=4):
    return json.dumps(dictionary, indent=indent, default=to_serializable, sort_keys=True,)

