def digitsMax(n: int) -> int:
    """Находит максимальную цифру числа.

    Args:
        n (int): Некоторое число.

    Returns:
        int: Максимальная цифра.
    """

    dM = 0
    while n != 0:
        dM = max(dM, n % 10)
        n //= 10
    return dM


def main():
    n = int(input())
    sum_dM = 0

    for i in range(n):
        sum_dM = sum_dM * 10 + digitsMax(int(input()))
        
    print(sum_dM)


if __name__ == "__main__":
    main()
