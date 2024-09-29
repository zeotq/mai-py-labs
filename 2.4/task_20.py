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
    max_sum = 0
    max_system = 0
    for i in range(2, 11):
        new_sum = digitsSum(n, i)
        if new_sum > max_sum:
            max_sum = new_sum
            max_system = i
    print(max_system)


if __name__ == "__main__":
    main()
