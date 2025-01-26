import pandas as pd
import numpy as np


def values(func, start, end, step) -> pd.Series:
    """строит Series значений функции в точках диапазона и принимающую:
    функцию одной переменной

    Args:
        start (int): начало диапазона
        end (int): конец диапазона
        step (int): шаг вычисления
    """
    iterable_val = np.arange(start, end + step, step)
    return pd.Series(data=[func(i) for i in iterable_val], index=iterable_val)


def min_extremum(data: pd.Series):
    """Возвращает точку, в которой был достигнут минимум на диапазоне
    """
    return data.idxmin(axis='index')


def max_extremum(data: pd.Series):
    """Возвращает точку, в который был достигнут максимум на диапазоне
    """
    return data.idxmax(axis='index')


def test_1():
    from pytest import approx
    data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)

    data_dict = {
        -1.5: 0.25, -1.4: 0.16, -1.3: 0.09, -1.2: 0.04, -1.1: 0.01, -1.0: 0.00,
        -0.9: 0.01, -0.8: 0.04, -0.7: 0.09, -0.6: 0.16, -0.5: 0.25, -0.4: 0.36,
        -0.3: 0.49, -0.2: 0.64, -0.1: 0.81, 1.332268e-15: 1.00, 0.1: 1.21,
        0.2: 1.44, 0.3: 1.69, 0.4: 1.96, 0.5: 2.25, 0.6: 2.56, 0.7: 2.89,
        0.8: 3.24, 0.9: 3.61, 1.0: 4.00, 1.1: 4.41, 1.2: 4.84, 1.3: 5.29,
        1.4: 5.76, 1.5: 6.25, 1.6: 6.76, 1.7: 7.29
    }
    test_data = pd.Series(data_dict)

    assert np.isclose(data, test_data).all()
    assert min_extremum(data) == approx(-0.9999999999999996)
    assert max_extremum(data) == approx(1.7000000000000028)


if __name__ == "__main__":
    test_1()