from math import sqrt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x: int | None = 0, y: int | None = 0) -> None:
        self.x += x
        self.y += y

    def length(self, second_point) -> float:
        return round(sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2), 2)


def main():
    first_point = Point(2, -7)
    second_point = Point(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))

    point = Point(3, 5)
    print(point.x, point.y)
    point.move(2, -3)
    print(point.x, point.y)


if __name__ == "__main__":
    main()
