def main():
    """Ищем количество зайцев в n строках.
    """

    n = int(input())
    rabbits = 0
    for _ in range(n):
        word = input().lower()
        rabbits = rabbits + word.count("зайка")
    print(rabbits)


if __name__ == "__main__":
    main()
