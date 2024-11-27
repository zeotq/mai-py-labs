def split_numbers(numstring: str) -> tuple:
    return tuple(map(int, numstring.split()))


def main():
    result = split_numbers("1 2 3 4 5")
    print(result)


if __name__ == "__main__":
    main()