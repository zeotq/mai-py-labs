def gcd(x: int, y: int) -> int:
    """Поиск наибольшего общего делителя"""

    while x != y:
        x, y = min(x, y), max(x, y)
        x, y = y - x, x
    return x


def main():
    result = gcd(12, 45)
    print(result)


if __name__ == "__main__":
    main()