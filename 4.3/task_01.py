def recursive_sum(*args):
    if not args:
        return 0
    return args[-1] + recursive_sum(*args[:-1])


def main():
    print(recursive_sum(1, 2, 3))
    print(recursive_sum(7, 1, 3, 2, 10))


if __name__ == "__main__":
    main()