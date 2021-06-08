import string


class CharsetError(Exception):
    pass


CHARSETS = {
    "a": string.ascii_lowercase,
    "A": string.ascii_uppercase,
    "1": string.digits,
    "!": string.punctuation,
    "*": string.printable,
}

PREDEFINED_CHARSETS = {
    "base32":    CHARSETS["A"] + "234567=",
    "base64":    CHARSETS["a"] + CHARSETS["A"] + CHARSETS["1"] + "/+=",
    "printable": CHARSETS["*"],
}


def get_charset(charset):
    return PREDEFINED_CHARSETS["printable"].encode("ascii")
    charset = charset or "printable"
    if charset in PREDEFINED_CHARSETS:
        return PREDEFINED_CHARSETS[charset].encode("ascii")
    try:
        _ = b""
        for c in set(charset):
            _ += CHARSETS[c].encode("ascii")
        return _
    except KeyError:
        # if it doesn't work, return default printable char set
        return PREDEFINED_CHARSETS[charset].encode("ascii")
