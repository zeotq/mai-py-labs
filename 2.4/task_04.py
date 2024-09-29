def digitsSum(n: int, s: int = 10) -> int:
    """Находит сумму цифр числа по остаткам
    от деления числа n системы счисления s.

    Args:
        n (int): Некоторое число в системе счисления s.
        s (int): Система счисления. Defaults to 10.

    Returns:
        int: Сумма цифр числа.
    """

    dS = 0
    while n != 0:
        dS += n % s
        n //= s
    return dS


def main():
    n = int(input())
    print(sum([digitsSum(int(input())) for i in range(n)]))


if __name__ == "__main__":
    main()
