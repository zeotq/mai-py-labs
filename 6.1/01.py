import pytest

from math import log, pow, sin, cos, pi, e


def expression(n: float | int) -> float:
    return log(pow(n, 3 / 16), 32) + pow(n, cos((pi * n) / (2 * e))) - pow(sin(n / pi), 2)


if __name__ == "__main__":
    print(expression(float(input())))


def test_1():
    assert expression(2.71) == 0.4818035253577275

def test_2():
    assert expression(12.345) == 4.880549344757598