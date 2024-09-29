def digitRectangleSnake(x: int = 1, y: int = 1) -> list:
    """Числовой прямоугольник змейка.
           
    Args:
        x (int, optional): Количество строк. Defaults to 1.
        y (int, optional): Количество столбцов. Defaults to 1.

    Returns:
        list: Прямоугольная числовая матрица вида:
         1  2  3  4
         8  7  6  5
         9 10 11 12
    """

    return [
        [j for j in range((y * (i - 1) + 1) if i % 2 == 1 else (y * i),
                          (y * (i - 1)) if i % 2 == 0 else (y * i + 1),
                          (-1) ** (i + 1))] for i in range(1, x + 1)
                          ]


def main():
    n_1, n_2 = int(input()), int(input())
    rec = digitRectangleSnake(x=n_1, y=n_2)
    space = max([len(str(max(i))) if i else 0 for i in rec])

    for i in rec:
        for j in i:
            print(f'{" " * (space - len(str(j)))}{j}', end=" ")
        print("", end="\n")


if __name__ == "__main__":
    main()
