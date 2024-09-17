def nod(x: int, y: int) -> int:
    """Поиск наибольшего общего делителя"""

    while x != y:
        x, y = min(x, y), max(x, y)
        x, y = y - x, x
    return x


print(nod(int(input()), int(input())))
