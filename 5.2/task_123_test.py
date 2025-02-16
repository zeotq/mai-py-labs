from point import *

# Task 1
def test_new_init():
    first_point = PatchedPoint((2, -7))
    second_point = PatchedPoint(7, 9)
    assert first_point.length(second_point) == 16.76
    assert second_point.length(first_point) == 16.76

# Task 2
def test_str_repr_1():
    point = PatchedPoint()
    assert point.__str__() == '(0, 0)'
    point.move(2, -3)
    assert repr(point) == 'PatchedPoint(2, -3)'

def test_str_repr_2():
    first_point = PatchedPoint((2, -7))
    second_point = PatchedPoint(7, 9)
    assert list(map(str, (first_point, second_point))) == ['(2, -7)', '(7, 9)']
    assert list(map(repr, (first_point, second_point))) == ['PatchedPoint(2, -7)', 'PatchedPoint(7, 9)']

# Task 3
def test_add_1():
    point = PatchedPoint()
    assert point.__str__() == '(0, 0)'
    new_point = point + (2, -3)
    assert (point.__str__(), new_point.__str__(), point is new_point) == ("(0, 0)", "(2, -3)", False)

def test_iadd_1():
    first_point = second_point = PatchedPoint((2, -7))
    first_point += (7, 3)
    assert (first_point.__str__(), second_point.__str__(), first_point is second_point) == ("(9, -4)", "(9, -4)", True)
