def make_matrix(size: tuple | int, value: any = 0) -> list:
    if isinstance(size, int):
        x, y = size, size
    elif isinstance(size, tuple):
        x, y = size[0], size[1]
    else:
        raise ValueError("Unsupporter size")
    return [list(x * [value]) for _ in range(y)]


def main():
    result = make_matrix(3)
    print(result)
    result = make_matrix((4, 2), 1)
    print(result)


if __name__ == "__main__":
    main()