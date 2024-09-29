def multiplayTable(rang_x: int = 1, rang_y: int = 1) -> list:
    """Создание двумерного массива таблицы умножения.

    Args:
        rang_x (int, optional): Длина таблицы. Defaults to 1.
        rang_y (int, optional): Высота таблицы. Defaults to 1.

    Returns:
        list: Матрица таблица.
    """

    table = rang_y * [rang_x * [0]]
    table[0] = list(range(1, rang_x + 1))
    for i in range(1, rang_y):
        table[i] = list(range(i + 1, (i + 1) * rang_x + 1, i + 1))
    return table


def main():
    n = int(input())
    data = multiplayTable(n, n)
    for i in data:
        print(*i)  


if __name__ == "__main__":
    main()
