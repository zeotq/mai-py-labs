def nok(x: int, y: int) -> int:
    """Поиск наименьшего общего кратного"""

    for i in range(min(x, y), x * y + 1):
        if i % x + i % y == 0: 
            return i


print(nok(int(input()), int(input())))
