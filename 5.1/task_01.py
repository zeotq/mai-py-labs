class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    point = Point(2, -7)
    print(point.x, point.y)


if __name__ == "__main__":
    main()
