numbers = list()


def add_number(num):
    numbers.append(num)


def get_prod():
    result = 1
    s = " * ".join(map(str, numbers))
    for i in numbers:
        result *= i
    s += f' = {result}'
    return s


def main():
    add_number(7)
    add_number(2)
    print(get_prod())
    add_number(5)
    print(get_prod())


if __name__ == "__main__":
    main()