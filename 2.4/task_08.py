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
    max_name = 0
    max_dS = 0

    for i in range(n):
        name = input()
        integer = digitsSum(int(input()))
        max_name, max_dS = ((name, integer) 
                            if (integer >= max_dS) 
                            else (max_name, max_dS))
    print(max_name)


if __name__ == "__main__":
    main()
