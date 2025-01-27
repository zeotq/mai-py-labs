import re


class CyrillicError(Exception):
    ...


class CapitalError(Exception):
    ...


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


def name_validation(name: str):
    if not isinstance(name, str):
        raise TypeError
    if not re.fullmatch(r"[А-Яа-яЁё]+", name):
        raise CyrillicError
    if name and name != name.capitalize():
        raise CapitalError
    return name


def user_validation(*, last_name: str = None, first_name: str = None, username: str = None, **kwargs):
    if bool(kwargs):
        raise KeyError
    if not (isinstance(last_name, str) and isinstance(first_name, str) and isinstance(username, str)):
        raise 

    name_validation(last_name)
    name_validation(first_name)
    username_validation(username)

    return {"last_name": last_name, "first_name": first_name, "username": username}


from pytest import raises

def test_1():
    dict_1 = {'last_name': 'Иванов', 'first_name': 'Иван', 'username': 'ivanych45'}
    dict_2 = user_validation(last_name="Иванов", first_name="Иван", username="ivanych45")
    assert (dict_1.items() == dict_2.items())

def test_2():
    with raises(KeyError):
        print(user_validation(last_name="Иванов", 
                              first_name="Иван", 
                              username="ivanych45", 
                              password="123456"))


if __name__ == "__main__":
    test_1()
    test_2()