def main():
    """Удаляем комментарии из кода.
    """

    symbols = ''
    while (word := input()) != "ФИНИШ":
        word = word.lower().replace(" ", "")
        symbols += word
    symbols = sorted(symbols, reverse=True)
    print(sorted(symbols, key=lambda a: symbols.count(a))[-1])


if __name__ == "__main__":
    main()

