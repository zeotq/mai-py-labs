def deEven(n: int) -> int:
    """Составление нового числа на основе входящего без
    чётных цифр.

    Args:
        n (int): некоторое число

    Returns:
        int: исходное число без четных цифр
    """

    output = 0
    digit_counter = 1

    while n != 0:
        temp = n % 10
        if temp % 2 != 0:
            output += digit_counter * temp
            digit_counter *= 10
        n //= 10

    return output


def main():
    print(deEven(int(input())))


if __name__ == "__main__":
    main()