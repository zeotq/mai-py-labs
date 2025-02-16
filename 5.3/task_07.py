import re


class CyrillicError(Exception):
    ...


class CapitalError(Exception):
    ...


def name_validation(name: str):
    if not isinstance(name, str):
        raise TypeError
    if not re.fullmatch(r"[А-Яа-яЁё]+", name):
        raise CyrillicError
    if name and name != name.capitalize():
        raise CapitalError
    return name


from pytest import raises

def test_1():
    with raises(CyrillicError):
        print(name_validation("user"))

def test_2():
    with raises(CapitalError):
        print(name_validation("иванов"))
