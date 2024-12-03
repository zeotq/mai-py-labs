def fibonacci(n):
    if n < 1:
        raise ValueError
    n += 2
    n_1 = 0
    n_2 = 1
    for i in range(2, n):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2


"""def fibonacci(n):
    n_1, n_2 = 1, 1
    for i in range(n):
        yield n_1
        n_1, n_2 = n_2, n_1 + n_2"""


def main():
    print(*fibonacci(5))
    print(*fibonacci(10), sep=', ')


if __name__ == "__main__":
    main()