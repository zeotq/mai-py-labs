def number_length(n: int) -> int:
    if n == 0:
        return 1
    n = abs(n)
    len_n = 0
    while n != 0:
        len_n += 1
        n //= 10
    return len_n


def main():
    result = number_length(-12345)
    print(result)


if __name__ == "__main__":
    main()