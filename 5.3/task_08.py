import re


class BadCharacterError(Exception):
    ...


class StartsWithDigitError(Exception):
    ...


def username_validation(name: str):
    if not isinstance(name, str):
        raise TypeError
    if not re.fullmatch(r"[A-Za-z0-9_]+", name):
        raise BadCharacterError
    if re.match(r"^[0-9]", name):
        raise StartsWithDigitError
    return name


from pytest import raises

def test_1():
    with raises(BadCharacterError):
            print(username_validation("user₄5"))

def test_2():
    with raises(StartsWithDigitError):
        print(username_validation("45_user"))
