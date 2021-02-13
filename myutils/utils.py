"""
Collection of utilities I use often.

Some are just ways I like calling specific functions.
"""

import hashlib
import os


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


def cls():
    """
    Clear terminal.
    
    Taken from popcnt at https://stackoverflow.com/a/684344.
    """
    os.system("cls" if os.name == "nt" else "clear")

