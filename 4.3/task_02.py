def recursive_digit_sum(n: int, sum: int = 0) -> int:
    if n == 0:
        return sum
    return recursive_digit_sum(n // 10, sum + n % 10)


def main():
    result = recursive_digit_sum(123)
    print(result)
    result = recursive_digit_sum(7321346)
    print(result)


if __name__ == "__main__":
    main()