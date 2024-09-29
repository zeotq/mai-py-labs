def main():
    """Удаляем комментарии из кода.
    """

    while (word := input()):
        if temp := word.split("#")[0]:
            print(temp)


if __name__ == "__main__":
    main()

