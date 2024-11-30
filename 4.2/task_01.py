def make_list(lenght: int, value: any = 0) -> list:
    return lenght * [value]


def main():
    result = make_list(3)
    print(result)


if __name__ == "__main__":
    main()