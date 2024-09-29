def nod_n(integers: list) -> int:
    """Поиск наибольшего общего делителя чисел из массива.

    Args:
        integers (list): целые числа.

    Returns:
        int: НОД.
    """

    temp = []
    while max(integers) != min(integers):
        integers.sort()
        min_element = integers[0]
        for i in integers:
            temp.append(i if i == min_element else i - min_element)
        integers = temp
        temp = []

    return integers[0]


def main():
    n = int(input())
    data = [int(input()) for i in range(n)]
    print(nod_n(data))


if __name__ == "__main__":
    main()
