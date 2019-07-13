import codecs
from pathlib import Path


def rot13(in_str: str):
    return codecs.encode(in_str, 'rot13')


def tor31(in_str: str):
    return codecs.decode(in_str, 'rot13')


def abbreviate(in_str: str, length=30):
    return f"{in_str[:length]} ..." if len(in_str) > length else in_str


def truncate(directory, with_parent=True):
    p = Path(directory)
    if with_parent:
        return f"../{p.parent.name}/{p.name}"
    else:
        return p.name


def str_to_bool(bool_str):
    if type(bool_str) is bool:
        return bool_str
    return bool_str.lower() in ("yes", "true", "t", "1")
