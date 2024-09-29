def main():
    """Сделай мне ням-ням...
    """

    variants = {
        0: "Манная",
        1: "Гречневая",
        2: "Пшённая",
        3: "Овсяная",
        4: "Рисовая"
    }

    n = int(input())
    print(*[variants[i % 5] for i in range(n)], sep="\n")


if __name__ == "__main__":
    main()
