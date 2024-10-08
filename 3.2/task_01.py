def uniSymbols(n: str) -> str:
    n = set(list(n))
    return n


def main():
    string = input()
    print(*list(uniSymbols(string)), sep='')


if __name__ == "__main__":
    main()
