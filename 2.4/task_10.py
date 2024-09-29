def orangeSlices(n: int, m: int = 3) -> list:
    """ Матрица все возможных вариантов разложения числа n на m слагаемых

    Args:
        n (int): Некоторое число
        m (int, optional): Количество слагаемых. Defaults to 3.

    Returns:
        list: матрица n x m
    """

    if n < m:
        return None

    data = []
    components = [i + 1 for i in range(0, n - m + 1)]

    def orangeCut(cur: list, alph: list, nl: int, ml: int) -> None:
        temp = []
        if sum(cur) > nl or len(cur) > ml:
            return None
        
        elif sum(cur) == n and len(cur) == ml:
            data.append(cur)

        for i in alph:
            next = orangeCut(cur + [i], alph, nl, ml)
            if next:
                temp.append(next)

        return temp

    for i in components:
        orangeCut(cur=[i], alph=components, nl=n, ml=m)

    return data
    

def main():
    n = int(input())
    print("А Б В")
    for i in orangeSlices(n):
        print(*i)


if __name__ == "__main__":
    main()
