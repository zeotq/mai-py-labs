from math import sqrt


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, x: int | None = 0, y: int | None = 0) -> None:
        self.x += x
        self.y += y

    def length(self, second_point) -> float:
        return round(sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2), 2)
    

class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], (tuple, list)):
            super().__init__(*args[0])
        elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            super().__init__(args[0], args[1])
        else:
            super().__init__(0, 0)

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'
    
    def __add__(self, delta: tuple):
        return PatchedPoint(self.x + delta[0], self.y + delta[1])
    
    def __radd__(self, delta: tuple):
        return PatchedPoint(self.x + delta[0], self.y + delta[1])
    
    def __iadd__(self, delta: tuple):
        self.x += delta[0]
        self.y += delta[1]
        return self


def main():
    pass

if __name__ == "__main__":
    main()