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
    fir = firTable(n)
    max_lenth = sum([len(str(i)) for i in fir[-1]]) + len(fir[-1]) - 1
    out_line = ''
    for line in fir:
        line = list(map(str, line))
        lenth = sum([len(i) for i in line]) + len(line) - 1
        out_line += (f"{' ' * ((max_lenth - lenth) // 2)}" +
                     f"{' '.join(line)}" + 
                     f"{' ' * (round((max_lenth - lenth) / 2))}\n")
    print(out_line)


if __name__ == "__main__":
    main()
