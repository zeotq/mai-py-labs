ACCURACY = 2


def round_answer(func, round_value: int | None = ACCURACY):
    def new_func(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if isinstance(result, tuple):
            return tuple(round(val, round_value) for val in result)
        elif isinstance(result, (float, int)):
            return round(result, round_value)
        elif isinstance(result, Point):
            result.x = round(result.x, round_value)
            result.y = round(result.y, round_value)
        return result  
    return new_func


class Point:
    def __init__(self, x: int | float, y: int | float):
        self.x = round(x, ACCURACY)
        self.y = round(y, ACCURACY)

    def __add__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return Point(self.x + other[0], self.y + other[1])
        raise ValueError

    def __iadd__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            self.x = round(self.x + other[0], ACCURACY)
            self.y = round(self.y + other[1], ACCURACY)
            return self
        raise ValueError
    
    def scale_from_other_point(self, other, factor: int | float):
        if isinstance(other, Point):
            dx = round(self.x - other.x, ACCURACY)
            dy = round(self.y - other.y, ACCURACY)
            self.x = round(self.x + dx * (factor - 1), ACCURACY)
            self.y = round(self.y + dy * (factor - 1), ACCURACY)
            return
        raise ValueError
    
    def rotate_around_other_point(self, other):
        if isinstance(other, Point):
            dx = round(self.y - other.y, ACCURACY)
            dy = round(other.x - self.x, ACCURACY)
            self.x = round(other.x + dx, ACCURACY)
            self.y = round(other.y + dy, ACCURACY)
            return
        raise ValueError

    def __str__(self):
        return f'<{self.x} {self.y}>'


class Rectangle:
    def __init__(self, point_1: tuple, point_2: tuple):
        self.A = Point(min(point_1[0], point_2[0]), max(point_1[1], point_2[1]))
        self.B = Point(max(point_1[0], point_2[0]), min(point_1[1], point_2[1]))

    @round_answer
    def area(self) -> float:
        return abs((self.A.x - self.B.x) * (self.A.y - self.B.y))
    
    @round_answer
    def perimeter(self) -> float:
        return 2 * (abs(self.A.x - self.B.x) + abs(self.A.y - self.B.y))
    
    @round_answer
    def get_pos(self) -> tuple:
        return (self.A.x, self.A.y)

    @round_answer
    def get_size(self) -> tuple:
        return (self.B.x - self.A.x), (self.A.y - self.B.y)

    def move(self, dx, dy) -> None:
        self.A += (dx, dy)
        self.B += (dx, dy)

    def resize(self, width, height) -> None:
        self.B.x = round(self.A.x + width, ACCURACY)
        self.B.y = round(self.A.y - height, ACCURACY)

    @round_answer
    def get_center(self) -> tuple:
        return (
            round((self.A.x + self.B.x) / 2, ACCURACY),
            round((self.A.y + self.B.y) / 2, ACCURACY)
        )

    def turn(self) -> None:
        center = Point(*self.get_center())
        self.A.rotate_around_other_point(center)
        self.B.rotate_around_other_point(center)
        self.A.x, self.B.x = self.B.x, self.A.x
        
    def scale(self, factor: int | float | None = 1) -> None:
        center = Point(*self.get_center())
        self.A.scale_from_other_point(center, factor)
        self.B.scale_from_other_point(center, factor)
