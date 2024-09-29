def main():
    """Поисковая система на минималках
    """

    n = int(input())
    pages = [input() for _ in range(n)]
    request = input()
    pages = list(filter(lambda a: request.lower() in a.lower(), pages))
    print(*pages, sep="\n")


if __name__ == "__main__":
    main()
