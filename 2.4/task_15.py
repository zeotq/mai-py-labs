def digitRectangleSnakeFlip(x: int = 1, y: int = 1) -> list:
    """Числовой прямоугольник змейка.
           
    Args:
        x (int, optional): Количество строк. Defaults to 1.
        y (int, optional): Количество столбцов. Defaults to 1.

    Returns:
        list: Прямоугольная числовая матрица вида:
         1  6  7 12
         2  5  8 11
         3  4  9 10
    """

    out = [[i + (j - 1) * x if j % 2 == 1 else j * x - i + 1
            for j in range(1, y + 1)] for i in range(1, x + 1)]
    
    return out


def main():
    n_1, n_2 = int(input()), int(input())
    rec = digitRectangleSnakeFlip(x=n_1, y=n_2)
    space = max([len(str(max(i))) if i else 0 for i in rec])

    for i in rec:
        for j in i:
            print(f'{" " * (space - len(str(j)))}{j}', end=" ")
        print("", end="\n")


if __name__ == "__main__":
    main()
