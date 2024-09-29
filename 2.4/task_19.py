def digitRectangleInner(x: int = 1, y: int = 1) -> list:
    """Числовой прямоугольник.
           
    Args:
        x (int, optional): Количество строк. Defaults to 1.
        y (int, optional): Количество столбцов. Defaults to 1.

    Returns:
        list: Прямоугольная числовая матрица вида:
            1 1 1 1 1
            1 2 2 2 1
            1 2 3 2 1
            1 2 2 2 1
            1 1 1 1 1
    """

    out = [[min(min(x - i + 1, i), min(y - j + 1, j)) 
            for j in range(1, y + 1)] for i in range(1, x + 1)]
    
    return out


def main():
    n_1 = int(input())
    n_2 = int(input())
    rec = digitRectangleInner(x=n_1, y=n_2)
    space = max([len(str(max(i))) if i else 0 for i in rec])

    for i in rec:
        for j in i:
            print(f'{" " * (space - len(str(j)))}{j}', end=" ")
        print("", end="\n")


if __name__ == "__main__":
    main()
