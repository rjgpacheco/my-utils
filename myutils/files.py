import re
import string
from pathlib import Path

from .strings import clip


VALID_WINDOWS_FILENAME_CHARS = frozenset([*"-_.() ", *string.ascii_letters, *string.digits])
WINDOWS_ILLEGAL_CHARACTERS = ["\\", "/", ":", "*", "?", "<", ">", "|"]
WINDOWS_MAX_FILE_LENGTH = 255


def rename(path: Path, name):
    """
    Replaces the name path with name in the same folders.

    Will also replace extension.
    """
    path.rename(Path(path.parent, name))


def reparent(path: Path, parent):
    """
    Replaces path parent, keeping name
    """
    return Path(parent, path.name)


def sanitize_name(filename: str, illegal_chars=WINDOWS_ILLEGAL_CHARACTERS) -> str:
    filename = filename.replace('"', "'")
    filename = re.sub("\s", " ", filename)
    filename = "".join([c if c not in illegal_chars else " " for c in filename])
    filename = re.sub("\s+", " ", filename)
    return filename


def clip_path(path: Path, max_length=WINDOWS_MAX_FILE_LENGTH) -> str:
    path = Path(path)

    if len(str(path)) <= max_length:
        return path

    return path.with_stem(clip(path.stem, max_length - len(str(path.with_stem("")))))
