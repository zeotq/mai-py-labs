def gcd(*args) -> int:
    """Поиск наибольшего общего делителя чисел из массива.

    Args:
        integers (list): целые числа.

    Returns:
        int: НОД.
    """
    integers = list(args)
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
    result = gcd(3)
    print(result)
    result = gcd(36, 48, 156, 100500)
    print(result)


if __name__ == "__main__":
    main()