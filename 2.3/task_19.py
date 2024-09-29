def question(number: int) -> int:
    """Получаем ответ от проверяющей системы.
    
    Args:
        number (int): Число на вход.
    
    Returns:
        status (int):
        keys:
            1 - больше
            -1 - меньше
            0 - неопределено
    """

    print(number)
    decoder = {"Больше": 1, "Меньше": -1, "Угадал!": 0}
    return decoder[f"{input()}"]


def binFinder(border_a: int, border_b: int):
    """Находит заданное число при помощи бинарного поиска.
    
    Args:
        border_a (int): Граница 1 диапозона поиска.
        border_b (int): Граница 2 диапозона поиска.

    Returns:
        any: Рекурсивный вызов или искомое число.
    """

    n = (border_a + border_b + 1) // 2
    status = question(n)

    if status == 1:
        return binFinder(n, max(border_a, border_b))
    elif status == -1:
        return binFinder(min(border_a, border_b), n)
    else:
        return n


def main():
    print(binFinder(0, 1000))


if __name__ == "__main__":
    main()