# Pytest

from rectangle_pwh import Rectangle as Rectangle


# task 5
def test_rectangle_perimeter():
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    assert rect.perimeter() == 23.52

def test_rectangle_area():
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    assert rect.area() == 32.14

# task 6
def test_rectangle_initialization():
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    assert rect.get_pos() == (3.2, 3.14), "Initial position is incorrect"
    assert rect.get_size() == (4.32, 7.44), "Initial size is incorrect"

def test_rectangle_resize():
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    assert rect.get_pos() == (3.2, 3.14), "Position is incorrect"
    assert rect.get_size() == (4.32, 7.44), "Size is incorrect"
    rect.resize(23.5, 11.3)
    assert rect.get_pos() == (3.2, 3.14), "Position after resize is incorrect"
    assert rect.get_size() == (23.5, 11.3), "Size after resize is incorrect"

def test_rectangle_move():
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    assert rect.get_pos() == (3.2, 3.14), "Position is incorrect"
    assert rect.get_size() == (4.32, 7.44), "Size is incorrect"
    rect.move(1.32, -5)
    assert rect.get_pos() == (4.52, -1.86), "Position after move is incorrect"
    assert rect.get_size() == (4.32, 7.44), "Size after move is incorrect"

# task 7
def test_rectangle_turn():
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    assert rect.get_pos() == (-3.14, 2.71), "Position is incorrect"
    assert rect.get_size() == (6.28, 5.42), "Size is incorrect"
    rect.turn()
    assert rect.get_pos() == (-2.71, 3.14), "Position after turn is incorrect"
    assert rect.get_size() == (5.42, 6.28), "Size after turn is incorrect"

def test_rectangle_turn_negative_1():
    rect = Rectangle((-5, -1), (-1, -5))
    rect.turn()
    assert rect.get_pos() == (-5, -1), "Position after turn is incorrect"
    assert rect.get_size() == (4, 4), "Size after turn is incorrect"

def test_rectangle_turn_negative_2():
    rect = Rectangle((0, 0), (-2, -10))
    rect.turn()
    assert rect.get_pos() == (-6, -4), "Position after turn is incorrect"
    assert rect.get_size() == (10, 2), "Size after turn is incorrect"


def test_rectangle_scale():
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    rect.scale(2.0)
    assert rect.get_pos() == (-6.28, 5.42), "Position after scale is incorrect"
    assert rect.get_size() == (12.56, 10.84), "Size after scale is incorrect"

def test_rectangle_scale_in_neg_zone():
    rect = Rectangle((-6, -4), (-4, -6))
    rect.scale(2.0)
    assert rect.get_pos() == (-7, -3), "Position after scale is incorrect"
    assert rect.get_size() == (4, 4), "Size after scale is incorrect"

def test_rectangle_negative_scale():
    rect = Rectangle((2, 10), (10, 2))
    rect.scale(0.5)
    assert rect.get_pos() == (4, 8), "Position after scale is incorrect"
    assert rect.get_size() == (4, 4), "Size after scale is incorrect"
