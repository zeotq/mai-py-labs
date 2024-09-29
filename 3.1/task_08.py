def main():
    """Определяем положение зайцев в n строках.
    """

    n = int(input())
    for _ in range(n):
        word = input().lower()
        print(word.find("зайка") + 1 if "зайка" in word else "Заек нет =(")


if __name__ == "__main__":
    main()
