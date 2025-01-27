import re
from hashlib import sha256


class MinLengthError(Exception):
    ...


class PossibleCharError(Exception):
    ...


class NeedCharError(Exception):
    ...


def password_validation(password: str, *, 
                        min_length: int = 8, 
                        possible_chars: str = None,
                        at_least_one=lambda s: s.isdigit()):
    
    if not isinstance(password, str):
        raise TypeError
    
    if possible_chars is None:
        poss_ch = re.compile(r"^[A-Za-z0-9]+$")
    else:
        poss_ch = re.compile(f"^[{re.escape(possible_chars)}]+$")
    
    if len(password) < min_length:
        raise MinLengthError
    
    if not re.fullmatch(poss_ch, password):
        raise PossibleCharError

    if not any(map(at_least_one, password)):
        raise NeedCharError
    
    return sha256(password.encode()).hexdigest()


if __name__ == "__main__":
    pass


import pytest

def test_1():
    assert (password_validation("Hello12345") == "67698a29126e52a6921ca061082783ede0e9085c45163c3658a2b0a82c8f95a1")

def test_2():
    with pytest.raises(PossibleCharError):
        print(password_validation("uNriuNrie_777",
        min_length=6,
        at_least_one=lambda char: char in "!@#$%^&*()_"
    ))
        
def test_3():
    with pytest.raises(NeedCharError):
        password_validation("a_+", min_length=0, possible_chars="+a_")


def test_4():
    with pytest.raises(NeedCharError):
        password_validation("A", min_length=0)

def test_5():
    with pytest.raises(MinLengthError):
        password_validation("A", min_length=8)

def test_6():
    with pytest.raises(NeedCharError):
        password_validation("A", min_length=0)