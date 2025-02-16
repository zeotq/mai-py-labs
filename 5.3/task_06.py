from math import sqrt


class NoSolutionsError(Exception):
    ...


class InfiniteSolutionsError(Exception):
    ...


def find_roots(a, b, c) -> tuple:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise TypeError

    if a == 0:
        if b == 0:
            if c == 0:
                raise InfiniteSolutionsError("Уравнение имеет бесконечно много решений.")
            else:
                raise NoSolutionsError("Уравнение не имеет решений.")
        else:
            return (-c / b, -c / b)

    d = b ** 2 - 4 * a * c

    if d < 0:
        raise NoSolutionsError

    sqrt_d = sqrt(d)
    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)

    return tuple(sorted([root1, root2]))


def test_1():
    from pytest import raises
    with raises(NoSolutionsError) as exc_info:
        find_roots(0, 0, 1)
    
def test_2():
    find_roots(1, 2, 1) == (-1.0, -1.0)
