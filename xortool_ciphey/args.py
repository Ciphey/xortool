

from xortool_ciphey.charset import get_charset


class ArgError(Exception):
    pass


def parse_char(ch):
    """
    'A' or '\x41' or '0x41' or '41'
    '\x00' or '0x00' or '00'
    """
    if ch is None:
        return None
    if len(ch) == 1:
        return ord(ch)
    if ch[0:2] in ("0x", "\\x"):
        ch = ch[2:]
    if not ch:
        raise ValueError("Empty char")
    if len(ch) > 2:
        raise ValueError("Char can be only a char letter or hex")
    return int(ch, 16)


def parse_int(i):
    if i is None:
        return None
    return int(i)


def parse_parameters(a):
    try:
        y = {
            "brute_chars": False,
            "brute_printable": True,
            "filename": "-",  # stdin by default
            "filter_output": False,
            "frequency_spread": 0,  # to be removed
            "input_is_hex": False,
            "known_key_length": None,
            "max_key_length": 65,
            "most_frequent_char": " ",
            "text_charset": get_charset("*"),
            "known_plain": False,
        }
        print(y)
        return y
    except ValueError as err:
        raise ArgError(str(err))
