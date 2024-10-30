def stringsCrossing(a: str = '', b: str = '') -> str:
    set_1 = set(a)
    set_2 = set(b)
    set_1 = set_1.intersection(set_2)
    return ''.join(reversed(list(set_1)))


def main():
    string_1, string_2 = input(), input()
    print(stringsCrossing(string_1, string_2))


if __name__ == "__main__":
    main()
