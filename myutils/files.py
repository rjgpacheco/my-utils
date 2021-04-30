from pathlib import Path


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
