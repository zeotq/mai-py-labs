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
    width = int(input())
    data = multiplayTable(n, n)
    len_data = len(data)
    out_line = ''

    for i in range(len_data):
        line = data[i]
        len_line = len(line)
        for j in range(len_line):
            len_symb = len(str(line[j]))
            out_line += (f"{' ' * ((width - len_symb) // 2)}" +
                         f"{line[j]}" + 
                         f"{' ' * (round((width - len_symb) / 2))}")
            if j + 1 < len_line:
                out_line += "|"
        if i + 1 < len_data:
            out_line += f"\n{((width + 1) * len_line - 1) * '-'}\n"
    print(out_line)


if __name__ == "__main__":
    main()
