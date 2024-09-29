def firTable(rang: int = 1) -> list:
    """Создание новогодней математической ёлки.

    Args:
        rang (int, optional): Последнее число ёлки. Defaults to 1.

    Returns:
        list: Матрица ёлка.
    """

    table = []
    n, k = 1, 1
    while n <= rang:
        table.append(list(range(n, (n + k if n + k <= rang else rang + 1))))
        n += k
        k += 1
    return table


def main():
    n = int(input())
    for i in firTable(n):
        print(*i)


if __name__ == "__main__":
    main()
